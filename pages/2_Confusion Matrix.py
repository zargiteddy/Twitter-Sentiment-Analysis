import streamlit as st
from PIL import Image

st.sidebar.success("Kamu sedang berada di menu Confusion Matrix")

st.title("Confusion Matrix")
image = Image.open('confusionmatrix.png')
st.image(image, width = 400)
st.markdown(
    """
    - 102 data negatif yang teridentifikasi dengan 
      benar bersentimen negatif, 
      10 data negatif teridentifikasi netral, 
      dan 47 data negatif teridentifikasi positif.
    - 12 data netral benar teridentifikasi dengan benar 
      bersentimen netral, 2 data netral teridentifikasi 
      negatif, dan 13 data netral teridentifikasi positif.
    - 585 data positif teridentifikasi dengan benar 
      bersentimen positif, 21 data positif teridentifikasi 
      negatif, dan 8 data positif teridentifikasi netral.
"""
)