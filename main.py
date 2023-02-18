# Membuka file phonebook.txt dan membaca kontak yang sudah tersimpan di dalamnya
phone_book = {} #membuat dan menginisialisasi variable phone_book sebagai kamus kosong
with open("phonebook.txt", "r") as f: #membuka file phonebook.txt dalam mode baca ("r" atau "read")
    for line in f:
        nama, nomor = line.strip().split(",") #format kontak adalah nama,nomor dipisahkan oleh ","
        phone_book[nama] = nomor #menambahkan kontak baru ke dalam kamus phone_book

# Fungsi untuk menambahkan kontak baru
def tambahKontak(nama, nomor):
    phone_book[nama] = nomor #menambahkan kontak baru ke dalam kamus phone_book
    with open("phonebook.txt", "a") as f: #membuka file phonebook.txt dalam mode tambah ("a" atau "append")
        f.write(f"{nama},{nomor}\n") #menambahkan kontak baru ke dalam file phonebook.txt dengan mode "append"
    print("Kontak berhasil ditambahkan")

# Fungsi untuk mencari kontak berdasarkan nama
def cariKontak(nama):
    if nama in phone_book:
        print(f"{nama}: {phone_book[nama]}")
    else:
        print("Kontak tidak ditemukan")

# Fungsi untuk menampilkan semua kontak
def tampilkanSemuaKontak():
    if phone_book:
        for nama, nomor in phone_book.items():
            print(f"{nama}: {nomor}")
    else:
        print("Tidak ada kontak yang tersimpan")

# Fungsi untuk menghapus kontak
def hapusKontak(nama):
    if nama in phone_book:
        del phone_book[nama]
        with open("phonebook.txt", "w") as f:
            for nama, nomor in phone_book.items():
                f.write(f"{nama},{nomor}\n")
        print(f"Kontak {nama} berhasil dihapus")
    else:
        print("Kontak tidak ditemukan")

# Looping program
while True:
    print("\n===== Phone Book App =====")
    print("1. Tambah Kontak")
    print("2. Cari Kontak")
    print("3. Tampilkan Semua Kontak")
    print("4. Hapus Kontak")
    print("5. Keluar")
    choice = input("Pilih menu (1/2/3/4/5): ")

    if choice == "1":
        nama = input("Masukkan nama kontak: ")
        nomor = input("Masukkan nomor telepon: ")
        tambahKontak(nama, nomor)
    elif choice == "2":
        nama = input("Masukkan nama kontak yang ingin dicari: ")
        cariKontak(nama)
    elif choice == "3":
        tampilkanSemuaKontak()
    elif choice == "4":
        nama = input("Masukkan nama kontak yang ingin dihapus: ")
        hapusKontak(nama)
    elif choice == "5":
        print("Terima kasih telah menggunakan Phone Book App")
        break
    else:
        print("Menu yang dipilih tidak tersedia")