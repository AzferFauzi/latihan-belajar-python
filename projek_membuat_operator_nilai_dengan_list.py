# Projek latihan

# Nilai sekolah

nilai = []

while True:
    print('\n========== Nilai Sekolah =========')
    print('Pilih menu yang anda pilih :')
    print('a | Menambah nilai')
    print('b | Melihat nilai')
    print('c | Menghitung rata rata nilai')
    print('d | Selesai')
    inputuser = input('Menu yang anda pilih = ')
    inputuser = inputuser.lower()

    if inputuser == "a":
        input_a = int(input('\na | Masukan Nilai yang ingin di tambah (0-100) = '))
        if 0 <= input_a <= 100:
            nilai.append(input_a)
        else:
            print(f'\nNilai {input_a} tidak dapat di proses')
    elif inputuser == "b":
        if nilai != []:
            print(f'\nKumpulan nilai saat ini = \n{nilai}')
        else:
            print('\nNilai masih kosong, mohon masukan nilai terlebih dahulu setidaknya 1')
    elif inputuser == "c":
        if nilai != []:
            x = sum(nilai)/len(nilai)
            print(f'\nRata - rata nilai adalah = {x}')
        else:
            print('\nNilai masih kosong, mohon masukan nilai terlebih dahulu setidaknya 1')      
    elif inputuser == "d":
        print("Terima kasih sudah menggunakan operator ini")
        break
    else:
        print("Eror, Mohon pilih menu yang tersedia")
