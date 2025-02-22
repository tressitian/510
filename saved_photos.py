import streamlit as st
import cv2
import numpy as np
from datetime import datetime
import os
from PIL import Image
import json

SAVE_DIR = "captured_images"
os.makedirs(SAVE_DIR, exist_ok=True)

def show_saved_photos():
    st.header("Your Photos")
    
    # Get list of photos and sort by date (newest first)
    photos = os.listdir(SAVE_DIR)
    photos = [p for p in photos if p.endswith(('.jpg', '.jpeg', '.png'))]
    photos.sort(reverse=True)

    if photos:
        # Create three columns for photo display
        col1, col2, col3 = st.columns(3)
        
        # Distribute photos across columns
        for idx, photo in enumerate(photos):
            # Parse date from filename
            date_str = photo[6:21]
            try:
                date_obj = datetime.strptime(date_str, "%Y%m%d_%H%M%S")
                formatted_date = date_obj.strftime("%Y-%m-%d %H:%M:%S")
            except ValueError:
                formatted_date = "Unknown date"

            # Load image
            img_path = os.path.join(SAVE_DIR, photo)
            img = Image.open(img_path)
            img.thumbnail((300, 300))
            
            # Display in appropriate column
            col = [col1, col2, col3][idx % 3]
            with col:
                st.image(img, use_container_width=True)
                
                # Load and display metadata if exists
                json_path = os.path.splitext(img_path)[0] + '.json'
                if os.path.exists(json_path):
                    with open(json_path, 'r') as f:
                        metadata = json.load(f)
                    
                    st.caption(f"📅 Taken: {metadata['date_taken']}")
                    st.caption(f"🏷️ Tags: {', '.join(metadata['clothing_tags'])}")
                    st.caption(f"👔 Last worn: {metadata['date_wore'][-1]}")
                else:
                    st.caption(formatted_date)
    else:
        st.info("No photos captured yet!")

    # Camera input section at the bottom
    st.header("Take a New Photo")
    st.info("📸 The photo will be automatically cropped to a square from the center after capture.")
    img_file_buffer = st.camera_input(
        "Take a picture",
        key="camera",
        help="The photo will be cropped to a square after capture",
        disabled=False,
        label_visibility="visible"
    )
    if img_file_buffer is not None:
        image = np.array(bytearray(img_file_buffer.read()), dtype=np.uint8)
        image = cv2.imdecode(image, cv2.IMREAD_COLOR)
        
        # Make the image square by cropping to the smaller dimension
        height, width = image.shape[:2]
        size = min(height, width)
        start_x = (width - size) // 2
        start_y = (height - size) // 2
        cropped_image = image[start_y:start_y+size, start_x:start_x+size]
        
        image_rgb = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2RGB)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{SAVE_DIR}/photo_{timestamp}.jpg"
        cv2.imwrite(filename, cropped_image)
        st.success(f"Photo saved as {filename}")
        
        # Create three columns for preview
        preview_col1, preview_col2, preview_col3 = st.columns(3)
        with preview_col2:  # Use middle column for centered preview
            st.image(image_rgb, caption="Captured Image (Square Crop)", use_container_width=True)