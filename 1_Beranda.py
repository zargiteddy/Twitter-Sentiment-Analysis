import streamlit as st
import streamlit as st
from googletrans import Translator
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import openpyxl
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn import svm

st.write("# Selamat Datang di Web App Analisis Sentimen Linear SVM! 👋")

st.markdown(
    """
    *Web Application* ini merupakan *sentiment analyzer* yang dibuat menggunakan model
    machine learning dengan metode *Linear Support Vector Machine* yang
    memiliki akurasi sebesar 87,375%. *Sentiment analyzer* ini memberikan output 
    berupa tiga kelas sentimen yaitu **positif✔️, netral➖,** atau **negatif❌**.
"""
)

st.sidebar.success("Menu Sidebar 👆")

#---------------------------------------#

#Read data
data = pd.read_excel('labeled.xlsx')
df=pd.DataFrame(data)

#Split data training dan testing
y=df.score.values
x=df.english.values
x_train, x_test, y_train, y_test = train_test_split(x, y, stratify = y, random_state=1,
                                    test_size=0.2, shuffle=True)

#CountVectorizer dan N-Gram
vectorizer = CountVectorizer(analyzer = 'word', ngram_range=(1,1), binary=True, stop_words='english')
vectorizer.fit (list(x_train) + list(x_test))
x_train_vec = vectorizer.transform(x_train)
x_test_vec = vectorizer.transform(x_test)

#Membuat Classifier SVM Linear
linear = svm.SVC(kernel='linear', C=1)
linear.fit(x_train_vec, y_train).predict(x_test_vec)

#Input teks
translator = Translator()
message = st.text_area("Ketik teks di bawah ini 👇")
try:
  translated_text = str(translator.translate(message,src='id',dest='en'))
except TypeError:
  pass

#Klasifikasi
if st.button("Klasifikasi sentimen teks"):
    text_vector = vectorizer.transform([translated_text])
    st.success(linear.predict(text_vector))
