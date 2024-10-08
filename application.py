import streamlit as st
import os
import uuid
from src.documentsai import ocr_doc
from dotenv import load_dotenv

# Load the .env file
load_dotenv()


PROJECT_ID = os.getenv('PROJECT_ID')
LOCATION =  os.getenv('LOCATION')  
PROCESSOR_ID = os.getenv('PROCESSOR_ID') 



# Define the folder to save the uploaded files
UPLOAD_FOLDER = "uploaded_files"

# Ensure the folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Function to delete existing files in the folder
def delete_existing_files(folder):
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)  # Delete the file
        except Exception as e:
            st.error(f"Error deleting file {file_path}: {e}")

# Streamlit file upload component
uploaded_file = st.file_uploader("Choose an image...", type=["jpeg"])

if uploaded_file is not None:
    # Delete any existing file before saving the new one
    delete_existing_files(UPLOAD_FOLDER)
    
    # Generate a unique filename
    unique_filename = str(uuid.uuid4()) + "_" + uploaded_file.name
    
    # Define the save path
    save_path = os.path.join(UPLOAD_FOLDER, unique_filename)
    
    # Save the file in the folder
    with open(save_path, "wb") as f:
        f.write(uploaded_file.getbuffer())


    # col1, col2 = st.columns([2,2])    

    result = ocr_doc(PROJECT_ID,LOCATION,PROCESSOR_ID,save_path) 
    st.write(result)


    # with col1:
    #  st.image(save_path, caption="Uploaded Image", use_column_width=True)

    # with col2:
    #  st.write(result)
    
    # Confirmation message
    # st.success(f"File saved as {unique_filename}")
    
    # # Display the uploaded image
    # st.image(save_path, caption="Uploaded Image", use_column_width=True)
