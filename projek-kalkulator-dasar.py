# PROJEK KALKULATOR SEDERHANA MENGGUNAKAN PYTHON

# inputan user
angka1 = int(input("Masukan Angka pertama yang ingin di hitung = "))
operator = input("Masukan Operator untuk menghitung (+,-,*,/ ) = ")
angka2 = int(input("Masukan Angka Kedua yang ingin di hitung = "))

# operasi nya
# jika operasi tambah
if operator == "+":
    hasil = angka1 + angka2
    print(f"Hasilnya adalah = {hasil}")
elif operator == "-":
    hasil = angka1 - angka2
    print(f"Hasilnya adalah = {hasil}")
elif operator == "*":
    hasil = angka1 * angka2
    print(f"Hasilnya adalah = {hasil}")
elif operator == "/":
    hasil = angka1 / angka2
    print(f"Hasilnya adalah = {hasil}")
else:
    print("Masukan data yang benar dong!!")
