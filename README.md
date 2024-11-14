**Skripsi**: https://eprints.utdi.ac.id/10057/

**Sentiment Analyzer Web App**: https://svm-sentiment-analyzer.streamlit.app/

**Artikel di Medium**: [still on progress]

### Penjelasan: 
Web App tersebut belum 100% dapat mengklasifikasi sentiment ke kelas yang benar, kemungkinan dikarenakan penelitian ini memiliki 4000 data yang jumlah negatif, positif, dan netral tidak imbang. Saya tidak sempat mengambil kumpulan data lain yang lebih bervariatif, dikarenakan di tengah penelitian terjadi pemberhentian layanan API Twitter gratis. Selain itu, tool - tool scraper yang ada di internet (seperti snscrape) sudah tidak dapat berfungsi lagi karena terkena block dari pihak Twitter, seperti pada kasus berikut: https://github.com/JustAnotherArchivist/snscrape/issues/996.

Lalu, alasan kenapa saya memutuskan menggunakan 4000 data adalah karena:
- SVM Classifier pada umumnya bekerja lebih baik pada dataset kecil
- Efisiensi tenaga dan waktu, karena penelitian ini sangat menguras tenaga di bagian normalisasi dan filtering
- Normalisasi ini penting untuk supaya googletrans bisa menerjemahkan dari Bahasa Indonesia ke Bahasa Inggris untuk pelabelan dengan TextBlob. Hal yang menyebabkan bagian normalisasi cukup menguras tenaga adalah banyaknya kata-kata slank atau singkatan di twitter seperti: bgt(banget), org(orang), nyinyir(menyindir), mo(mau), lo(kamu), th(tahun), dll. Saya mau tidak mau harus secara manual membuat list sejumlah 2245 kata di Microsoft Excel kemudian mengaplikasikan teknik normalisasi menggunakan Python dengan list tersebut untuk mengganti kata tidak baku menjadi baku.
- Tahap filtering juga sangat menguras tenaga karena stopwords Bahasa Indonesia yang tersedia di Internet ternyata memang belum lengkap, sehingga tidak bisa diaplikasikan ke banyak jenis dataset berbahasa Indonesia. Maka dari itu, lagi-lagi saya membuat list ratusan kata-kata tidak berguna seperti 'jsdieksisnisawikwok', 'kwkwkwkwwkwk', 'hehehee', 'tuh', 'krtsk', 'hokyahokya', 'Aksjsjsk', 'oneesan', 'tjuyyy', dan lain-lain. Lalu list tersebut dipadukan dengan stopwords yang saya download dari internet. Kemudian dengan Python saya menghilangkan kata-kata tidak berguna di dataset menggunakan list yang saya buat tersebut.

Sekian, dan terima kasih.
