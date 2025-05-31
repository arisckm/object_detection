import streamlit as st
import torch
import gdown
import os
import cv2
import numpy as np
from PIL import Image

# ---- Download model from Google Drive ----
@st.cache_resource
def download_model():
    file_id = "1ObP7ZtBHguYTQ8Emtkk1f2gSu6WB0EUG"  # Your .pt file ID
    url = f"https://drive.google.com/uc?export=download&id={file_id}"
    output = "yolov5l.pt"
    if not os.path.exists(output):
        gdown.download(url, output, quiet=False)
    return output

# ---- Load YOLOv5 model ----
@st.cache_resource
def load_model():
    model_path = download_model()
    model = torch.hub.load('ultralytics/yolov5', 'custom', path=model_path, force_reload=True)
    return model

model = load_model()

st.title("YOLOv5 Object Detection 🚀")
st.markdown("Choose either image upload or use webcam (only works locally).")

mode = st.radio("Select mode:", ("Upload Image", "Use Webcam (local only)"))

# ---- Image Upload Mode ----
if mode == "Upload Image":
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
    if uploaded_file:
        image = Image.open(uploaded_file).convert("RGB")
        st.image(image, caption="Uploaded Image", use_column_width=True)

        results = model(np.array(image))
        output_image = np.squeeze(results.render())
        st.image(output_image, caption="Detected Objects", use_column_width=True)

# ---- Webcam Mode ----
elif mode == "Use Webcam (local only)":
    run = st.checkbox("Start Webcam")
    FRAME_WINDOW = st.image([])

    if run:
        cap = cv2.VideoCapture(0)
        while run:
            ret, frame = cap.read()
            if not ret:
                st.warning("Failed to grab frame.")
                break

            img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = model(img)
            annotated_frame = np.squeeze(results.render())
            FRAME_WINDOW.image(annotated_frame)

        cap.release()
    else:
        st.info("Webcam is OFF.")
