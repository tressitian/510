import streamlit as st
import cv2
import numpy as np
from datetime import datetime
import os

SAVE_DIR = "captured_images"
os.makedirs(SAVE_DIR, exist_ok=True)

def show_saved_photos():
    st.header("Saved Photos")
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
