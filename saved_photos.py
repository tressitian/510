import streamlit as st
import cv2
import numpy as np
from datetime import datetime
import os
from PIL import Image
import pandas as pd
import base64
from io import BytesIO

SAVE_DIR = "captured_images"
os.makedirs(SAVE_DIR, exist_ok=True)

def image_to_base64(img):
    buffered = BytesIO()
    img.save(buffered, format="JPEG")
    return base64.b64encode(buffered.getvalue()).decode()

def show_saved_photos():
    st.header("Saved Photos")
    
    # Camera input section
    img_file_buffer = st.camera_input("Take a picture")
    if img_file_buffer is not None:
        image = np.array(bytearray(img_file_buffer.read()), dtype=np.uint8)
        image = cv2.imdecode(image, cv2.IMREAD_COLOR)
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{SAVE_DIR}/photo_{timestamp}.jpg"
        cv2.imwrite(filename, image)
        st.success(f"Photo saved as {filename}")
        st.image(image_rgb, caption="Captured Image", use_container_width=True)

    # Get list of photos and create DataFrame
    photos = os.listdir(SAVE_DIR)
    photos = [p for p in photos if p.endswith(('.jpg', '.jpeg', '.png'))]
    
    if not photos:
        st.info("No photos captured yet!")
        return

    # Create data for DataFrame
    data = []
    for photo in photos:
        # Parse date from filename (format: photo_YYYYMMDD_HHMMSS.jpg)
        date_str = photo[6:21]  # Extract YYYYMMDD_HHMMSS
        try:
            date_obj = datetime.strptime(date_str, "%Y%m%d_%H%M%S")
            formatted_date = date_obj.strftime("%Y-%m-%d %H:%M:%S")
        except ValueError:
            formatted_date = "Unknown date"

        # Load and resize image
        img_path = os.path.join(SAVE_DIR, photo)
        img = Image.open(img_path)
        img.thumbnail((100, 100))  # Smaller thumbnails for grid
        
        # Convert image to base64
        img_base64 = image_to_base64(img)
        img_html = f'<img src="data:image/jpeg;base64,{img_base64}" width="100">'
        
        data.append({
            "Image": img_html,
            "Date Taken": formatted_date,
            "Filename": photo
        })

    # Create DataFrame and sort by date
    df = pd.DataFrame(data)
    df = df.sort_values("Date Taken", ascending=False)

    # Display as grid
    st.write(
        df.to_html(
            escape=False,
            index=False
        ),
        unsafe_allow_html=True
    )