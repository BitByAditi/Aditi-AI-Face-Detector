import streamlit as st
import cv2
import numpy as np

st.title("🤖 Aditi's AI Face Detector")
st.write("Click 'Start' to see the AI work!")

# This creates a camera window in the browser
img_file_buffer = st.camera_input("Say cheese!")

if img_file_buffer is not None:
    # Convert the image so the AI can read it
    bytes_data = img_file_buffer.getvalue()
    cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)

    # Load the AI detector
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    gray = cv2.cvtColor(cv2_img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    # Draw the green box and show the count
    for (x, y, w, h) in faces:
        cv2.rectangle(cv2_img, (x, y), (x+w, y+h), (0, 255, 0), 5)
    
    if len(faces) > 0:
        st.success(f"Hie cutie! I found {len(faces)} human(s)!")
        st.image(cv2_img, channels="BGR")
    else:
        st.warning("No humans detected yet. Move closer!")