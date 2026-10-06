import json

path = r"C:\Users\ASUS TUF GK\Music\BELAJAR CODING\studi_kasus6\nilaimahasiswa.json"

with open(path,"r",encoding="utf-8")as f:
    data = json.load(f)

def tampilkan_data():
    print("\n--- Data Nilai Mahasiswa ---")

    if len(data) == 0:
        print("Belum ada data.")
    else:
        for mahasiswa in data:
            print("Nama :", mahasiswa["nama"])
            print("NIM  :", mahasiswa["nim"])
            print("Nilai:", mahasiswa["nilai"])
            print("-------------------------")


def tambah_data(nama, nim, nilai):
    data.append({
        "nama": nama,
        "nim": nim,
        "nilai": nilai
    })

    return "Data ditambah!"

def simpan_file():
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

    return "Data tersimpan ke nilai_mahasiswa.json!"


while True:
    print("\n=== SISTEM PENCATATAN NILAI MAHASISWA ===")
    print("1. Tampilkan Data")
    print("2. Tambah Data")
    print("3. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        tampilkan_data()

    elif pilihan == "2":
        nama = input("Masukkan nama : ")
        nim = input("Masukkan NIM  : ")
        nilai = int(input("Masukkan nilai: "))

        print(tambah_data(nama, nim, nilai))
        print(simpan_file())

    else:
        print("Pilihan tidak tersedia!")