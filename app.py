import streamlit as st
from PIL import Image
import numpy as np
import easyocr

img_file_buffer = st.camera_input("Take a picture")

if img_file_buffer is not None:
	# To read image file buffer as a PIL Image:
	image = Image.open(img_file_buffer)

	# streamlit write "Full image"
	st.write("Full image")
	# show the image
	st.image(image, use_column_width=True)

	# create a streamlit slider to select the height from top
	height_from_top_percent = st.slider("Height from top", 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1)
	# create a streamlit slider to select the width retained from centre
	width_retained_from_centre_percent = st.slider("Width retained from centre", 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1)

	# Crop the image
	image = image.crop((image.width * (1 - width_retained_from_centre_percent) / 2,
						image.height * height_from_top_percent,
						image.width * (1 + width_retained_from_centre_percent) / 2,
						image.height))
	
	# streamlit write "Cropped image"
	st.write("Cropped image")
	# show the image
	st.image(image, use_column_width=True)

	# Convert the image to a numpy array
	img_array = np.array(image)

	# Initialize the EasyOCR reader
	reader = easyocr.Reader(['en'])

	# Use the reader to extract text from the image
	result = reader.readtext(img_array)

	# Print the extracted text using Streamlit
	st.write(result)
