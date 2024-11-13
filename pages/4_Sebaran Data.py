import streamlit as st
from PIL import Image

st.sidebar.success("Kamu sedang berada di menu Sebaran Data")

st.title("Sebaran Sentimen Data Tweet")
images = ['bar.png', 'pie.png']
st.image(images, width=150 * len(images))
st.markdown(
    """
    Dengan menggunakan bar chart dan pie chart, bisa diketahui sebaran
    sentimen data tweet selama bulan Maret dan April 2023. Data sentimen positif
    memiliki jumlah paling banyak yaitu 3069 data. Data sentiment negatif
    berada di urutan ke-2 yaitu berjumlah 794 data. Data sentimen netral
    memiliki data paling sedikit yaitu 137 data.

    """
)