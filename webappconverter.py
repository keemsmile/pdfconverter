import os
import streamlit as st
from pdf2image import convert_from_path
from PIL import Image
import tempfile

def pdf_to_jpg(pdf_path, output_folder, dpi=300, poppler_path=r'C:\poppler-24.08.0\Library\bin'):
    """
    Converts each page of the given PDF to a JPG image.
    """
    # Check if the output folder exists, if not, create it
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    try:
        # Convert the PDF pages to images
        images = convert_from_path(pdf_path, dpi=dpi, poppler_path=poppler_path)

        # Save each page as a separate JPG file
        saved_images = []
        for i, image in enumerate(images):
            image_path = os.path.join(output_folder, f"page_{i + 1}.jpg")
            image.save(image_path, 'JPEG')
            saved_images.append(image_path)
            st.success(f"Saved: {image_path}")

        return saved_images
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return []

# Streamlit Web App
def main():
    st.set_page_config(page_title="PDF to JPG Converter", page_icon="📄", layout="wide")
    
    # Load custom CSS
    with open("style.css") as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    
    st.title("PDF to JPG Converter")
    st.write("Upload a PDF file and convert its pages to high-quality JPG images.")

    col1, col2 = st.columns([2, 1])

    with col1:
        uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

    with col2:
        st.write("## How it works")
        st.write("1. Upload your PDF file")
        st.write("2. We'll convert each page to a JPG image")
        st.write("3. Download the converted images")

    if uploaded_file is not None:
        try:
            # Create a temporary file
            with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as tmp_file:
                tmp_file.write(uploaded_file.getvalue())
                pdf_path = tmp_file.name

            # Convert PDF to JPG
            with st.spinner("Converting PDF to JPG..."):
                saved_images = pdf_to_jpg(pdf_path, "output_images")

            # Display the images
            if saved_images:
                st.success("Conversion successful! Here are your JPG images:")
                
                for i, img_path in enumerate(saved_images):
                    col1, col2 = st.columns([3, 1])
                    with col1:
                        st.image(img_path, caption=f"Page {i+1}")
                    with col2:
                        with open(img_path, "rb") as file:
                            st.download_button(
                                label=f"Download Page {i+1}",
                                data=file,
                                file_name=f"page_{i+1}.jpg",
                                mime="image/jpeg"
                            )
            
            # Clean up the temporary PDF file
            os.unlink(pdf_path)

        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
            
if __name__ == "__main__":
    main()
