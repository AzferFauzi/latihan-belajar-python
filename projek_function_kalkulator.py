def header():
    print(f'{"KALKULATOR SEDERHANA":^40}')
    print(f'{"Tambah, Kali, Kurang, Dan Bagi":^40}')
    print(f"{'-'*40:^40}")

def input_user():
    angka_1 = int(input("Masukan angka pertama = "))
    angka_2 = int(input("Masukan angka kedua = "))

    return angka_1,angka_2
    
def kalkulator_tambah(angka_1,angka_2):
    return angka_1 + angka_2

def kalkulator_kurang(angka_1,angka_2):
    return angka_1 - angka_2

def kalkulator_kali(angka_1,angka_2):
    return angka_1 * angka_2

def kalkulator_bagi(angka_1,angka_2):
    return angka_1 / angka_2

while True:
    header()
    Angka1,Angka2 = input_user()
    Tambah = kalkulator_tambah(Angka1,Angka2)
    Kurang = kalkulator_kurang(Angka1,Angka2)
    Kali = kalkulator_kali(Angka1,Angka2)
    Bagi = kalkulator_bagi(Angka1,Angka2)

    print(f'{Angka1} + {Angka2} = {Tambah}')
    print(f'{Angka1} - {Angka2} = {Kurang}')
    print(f'{Angka1} * {Angka2} = {Kali}')
    print(f'{Angka1} / {Angka2} = {Bagi}\n')
