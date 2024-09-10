# Import packages
from pathlib import Path
import PIL

# External packages
import streamlit as st

# Local Modules
import settings
import helper

# Setting page layout
st.set_page_config(
    page_title="Dyslexic Handwriting Correction Tool",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Main page heading
st.title("Dyslexic Handwriting Correction Tool")

# Sidebar
st.sidebar.header("ML Model Config")

# Model Options
model_type = "Detection"

confidence = 0.001

# Assuming you have a list of class names
class_names = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Selecting Detection Or Segmentation
model_path = Path(settings.DETECTION_MODEL)


# Load Pre-trained ML Model
try:
    model = helper.load_model(model_path)
except Exception as ex:
    st.error(f"Unable to load model. Check the specified path: {model_path}")
    st.error(ex)

source_radio = st.sidebar.radio(
    "Select Source", settings.SOURCES_LIST)

source_img = None
# If image is selected
if source_radio == settings.IMAGE:
    source_img = st.sidebar.file_uploader(
        "Choose an image...", type=("jpg", "jpeg", "png", 'bmp', 'webp'))

    col1, col2 = st.columns(2)

    with col1:
        try:
            if source_img is None:
                default_image_path = str(settings.DEFAULT_IMAGE)
                default_image = PIL.Image.open(default_image_path)
                st.image(default_image_path, caption="Default Image",
                         use_column_width=True)
            else:
                uploaded_image = PIL.Image.open(source_img)
                st.image(source_img, caption="Uploaded Image",
                         width=60)
        except Exception as ex:
            st.error("Error occurred while opening the image.")
            st.error(ex)

    with col2:
        if source_img is None:
            default_detected_image_path = str(settings.DEFAULT_DETECT_IMAGE)
            default_detected_image = PIL.Image.open(
                default_detected_image_path)
            st.image(default_detected_image_path, caption='Detected Image',
                     use_column_width=True)
        else:
            if st.sidebar.button('Detect Objects'):
                res = model.predict(uploaded_image, conf=confidence)
                boxes = res[0].boxes
                res_plotted = res[0].plot()[:, :, ::-1]
                # st.image(res_plotted, caption='Detected Image',
                #         use_column_width=True)

                try:
                    st.write("Detection Results")
                    highest_prob_class = None
                    highest_prob = 0.0
                    for box in boxes:
                        box_data = box.data.cpu().numpy().tolist()  # Convert box data to list
                        class_id = int(box_data[0][-1])  # Assuming class ID is the last entry
                        probability = box_data[0][-2]  # Assuming probability/confidence is the second last entry

                        # Get the class name from the class ID
                        class_name = class_names[class_id] if class_id < len(class_names) else "Unknown"

                        # Update highest probability class
                        if probability > highest_prob:
                            highest_prob = probability
                            highest_prob_class = class_name

                        st.write(f"Predicted letter: {class_name}")
                    
                        
                except Exception as ex:
                    st.write("No image is uploaded yet!")
                    st.error(ex)

elif source_radio == settings.VIDEO:
    helper.play_stored_video(confidence, model)

elif source_radio == settings.WEBCAM:
    helper.play_webcam(confidence, model)

elif source_radio == settings.RTSP:
    helper.play_rtsp_stream(confidence, model)

elif source_radio == settings.YOUTUBE:
    helper.play_youtube_video(confidence, model)

else:
    st.error("Please select a valid source type!")
