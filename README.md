# AI Coursework Automation: Jupyter Notebook and LaTeX Pipeline

Repositori ini berisi sistem otomasi agen AI (AI Agent Prompt/Instruction) yang dirancang secara profesional sebagai AI Engineer Senior dan Asisten Akademik. Agen ini bertugas menganalisis instruksi tugas kuliah Kecerdasan Buatan (Artificial Intelligence), mengembangkan kode berbasis Jupyter Notebook (.ipynb) yang siap pakai di Google Colab, melakukan pengujian metrik evaluasi secara otomatis, membuat visualisasi, hingga menyusun laporan akademik siap cetak berbasis LaTeX (.tex).

---

## Fitur Utama dan Keunggulan Pipeline

- Robust Data Loading: Dilengkapi penanganan try-except FileNotFoundError adaptif untuk mencegah error path saat dijalankan di Google Colab maupun lokal.
- Robust NLP Preprocessing: Penanganan otomatis konversi kolom teks ke tipe string untuk mencegah kegagalan TfidfVectorizer akibat nilai NaN atau data campuran.
- Automated Evaluation Metrics: Ekstraksi otomatis metrik Accuracy, Precision, Recall, dan F1-Score lengkap dengan visualisasi Confusion Matrix.
- Overleaf-Ready Reports: Penyusunan laporan terstruktur berstandar akademik langsung ke format .tex lengkap dengan tabel performa dan injeksi gambar.

---

## Alur Kerja Sistem (Workflow Execution Steps)

[Mulai] -> 1. Analisis Instruksi & Dataset (.csv/.json)
               │
               ▼
         2. Pengembangan Jupyter Notebook (.ipynb) di hasil/
               │
               ▼
         3. Dummy Run & Ekstraksi Metrik (Accuracy, F1-Score)
               │
               ▼
         4. Ekspor Visualisasi (.png) (Confusion Matrix, dll.)
               │
               ▼
         5. Generasi Dokumen Akademik LaTeX (.tex)
               │
               ▼
[Selesai] -> 6. Pengemasan Arsip ZIP untuk Overleaf

### Detail Langkah Eksekusi:
1. Analisis Instruksi Tugas: Agen membaca berkas deskripsi tugas dan skema dataset, mengidentifikasi algoritma optimal (SVM, Naive Bayes, Random Forest, dll.), dan metrik evaluasi wajib.
2. Pengembangan Kode (Jupyter Notebook): Struktur notebook dipecah secara modular menjadi bagian Identitas, Preprocessing, Pemodelan, dan Evaluasi menggunakan pustaka nbformat.
3. Pengujian dan Validasi: Kode dieksekusi secara internal untuk mengamankan data performa sebelum ditulis ke dalam laporan ilmiah.
4. Visualisasi: Plotting grafik distribusi kelas atau evaluasi model diekspor langsung ke direktori keluaran.
5. Penyusunan Laporan LaTeX: Melakukan penyusunan anotasi laporan ilmiah lengkap dengan blok author, begin{table}, dan begin{figure}.
6. Pengemasan Berkas: Melakukan kompresi otomatis untuk mempermudah manajemen berkas oleh pengguna akhir.

---

## Struktur Direktori Hasil Output

Seluruh file yang diproduksi oleh AI Agent akan disimpan pada folder hasil/ dengan struktur sebagai berikut:

proyek-ai-automation/
├── hasil/
│   ├── [Nama_Tugas].ipynb      # Jupyter Notebook siap pakai di Google Colab
│   ├── [Nama_Grafik].png       # Dokumentasi visualisasi/Confusion Matrix
│   ├── [Laporan_Tugas].tex     # File source laporan akademik LaTeX
│   └── [Laporan_Tugas].zip     # Arsip zip berisi (.tex + .png) siap unggah ke Overleaf
└── README.md                   # Dokumentasi utama proyek

---

## Panduan Penggunaan dan Panduan Deployment

### A. Menjalankan Jupyter Notebook di Google Colab
1. Buka Google Colab di browser Anda.
2. Pilih tab Upload dan unggah berkas [Nama_Tugas].ipynb dari direktori hasil/.
3. Unggah dataset pendukung (misal file .csv atau .json) ke panel Files di bagian kiri Google Colab Anda.
4. Jalankan seluruh cells melalui menu Runtime > Run all.

### B. Menyusun Laporan di Overleaf (LaTeX)
1. Masuk ke akun Overleaf Anda.
2. Buat proyek baru melalui New Project > Blank Project.
3. Pilih opsi Upload pada menu kiri atas Overleaf.
4. Seret dan lepas berkas kompresi [Laporan_Tugas].zip dari direktori hasil/. Overleaf akan mengekstrak berkas .tex dan gambar .png secara otomatis.
5. Klik tombol Recompile untuk melihat pratinjau dokumen PDF laporan akademik Anda.

---

## Target Checklist Output

Sebelum agen AI menyelesaikan tugasnya, verifikasi keberadaan file berikut pada sistem:

- [ ] hasil/[Nama_Tugas].ipynb tersedia dan valid secara sintaksis JSON.
- [ ] hasil/[Nama_Grafik].png berhasil digenerasi dengan resolusi yang jelas.
- [ ] hasil/[Laporan_Tugas].tex memuat metadata identitas mahasiswa yang lengkap.
- [ ] hasil/[Laporan_Tugas].zip berisi seluruh dependensi penulisan laporan.

---

## Konfigurasi Identitas Mahasiswa

Sebelum menjalankan instruksi sistem prompt, pastikan variabel berikut telah disesuaikan di lingkungan agen Anda:
- NAMA_ANDA : Nama lengkap Anda untuk dicantumkan pada Notebook dan LaTeX.
- NIM_ANDA  : Nomor Induk Mahasiswa.
- JURUSAN_ANDA : Program studi saat ini (misal: Teknik Komputer atau Informatika).
- UNIVERSITAS_ANDA : Nama perguruan tinggi.

---
Dokumentasi Otomasi Sistem Tugas Akademik AI.