print("-" * 20)
print("GoKontak".center(19))
print("-" * 20)

kontak = []
nomor_kontak = set()

while True:
    print("1. Tambah kontak")
    print("2. Daftar kontak")
    print("3. Cari kontak")
    print("4. Hapus kontak")
    print("5. Keluar")

    pilihan = input("Pilih menu: ")
    print("-" * 30)

    if pilihan == "1":
        print("Tambah Kontak")
        nama = input("Nama: ")
        nomor = input("Nomor: ")

        if nomor not in nomor_kontak:
            kontak.append([nama, nomor])
            nomor_kontak.add(nomor)
            print(f"{nama} berhasil disimpan")
            print("-" * 30)
        else:
            print(f"{nomor} sudah terdaftar")
            print("-" * 30)
    elif pilihan == "2":
        print("Daftar kontak")
        if kontak:
            for i, data in enumerate(kontak, 1):
                print(f"{i}. {data[0]} - {data[1]}")
                print("-" * 30)
        else:
            print("Belum ada kontak")
            print("-" * 30)

    elif pilihan == "3":
        print("Cari kontak")
        if kontak:
            keyword = input("Cari nama: ")
            ditemukan = False
            for data in kontak:
                if keyword.lower() in data[0].lower():
                    print(f"{data[0] - {data[1]}}")
                    ditemukan = True
                    print("-" * 30)
            if not ditemukan:
                print("Tidak ada kontak")
                print("-" * 30) 
        else:
            print("Belum ada kontak untuk dicari")
            print("-" * 30)
    elif pilihan == "4":
        print("Daftar kontak")
        if kontak:
            for i, data in enumerate(kontak, 1):
                print(f"{i}. {data[0]} - {data[1]}")
            try:
                hapus = int(input("Pilih nomor kontak yang akan dihapus: ")) - 1
                if 0 <= hapus <= len(kontak):
                    kontak_hapus = kontak[hapus]
                    nomor_kontak.remove(kontak_hapus[1])
                    kontak.pop(hapus)
                    print(f"Kontak {kontak_hapus[0]} berhasil dihapus")
                else:
                    print(f"Nomor kontak tidak valid")
            except ValueError:
                print("Masukan angka yang valid!")
    else:
        print("✗ Pilihan tidak valid! Silakan pilih 1-5.")