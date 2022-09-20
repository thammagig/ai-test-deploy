#Library imports
import numpy as np
import streamlit as st
import cv2
from keras.models import load_model

#import joblib
from keras.preprocessing import image
from io import BytesIO
from tensorflow.keras.applications import resnet50


df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})

st.write("Here's our first attempt at using data to create a table:")
st.write(df)

st.write("555555")

