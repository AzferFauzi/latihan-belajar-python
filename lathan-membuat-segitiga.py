# Membuat berbagai Bentuk segitiga di python

# Menggunakan for in
sisi = 5
count = 1

for i in range(sisi):
    print("*" * count)
    count += 1

print('\n')

for i in range(sisi):
    print("*" * sisi)
    sisi -= 1



# menggunakan while
sisi = 5
count = 1
spasi = 5

while True:
    print(" " * spasi + "*" * count)
    spasi -= 1
    count += 1

    if sisi < count:
        break
print('\n')

sisi = 5
count = 1
spasi = 5

while True:
    print(" " * spasi + "*" * sisi)
    spasi += 1
    sisi -= 1

    if sisi < count:
        break

# segitiga sama sisi
sisi = 11
spasi = 1
count = 1

while True:
    if (count % 2) == 0:
        count += 1
        continue
    
    print("*" * count)
    count += 1

    if count > sisi:
        break
print('\n')

# Segitiga sama sisi terbalik
sisi = 11
spasi = 1
count = 11

while True:
    if (count % 2) == 0:
        count -= 1
        continue
    
    print(" " * spasi + "*" * count)
    count -= 1
    spasi += 1

    if count > sisi:
        break

