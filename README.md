nama: muhammad azzam juhd
nim: 2609116089
kelas: c

# Sistem Pencatatan Nilai Mahasiswa

## Penjelasan Kode

`import json` digunakan untuk mengimpor library JSON agar program dapat membaca dan menyimpan data dalam format JSON.

`path` digunakan untuk menentukan lokasi file `nilaimahasiswa.json` yang menjadi tempat penyimpanan data mahasiswa.

`with open(path, "r", encoding="utf-8")` digunakan untuk membuka file JSON dalam mode membaca, kemudian `json.load(f)` digunakan untuk mengambil data dari file dan menyimpannya ke dalam variabel `data`.

Function `tampilkan_data()` digunakan untuk menampilkan data mahasiswa. `if len(data) == 0` digunakan untuk mengecek apakah data masih kosong. Jika ada data, `for mahasiswa in data` digunakan untuk menampilkan nama, NIM, dan nilai setiap mahasiswa.

Function `tambah_data()` digunakan untuk menambahkan data mahasiswa baru. `data.append()` digunakan untuk memasukkan data nama, NIM, dan nilai ke dalam list.

Function `simpan_file()` digunakan untuk menyimpan data yang sudah ditambahkan ke file JSON. `json.dump()` digunakan untuk menulis data ke dalam file sehingga data tetap tersimpan secara permanen.

`while True` digunakan agar program dapat berjalan terus menerus dan menampilkan menu berulang kali. `input()` digunakan untuk menerima pilihan dari pengguna. `if`, `elif`, dan `else` digunakan untuk menentukan proses sesuai pilihan menu. Jika pengguna memilih menu 1, program menampilkan data. Jika memilih menu 2, program meminta data mahasiswa dan menyimpannya. Jika memilih menu 3, `break` digunakan untuk menghentikan program.

## Kode Program

```python
import json

path = r"C:\Users\ASUS TUF GK\Music\BELAJAR CODING\studi_kasus6\nilaimahasiswa.json"

with open(path, "r", encoding="utf-8") as f:
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

    return "Data tersimpan ke nilaimahasiswa.json!"

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

    elif pilihan == "3":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak tersedia!")
```

## Output

### Menampilkan semua data

<img width="800" alt="Output menampilkan semua data" src="https://github.com/user-attachments/assets/e054143f-87bc-460c-90c6-f6a7ae064cc8" />

### Menambahkan data

<img width="466" alt="Output menambahkan data" src="https://github.com/user-attachments/assets/17b0ee88-51d9-4532-a851-db83a69093e7" />

### Keluar dari program (menu 3)

<img width="467" alt="Output keluar dari program" src="https://github.com/user-attachments/assets/acb1dd42-41c6-414c-842c-272db0161e5c" />
