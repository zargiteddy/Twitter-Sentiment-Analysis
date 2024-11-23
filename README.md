**Skripsi**: https://eprints.utdi.ac.id/10057/

**Sentiment Analyzer Web App**: https://svm-sentiment-analyzer.streamlit.app/

**Artikel di Medium**: [still on progress]

### Penjelasan: 
Web App tersebut belum 100% dapat mengklasifikasi sentiment ke kelas yang benar, kemungkinan dikarenakan penelitian ini memiliki 4000 data yang jumlah negatif, positif, dan netral tidak imbang. Saya tidak sempat mengambil kumpulan data lain yang lebih bervariatif, dikarenakan di tengah penelitian terjadi pemberhentian layanan API Twitter gratis. Selain itu, tool - tool scraper yang ada di internet (seperti snscrape) sudah tidak dapat berfungsi lagi karena terkena block dari pihak Twitter, seperti pada kasus berikut: https://github.com/JustAnotherArchivist/snscrape/issues/996.

**Lalu, alasan kenapa saya memutuskan menggunakan 4000 data adalah karena:**
- SVM Classifier pada umumnya bekerja lebih baik pada dataset kecil
- Efisiensi tenaga dan waktu, karena penelitian ini sangat menguras tenaga di bagian normalisasi dan filtering
- Normalisasi ini penting untuk supaya googletrans bisa menerjemahkan dari Bahasa Indonesia ke Bahasa Inggris untuk pelabelan dengan TextBlob. Hal yang menyebabkan bagian normalisasi cukup menguras tenaga adalah banyaknya kata-kata slank atau singkatan di twitter seperti: bgt(banget), org(orang), nyinyir(menyindir), mo(mau), lo(kamu), th(tahun), dll. Saya mau tidak mau harus secara manual membuat list sejumlah 2245 kata di Microsoft Excel kemudian mengaplikasikan teknik normalisasi menggunakan Python dengan list tersebut untuk mengganti kata tidak baku menjadi baku.
- Tahap filtering juga sangat menguras tenaga karena stopwords Bahasa Indonesia yang tersedia di Internet ternyata memang belum lengkap, sehingga tidak bisa diaplikasikan ke banyak jenis dataset berbahasa Indonesia. Maka dari itu, lagi-lagi saya membuat list ratusan kata-kata tidak berguna seperti 'jsdieksisnisawikwok', 'kwkwkwkwwkwk', 'hehehee', 'tuh', 'krtsk', 'hokyahokya', 'Aksjsjsk', 'oneesan', 'tjuyyy', dan lain-lain. Lalu list tersebut dipadukan dengan stopwords yang saya download dari internet. Kemudian dengan Python saya menghilangkan kata-kata tidak berguna di dataset menggunakan list yang saya buat tersebut.

**Alasan kenapa banyak data yang terklasifikasi ke dalam kelas positif adalah kemungkinan karena terlalu banyaknya data bersentimen positif yang kemungkinan dikarenakan oleh:**
- entah karena memang dari sananya banyak data bersentimen positif, atau..
- library googletrans tidak mampu menerjemahkan tweet dengan baik, atau..
- karena TextBlob tidak mampu menentukan polaritas yang tepat, atau..
- karena SVM tidak mampu memprediksi kelas dengan benar (Linear Support Vector Machine di penelitian ini  memiliki akurasi sebesar 87,375% dengan nilai presisi 82% untuk sentimen negatif, 40% untuk sentimen netral, dan 91% untuk sentimen positif. Selain itu juga dihasilkan nilai recall 64% untuk sentimen negatif, 44% untuk sentimen netral, dan 95% untuk sentimen positif. Terakhir, f1-score untuk sentimen negatif adalah 72%, lalu 42% untuk sentimen netral, kemudian 93% untuk sentimen positif), atau..
- karena keempatnya.

**Bagi yang ingin melanjutkan atau memodifikasi penelitian ini, diharapkan dapat melakukan:**
- mengambil data tweet yang bervariatif dan lebih banyak (sekitar 10.000 data) dan menggunakan metode selain SVM
- Melakukan preprocessing dengan lebih baik terutama di tahap filtering dan normalisasi.
- menggunakan library pendeteksi sentimen selain TextBlob. Bisa menggunakan VADE (Valence Aware Dictionary and Sentiment Reasoner).
- Jika masih ingin menggunakan SVM, coba tingkatkan nilai **presisi** sentimen netral, kemudian tingkatkan nilai **recall** dan nilai **f1-score** milik sentimen negatif dan netral.

### Sekian, dan terima kasih.
