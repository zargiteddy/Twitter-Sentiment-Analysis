import streamlit as st
from PIL import Image

st.sidebar.success("Kamu sedang berada di menu Classification Report")

st.title("Classification Report")
image = Image.open('classreport.png')
st.image(image, width = 400)
st.markdown(
  """
    - Nilai precision untuk kelas negatif sebesar 82%, 
      kelas netral sebesar 40%, kelas positif sebesar 91%. 
      Artinya presisi proporsi label yang diprediksi dengan benar dari 
      total prediksi cukup tinggi untuk kelas positif dan negatif.
    - Nilai recall kelas negatif sebesar 64%, kelas netral sebesar 44%, dan 
      kelas positif sebesar 95%. Artinya kinerja keberhasilan sistem 
      dalam menemukan kembali informasi yang bernilai positif dalam dokumen 
      lebih baik dibandingkan dengan menemukan informasi kembali yang 
      bernilai netral dan negatif.
    - Nilai F1-Score untuk kelas negatif sebesar 72%, 
      kelas netral sebesar 42%, dan kelas positif sebesar 93%. F1-Score bisa 
      diartikan sebagai harmonic mean (rata-rata yang dihitung dengan cara 
      mengubah semua data menjadi pecahan) dari precision dan recall. 
      F1-Score yang baik mengindikasikan bahwa model klasifikasi memiliki 
      precision dan recall yang baik.
"""
)