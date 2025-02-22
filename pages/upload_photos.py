import streamlit as st
import os
import cv2
import numpy as np
from datetime import datetime

def get_saved_images(directory):
    images = []
    if os.path.exists(directory):
        for file in sorted(os.listdir(directory), reverse=True):
            if file.endswith(".jpg"):
                timestamp = file.replace("photo_", "").replace(".jpg", "")
                try:
                    readable_time = datetime.strptime(timestamp, "%Y%m%d_%H%M%S").strftime("%Y-%m-%d %H:%M:%S")
                    images.append((os.path.join(directory, file), readable_time))
                except ValueError:
                    continue
    return images

# Create a directory to store images
SAVE_DIR = "captured_images"
os.makedirs(SAVE_DIR, exist_ok=True)

# Sidebar to show existing photos
st.header("Saved Photos")
saved_images = get_saved_images(SAVE_DIR)
for img_path, img_time in saved_images:
    st.image(img_path, caption=f"Taken on {img_time}", use_container_width=True)
