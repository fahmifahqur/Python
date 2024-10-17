## Operasi

# index  0(-3)  1(-2)  2(-1)
data = ["Ucup","Otong","Rere"]

# mengambil data dari list ini
data_0 = data[0]
print(f"data pertama (index 0) = {data_0}")

data_terakhir = data[-1]
print(f"data terakhir adalah = {data_terakhir}")

data_ucup = data[-3]
print(f"data ucup = {data_ucup}")

# mengambil info jumlah data dalam list
panjang_data = len(data)
print(f"panjang data = {panjang_data}")

## Manipulasi data list

# Menambahkan item pada list sesuai posisi
print(f"data sebelum ditambah = \n{data}")

data.insert(1,"Acep")
print(f"data sesudah ditambah = \n{data}")

# menambah diakhir list
data.append("Jeje")
print(f"data ditambah lagi = \n{data}")

# menambahlan list dengan list
data_baru = ["Madang","Koci","Dudung"]
data.extend(data_baru)
print(f"data gabungan = \n{data}")

# merubah data
# kita ubah data 2 menjadi mikel
data[2] = "Mikel"
print(f"data rubah = \n{data}")

# meremove data

data.remove("Jeje")
print(f"data remove = \n{data}") # meremove data harus sesuai dengan data yang ada

# meremove data paling belakang
data.pop()
print(f"data_akhir = {data}")

# melihat data yang sudah hilang
data_akhir = data.pop()
print(f"data_akhir = {data}")

print(data_akhir)
