# Latihan Aritmatika 
print("\n====================")
print("OPERASI ARITMATIKA")
print("====================")

# CELCIUS
c = float(input("Berapa Suhu Celcius = "))
print(f"Suhu Celcius adalah = {c}")
# celcius ke reamur
r = (4/5) * c
print(f"Suhu Celcius ke Reamur adalah = {r}")
# celcius ke fahrenheit
f = ((9/5) * c) + 32
print(f"Suhu Celcius ke Fahrenheit adalah = {f}")
# celcius ke kelvin
k = c + 273
print(f"Suhu Celcius ke Kelvin adalah = {k}")

# REAMUR
r = float(input("Berapa Suhu Reamur = "))
print(f"Suhu Reamur adalah = {r}")
# reamur ke celcius
c = (5/4) * r
print(f"Suhu Reamur ke Celcius adalah = {c}")
# reamur ke fahrenheit
f = ((9/4) * r) + 32
print(f"Suhu Reamur ke Fahrenheit adalah = {f}")
# reamur ke kelvin
k = ((5/4) * r) + 273
print(f"Suhu Reamur ke Kelvin adalah = {k}")

# FEHRENHEIT
f = float(input("Berapa Suhu Fahrenheit = "))
print(f"Suhu Fahrenheit adalah = {f}")
# fahrenheit ke reamur
r = (4/9) * (f - 32)
print(f"Suhu Fahrenheit ke Reamur adalah = {r}")
# fahrenheit ke celcius
c = (5/9) * (f - 32)
print(f"Suhu Fahrenheit ke Celcius adalah = {c}")
# fahrenheit ke kelvin
k = (f - 32) * (5/9) + 273
print(f"Suhu Fahrenheit ke Kelvin adalah = {k}")

k = float(input("Berapa Suhu Kelvin = "))
print(f"Suhu Kelvin adalah = {k}")
# kelvin ke reamur
r = (4/5) * (k - 273)
print(f"Suhu Kelvin ke Reamur adalah = {r}")
# kelvin ke fahrenheit
f = (k - 273) * (9/5) - 32
print(f"Suhu Kelvin ke Fahrenheit adalah = {f}")
# kelvin ke celcius
c = k - 273
print(f"Suhu Kelvin ke Celcius adalah = {c}")
