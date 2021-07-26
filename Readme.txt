Implementasi Topological Sort dengan pendekatan Decrease and
Conquer dalam pemecahan masalah penentuan urutan pengambilan
mata kuliah.

PENJELASAN SINGKAT ALGORITMA :
Adapun garis besar dari algoritma ini adalah dengan mereduksi
mata kuliah yang tidak memiliki pre-requisite dari dalam senarai
ketetanggaan, lalu menghapus mata kuliah tersebut dari dalam
senarai ketetanggaan simpul yang bertetangga dengannya, kemudian
memasukkan mata kuliah tersebut ke dalam himpunan solusi, hal ini
diulang terus di setiap iterasinya sampai senarai ketetanggaan kosong,
dan akhirnya diperoleh himpunan solusi berupa urutan pengambilan
mata kuliah di setiap semesternya

REQUIREMENT PROGRAM :
1. Memiliki Python 3.7 keatas
2. Sudah menginstall library "PySimpleGUI" (jika belum, bisa di-install)
   dengan mengetik "pip install PySimpleGUI" di terminal

CARA MENGGUNAKAN PROGRAM :

A. Menggunakan Source Code Program :
   Dalam folder src terdapat 2 buah source code .py, yaitu:
   1. SmortPRS_13519059.py
   2. SmortPRS_GUI_13519059.py

   Dimana SmortPRS.py adalah source code yang menerima input dan
   memberikan output di terminal / CLI, sedangkan SmortPRS_GUI.py
   menerima input dan memberikan output melalui GUI-nya sendiri

   Cara Penggunaan SmortPRS_13519059.py :
   1. Buka terminal, lalu cd ke folder src
   2. Pastikan Line 74 - 77 SmortPRS.py tidak dikomentari
   3. Jalankan "py SmortPRS.py"
   4. Masukkan input nama file sesuai nama file yang ada dalam folder
      test

   Cara Penggunaan SmortPRS_GUI_13519059.py :
   1. Buka terminal, lalu cd ke folder src
   2. Pastikan Line 74 - 77 SmortPRS.py sudah dikomentari
   3. Jalankan "py SmortPRS_GUI.py"
   4. Tekan tombol "Folder" untuk memilih folder tempat input file
      .txt berada, dalam hal ini folder test
   5. Tekan nama file yang ingin anda ketahui outputnya
   6. Output akan ditampilkan di kolom sebelah kanan
   7. Jika masih ingin memilih file lain, tekan tombol "Clear"
      terlebih dahulu untuk mereset output, kemudian klik lagi
      nama file yang ingin diketahui outputnya seperti pada
      langkah (5)

B. Menggunakan executable file program :
   Dalam Folder bin terdapat file "SmortPRS_GUI_13519059.exe", silahkan
   jalankan executable file-nya, untuk petunjuk penggunaannya sama dengan
   petunjuk penggunaan SmortPRS_GUI_13519059.py di poin (A)

AUTHOR :
Nama  : Denilsen Axel Candiasa
NIM   : 13519059
Email : 13519059@std.stei.itb.ac.id