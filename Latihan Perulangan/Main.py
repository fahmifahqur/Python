# Latihan perulangan membuat segitiga

sisi = 10

# 1. Menggunakan for

# dummy variable
print("awal dari for")
count = 1
for i in range(sisi):
    print("*"*count)
    count += 1

print("akhir dari for")
# 2. Menggunakan while

print("awal while")
count = 1
while True:
    print("*"*count)
    count += 1

    if count > sisi:
        break

print("akhir while")

# 3. hanya ganjil

print("awal while")
count = 1
while True:
    if (count%2):
        # print jika ganjil
        print("*"*count)
        count += 1
    else:
    # akan kembali ke atas jika ganjil
        count += 1
        continue

# akan break jika count melebihi sisi
    if count > sisi:
        break

print("akhir while")

# 3. hanya ganjil saja

print("awal while")
count = 1
spasi = int(sisi/2)
while True:
    if (count%2):
        # print jika ganjil
        print(" "*spasi,"+"*count)
        spasi -= 1
        count += 1
    else:
    # akan kembali ke atas jika ganjil
        count += 1
        continue

# akan break jika count melebihi sisi
    if count > sisi:
        break

print("akhir while\n")

print("ini ketupat\n")
count = 1
spasi = int(sisi/2)
while True:
    if (count%2):
        print(" "*spasi,"+"*count)
        spasi -= 1
        count += 1
    else:
        count += 1
        continue
    if count > sisi:
        break
while True:
    if (count%2): 
        spasi += 1
        print(" "*spasi,"+"*count)
        count -= 1
    else:
        count -= 1
    if count == 0:
        break






























