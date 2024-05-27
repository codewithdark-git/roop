import streamlit as st
from PIL import Image
import subprocess
import os

def run_face_swap(source_path, target_path, output_path):
    command = ['python', 'run.py', '-s', source_path, '-t', target_path, '-o', output_path]
    subprocess.run(command)

st.title("Face Swapper")

source_file = st.file_uploader("Upload Source Image", type=["jpg", "jpeg", "png"])
target_file = st.file_uploader("Upload Target Image or Video", type=["jpg", "jpeg", "png", "mp4"])

if source_file and target_file:
    source_path = os.path.join("uploads", "source.jpg")
    target_path = os.path.join("uploads", "target" + os.path.splitext(target_file.name)[1])
    output_path = os.path.join("outputs", "output" + os.path.splitext(target_file.name)[1])

    os.makedirs("uploads", exist_ok=True)
    os.makedirs("outputs", exist_ok=True)

    with open(source_path, "wb") as f:
        f.write(source_file.getbuffer())
    with open(target_path, "wb") as f:
        f.write(target_file.getbuffer())

    if st.button("Swap Faces"):
        run_face_swap(source_path, target_path, output_path)
        if target_file.type.startswith("video"):
            st.video(output_path)
        else:
            st.image(output_path, caption="Output Image")

if __name__ == "__main__":
    st.run()
