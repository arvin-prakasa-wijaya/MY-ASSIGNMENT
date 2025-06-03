# MY-ASSIGNMENT
 **KALENDER DIGITAL**
<p align="center">
  <img src="https://github.com/arvin-prakasa-wijaya/MY-ASSIGNMENT/blob/main/VISUAL%20CODE.jpg" width="1000"/>
</p>

<div align="justify">
  
  <b>INDONESIAN LANGUAGE</b><br>
  <h4>INI FIRST TIME AKU BIKIN KALENDER DIGITAL PAKEK VISUAL CODE!!!! Fyi aku baru baru ini mengenal dunia coding saat aku mulai masuk kegiatan Digital Bootcamp. Disinilah aku mulai belajar coding menggunakan bahasa Python. 
  Aku sendiri kalau belajar hal baru rasanya tidak sabaran ingin cepet mahir. Jadi rasanya pertama kali membuat kalender digital ini cukup kesel karena ngeliat beragam jenis kode yang asing diliat dan susah untuk dicerna
  sama otak ku sendiri. Ketika ada kode yang eror, greget banget ngeliatnya sampai pukul - pukul meja, padahal meja gw gak salah apa - apa. Tapi, apakah dengan membuat kalender digital ini aku langsung paham coding?? tentu tidak.
  Aku masih bener - bener mencerna beberapa jenis kode python yang asing diliat karena aku bukan anak programer. Selama 1 hari full aku membuat tugas ini, aku gak sendirian karena aku ditemenin sama mentor AI ku: ChatGPT 🤖✨ </h4>
  
</div>

<div align="justify">
  
  <b>ENGLISH LANGUAGE</b><br>
  <h4>THIS IS MY FIRST TIME MAKING A DIGITAL CALENDAR USING VISUAL CODE!!!! FYI, I just recently got into the world of coding when I joined a Digital Bootcamp. That’s where I started learning to code using Python. When I’m learning something new, I tend to get impatient because I want to master it quickly. So honestly, making this digital calendar for the first time was pretty frustrating. I saw so many unfamiliar lines of code that were hard for my brain to process. When there was an error in the code, I got so triggered I ended up punching the table even though the table didn’t do anything wrong. But, did making this digital calendar suddenly make me understand coding? Of course not. I’m still trying to digest a bunch of Python code that looks foreign to me, since I’m not a programmer kid. I worked on this task for a full day, and I wasn’t alone, I was accompanied by my AI mentor: ChatGPT 🤖✨</h4>
  
</div>

# KODE PROGRAM
```python
print("="*51)
print("MASUKKAN TANGGAL UNTUK CEK HARI DAN  TAHUN KABISAT.")
while True:
    try:
        tanggal = int(input("Masukkan tanggal: "))
        if 1 <= tanggal <=31:
            break
        else:
            print("Tanggal tidak valid")
    except ValueError:
        print("Harap masukan angka, bukan huruf!")


while True:
    try:
        bulan = int(input("Masukkan bulan: "))
        if 1 <= bulan <=12:
            break
        else:
            print("Bulan tidak valid")
    except ValueError:
        print("Harap masukin angka, bukan huruf!")

while True:
    try:
        tahun = int(input("Masukkan tahun: "))
        if 1 <= tahun:
            break
        else:
            print("Tahun tidak valid!")
    except ValueError:
        print("Harap masukin angka, bukan huruf!")
        

awal = tahun - 2
akhir = tahun + 2
print("\nHASIL PEMERIKSAAN TAHUN KABISAT:")

for year in range(awal, akhir + 1):
    if (year % 4 == 0 and year % 100 != 0) or (year %400 ==0):
        print(f"Tahun {year} merupakan tahun kabisat")

    else:
        print(f"Tahun {year} merupakan bukan tahun kabisat")


import datetime
tanggal_masuk = datetime.date(tahun, bulan, tanggal)
        
nama_hari = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]

hari = tanggal_masuk.weekday()

print(f"\nPada tanggal {tanggal:02d}/{bulan:02d}/{tahun} merupakan hari {nama_hari[hari]}")


