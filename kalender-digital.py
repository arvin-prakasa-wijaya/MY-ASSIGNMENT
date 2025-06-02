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