import streamlit as st
import cv2
import numpy as np
from datetime import datetime
import os
from PIL import Image
import json
from utils.gpt_vision import call_gpt4_vision  # Update import
import time

SAVE_DIR = "captured_images"
os.makedirs(SAVE_DIR, exist_ok=True)

def save_photo_metadata(photo_filename, tags=None):
    """Save metadata for a photo in a JSON file"""
    metadata = {
        "date_taken": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "clothing_tags": tags or [],  # Default empty list if no tags provided
        "date_wore": [datetime.now().strftime("%Y-%m-%d")]  # Initialize with today's date
    }
    
    # Save with same name as photo but .json extension
    json_filename = photo_filename + '.json'
    with open(json_filename, 'w') as f:
        json.dump(metadata, f, indent=4)

def show_saved_photos():
    # Initialize session state for photo processing
    if 'processing_photo' not in st.session_state:
        st.session_state.processing_photo = False
    if 'last_photo_time' not in st.session_state:
        st.session_state.last_photo_time = None
    if 'new_photo_taken' not in st.session_state:
        st.session_state.new_photo_taken = False

    st.header("Your Photos")
    
    # Get list of photos and sort by date (newest first)
    photos = os.listdir(SAVE_DIR)
    photos = [p for p in photos if p.endswith(('.jpg', '.jpeg', '.png'))]
    photos.sort(reverse=True)

    # Display existing photos first
    if photos:
        # Define a fixed display size for all images
        DISPLAY_SIZE = (300, 300)
        
        # Create three columns for photo display
        col1, col2, col3 = st.columns(3)
        
        # Distribute photos across columns
        for idx, photo in enumerate(photos):
            # Load image and resize to fixed dimensions
            img_path = os.path.join(SAVE_DIR, photo)
            img = Image.open(img_path)
            img = img.resize(DISPLAY_SIZE, Image.Resampling.LANCZOS)
            
            # Load metadata if exists
            json_path = img_path + '.json'
            if os.path.exists(json_path):
                with open(json_path, 'r') as f:
                    metadata = json.load(f)
                
                # Display in appropriate column
                col = [col1, col2, col3][idx % 3]
                with col:
                    st.image(img, use_container_width=True)
                    st.caption(f"👕 Type: {metadata['type']}")
                    st.caption(f"✨ Style: {metadata['style']}")
                    st.caption(f"🎨 Color: {metadata['color']}")
                    st.caption(f"📅 Last worn: {metadata['date_wore'][-1]}")
            else:
                # Display without metadata
                col = [col1, col2, col3][idx % 3]
                with col:
                    st.image(img, use_container_width=True)
                    st.caption(f"ℹ️ No metadata available")
    else:
        st.info("No photos captured yet!")

    # Camera input section at the bottom
    st.header("Take a New Photo")
    st.info("📸 The photo will be automatically cropped to a square from the center after capture.")
    img_file_buffer = st.camera_input(
        "Take a picture",
        key="camera",
        help="The photo will be cropped to a square after capture",
        disabled=st.session_state.processing_photo,
        label_visibility="visible"
    )
    
    if (img_file_buffer is not None and 
        not st.session_state.processing_photo and 
        not st.session_state.new_photo_taken):  # Only process if it's a new photo
        
        st.session_state.processing_photo = True
        st.session_state.new_photo_taken = True
        
        # Generate filename using timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{SAVE_DIR}/photo_{timestamp}.jpg"
        json_filename = filename + '.json'
        
        image = np.array(bytearray(img_file_buffer.read()), dtype=np.uint8)
        image = cv2.imdecode(image, cv2.IMREAD_COLOR)
        
        # Make the image square by cropping to the smaller dimension
        height, width = image.shape[:2]
        size = min(height, width)
        start_x = (width - size) // 2
        start_y = (height - size) // 2
        cropped_image = image[start_y:start_y+size, start_x:start_x+size]
        
        image_rgb = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2RGB)
        cv2.imwrite(filename, cropped_image)
        
        # Get metadata from GPT
        metadata = get_clothing_metadata_from_gpt(filename)
        if metadata:
            # Save metadata to JSON file
            with open(json_filename, 'w') as f:
                json.dump(metadata, f, indent=4)
            st.success(f"Photo and metadata saved successfully!")
            
            # Create three columns for preview
            preview_col1, preview_col2, preview_col3 = st.columns(3)
            with preview_col2:  # Use middle column for centered preview
                st.image(image_rgb, caption="Captured Image (Square Crop)", use_container_width=True)
            
            # Reset processing flag and rerun
            st.session_state.processing_photo = False
            st.rerun()
        else:
            st.warning("Photo saved but couldn't generate metadata")
            if os.path.exists(filename):
                os.remove(filename)  # Clean up the photo if metadata generation failed
            st.session_state.processing_photo = False
            st.session_state.new_photo_taken = False

    # Reset new_photo_taken flag when camera input is cleared
    if img_file_buffer is None:
        st.session_state.new_photo_taken = False

def get_clothing_metadata_from_gpt(image_path):
    """Use GPT-4-vision to analyze the clothing image and return metadata"""
    prompt = """Analyze this clothing item and provide ONLY a JSON object with these exact keys:
    {
        "type": "the type of clothing (e.g., jacket, shirt, pants, dress)",
        "style": "the style (e.g., casual, formal, sporty)",
        "color": "the primary color"
    }"""
    
    try:
        response = call_gpt4_vision(image_path, prompt)
        content = response.choices[0].message.content.strip()
        content = content.replace('\n', '').replace('\r', '').strip()
        if content.startswith('```json'):
            content = content[7:-3].strip()
        elif content.startswith('```'):
            content = content[3:-3].strip()
            
        metadata = json.loads(content)
        metadata["date_wore"] = [datetime.now().strftime("%Y-%m-%d")]
        return metadata
    except Exception as e:
        st.error(f"Error analyzing image: {str(e)}")
        return None