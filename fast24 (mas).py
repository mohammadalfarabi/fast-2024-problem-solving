print('''Sistem Manajemen Gudang
1. Tambah Barang
2. Tampilkan Barang
3. Cari Barang
4. Distribusi Barang
0. Keluar''')

max =250

gudang = [{'nama': None, 'jumlah': 0} for _ in range(max)]

def cariib(nama):
    for i, barang in enumerate(gudang):
        if barang['nama'] == nama:
            return i
    return -1

def hitungtstok():
    total = 0
    for barang in gudang:
        if barang['nama'] is not None:
            total += barang['jumlah']
    return total

def nambah(nama, jumlah):
    tstoksekarang = hitungtstok()
    if tstoksekarang + jumlah > max:
        print(f"Gagal menambahkan barang. Total stok akan melebihi kapasitas maksimum ({max}).")
        return

    indeks = cariib(nama)
    if indeks != -1:
        gudang[indeks]['jumlah'] += jumlah
    else:
        for i in range(max):
            if gudang[i]['nama'] is None:
                gudang[i] = {'nama': nama, 'jumlah': jumlah}
                return
        print("Gudang sudah penuh. Tidak bisa menambahkan barang baru.")

def tampilkan():
    print("\nDaftar semua barang di gudang:")
    for barang in gudang:
        if barang['nama'] is not None and barang['jumlah'] > 0:
            print(f"Nama: {barang['nama']}, Jumlah: {barang['jumlah']}")


def tampilkanterbanyak():
    bterbanyak = None
    sterbanyak = -1  

    for barang in gudang:
        if barang['nama'] is not None and barang['jumlah'] > 0 and barang['jumlah'] > sterbanyak:
            bterbanyak = barang
            sterbanyak = barang['jumlah']

    if bterbanyak:
        print(f"\nBarang dengan stok terbanyak: Nama: {bterbanyak['nama']}, Jumlah: {bterbanyak['jumlah']}")
    else:
        print("\nGudang kosong. Tidak ada barang dengan stok.")

def tampilkantersedikit():
    barang_tersedikit = None
    stok_tersedikit = float('')

    for barang in gudang:
        if barang['nama'] is not None and barang['jumlah'] > 0 and barang['jumlah'] < stok_tersedikit:
            barang_tersedikit = barang
            stok_tersedikit = barang['jumlah']

    if barang_tersedikit:
        print(f"\nBarang dengan stok tersedikit: Nama: {barang_tersedikit['nama']}, Jumlah: {barang_tersedikit['jumlah']}")
    else:
        print("\nGudang kosong. Tidak ada barang dengan stok.")

def carib(nama):
    indeks = cariib(nama)
    if indeks != -1:
        barang = gudang[indeks]
        print(f"Barang ditemukan - Nama: {barang['nama']}, Jumlah: {barang['jumlah']}")
        return barang
    print("Barang tidak ditemukan.")
    return None

def hapus(nama):
    indeks = cariib(nama)
    if indeks != -1:
        if gudang[indeks]['jumlah'] > 0:
            gudang[indeks]['jumlah'] = 0
        else:
            gudang[indeks] = {'nama': None, 'jumlah': 0}
        print(f"Barang '{nama}' berhasil dihapus.")
    else:
        print("Barang tidak ditemukan.")

def distribusi(nama, jumlah):
    indeks = cariib(nama)
    if indeks != -1:
        if gudang[indeks]['jumlah'] >= jumlah:
            gudang[indeks]['jumlah'] -= jumlah
            print(f"Mendistribusikan {jumlah} dari '{nama}'. Sisa stok: {gudang[indeks]['jumlah']}")
        else:
            print(f"Stok tidak mencukupi untuk '{nama}'. Jumlah yang tersedia: {gudang[indeks]['jumlah']}")
    else:
        print("Barang tidak ditemukan.")


while True:
    menu = input("\nPilih menu (1/2/3/4/0): ")

    if menu == '1':
        nama = input("Masukkan nama barang: ")
        jumlah = int(input("Masukkan jumlah barang: "))
        nambah(nama, jumlah)

    elif menu == '2':
        print("\nMenu Tampilkan Barang")
        print("1. Tampilkan Semua Barang")
        print("2. Barang dengan Stok Terbanyak")
        print("3. Barang dengan Stok Tersedikit")

        pilihlgi = input("Pilih opsi: ")

        if pilihlgi == '1':
            tampilkan()
        elif pilihlgi == '2':
            tampilkanterbanyak()
        elif pilihlgi == '3':
            tampilkantersedikit()
        else:
            print("Pilihan tidak valid. Kembali ke menu utama.")

    elif menu == '3':
        nama = input("Masukkan nama barang yang ingin dicari: ")
        carib(nama)
        menghapus = input('Mau menghapus barang? (y/n): ')
        if menghapus == 'y':
            hapus(nama)

    elif menu == '4':
        nama = input("Masukkan nama barang yang ingin didistribusikan: ")
        jumlah = int(input("Masukkan jumlah yang ingin didistribusikan: "))
        distribusi(nama, jumlah)

    elif menu == '0':
        print("Keluar dari program.")
        break

    else:
        print("menu tidak valid. Silakan coba lagi.")
