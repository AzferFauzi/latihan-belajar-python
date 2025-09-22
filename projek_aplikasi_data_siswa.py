DataSiswa = {}
while True:
    print('\n======== Aplikasi Data Siswa =========\n')
    print('Menu :')
    print('a. Lihat Data')
    print('b. Update Data Siswa')
    print('c. Cari Data Siswa Berdasarkan Nama')
    print('d. Hapus Siswa')
    print('e. Sudahi Pemasukan Data')
    InputUser = input("Menu yang anda pilih = ")
    InputUser = InputUser.lower()

    # a
    if InputUser == "a":
        if DataSiswa != {}:
            print(f'\n{'Nama':<10} {"kelas":<10} {"Umur":<10}')
            print('================================')
            for data in DataSiswa:
                Nama = data
                Kelas = DataSiswa[Nama]['kelas']
                Umur = DataSiswa[Nama]['umur']
                print(f'{Nama:<10} {Kelas:<10} {Umur:<10}')
        else:
            print('\naMaaf data masih kosong, silahkan isi data terlebih dahulu')
            print(f'{'Nama':<10} {"kelas":<10} {"Umur":<10}')
            print('================================')
    # b
    elif InputUser == "b":
        nama = input("\nMasukan nama = ")
        kelas = (input("Masukan kelas = ")) 
        umur = int(input("Masukan umur = "))

        DataSiswa[nama] = {
            "kelas": kelas,
            "umur": umur
            }
    # c. Menacri data berdasarkan nama
    elif InputUser == "c":
        InputNama = input("Nama yang ingin anda cari = ")
        if InputNama in DataSiswa:
            print(f'\nNama "{InputNama}" tersedia di dalam data siswa')
            print(DataSiswa[InputNama])
        else:
            print('\nNama tidak tersedia di dalam data siswa')
    # d. Hapus data
    elif InputUser == "d":
        if DataSiswa != {}:
            InputHapus = input("\nData nama yang ingin di hapus = ")
            if InputHapus in DataSiswa:
                print(f'\nData "{InputHapus}" berhasil di hapus')
                del DataSiswa[InputHapus]
            else:
                print('\nNama tidak tersedia di data siswa')
        else:
            print('\nData masih kosong, jadi tidak bisa menghapus')

    # e. Sudahi data
    elif InputUser == "e":
        print('\nTerima kasih sudah mengisi data di aplikasi ini.')
        break
    else:
        print('\nMasukan pilihan menu yang sesuai')
