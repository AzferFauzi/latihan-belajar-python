# PROYEK DAFTAR BELANJA SEDERHANA

# List kosong
belanja = []
# Daftar buah
daftar_buah = ["Apel","Jeruk","Mangga","Pisang"]

# Operasinya
while True:
    print("========= Tokoh Buah Pak Somad ===========")
    print("MENU : ")
    print("|a. Tambah buah |b. Hapus buah |c. Beli |d. Batalkan Pembelian")
    menu = input("Menu apa yang kamu pilih = ")

    # JIKA INGIN TAMBAH BUAH
    if menu == "a":
        print("\nDaftar Belanja :")
        print("| Apel | Jeruk | Mangga | Pisang |")
        tmbh_barang = input("\nBuah apa yang ingin anda pilih? : ")
        tmbh_barang = tmbh_barang.title()

        if tmbh_barang in daftar_buah:
            print("Buah di Keranjang :")
            belanja.append(tmbh_barang)
            print(belanja,"\n")
        else:
            print("Maaf buah tidak ada didalam daftar\n")
    
    # JIKA INGIN APUS BARANG
    elif menu == "b":
        print("\nDaftar Belanja :")
        print("| Apel | Jeruk | Mangga | Pisang |")

        krng_barang = input("\nBuah apa yang ingin anda batalkan? : ")
        krng_barang = krng_barang.title()

        if belanja == []:
            print("Anda harus memilih buah terlebih dahulu\n")
        else:
            if krng_barang in belanja:
                print("Buah di Keranjang :")
                belanja.remove(krng_barang)
                print(belanja,"\n")
            else:
                print("Buah tidak ada di keranjang")
                print("Buah di Keranjang :")
                print(belanja,"\n")

    # JIKA INGIN MENYUDAHI BELANJA DENGAN BELI
    elif menu == "c":
        print("\nBuah yang anda beli :")
        print(belanja)
        print("\nTerima kasih telah membeli buah di Toko  Buah Pak Somad")
        print("Kami menunggu kedatangan anda kembali\n")
        break

    # JIKA INGIN MEMBATALKAN PEMBELIAN DENGAN TIDAK JADI MEMBELI
    elif menu == "d":
        print("Terima Kasih Telah datang ke Toko Buah Pak Somad")
        print("Kami menunggu kedatangan anda kembali\n")
        break

    else:
        print("\n")
            
        
