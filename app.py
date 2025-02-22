import streamlit as st
import cv2
import numpy as np
from datetime import datetime
import os

# Set up the app title
st.title("Webcam Photo Capture App")

# Create a directory to store images
SAVE_DIR = "captured_images"
os.makedirs(SAVE_DIR, exist_ok=True)

# Access the webcam
img_file_buffer = st.camera_input("Take a picture")

if img_file_buffer is not None:
    # Convert the image to OpenCV format
    image = np.array(bytearray(img_file_buffer.read()), dtype=np.uint8)
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)

    # Convert BGR to RGB
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Generate a filename with timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{SAVE_DIR}/photo_{timestamp}.jpg"

    # Save the image locally
    cv2.imwrite(filename, image)

    st.success(f"Photo saved as {filename}")
    st.image(image_rgb, caption="Captured Image", use_container_width=True)
