# LATIHAN OPERASI KOMPERASI DAN LOGIKA
# membuat nilai variable yang sesuai

# SOAL 1 
# ++++(-15)---(-12)+++++(-9)---(-5)+++++(-2)---1++++++4---6+++++9---11++++++
print("\n++++(-15)---(-12)+++++(-9)---(-5)+++++(-2)---1++++++4---6+++++9---11++++++")
while True:
    data = int(input("Masukan angka untuk mengetahui nilai yang di atas = "))
    if (-15 <= data <= -12) or (-9 <= data <= -5) or (-2 <= data <= 1) or (4 <= data <= 6) or (9 <= data <= 11):
        print(f"Nilai {data} = Negatif")
    else:
        print(f"Nilai {data} = Positif")
