data_angka = [1,4,1,5,3,1,2,4,5,6,2,4]

print(f"data angka = \n{data_angka}")

# count data

jumlah_data_4 = data_angka.count(4)
jumlah_data_3 = data_angka.count(3)

print(f"jumlah angka 4 = {jumlah_data_4}")
print(f"jumlah angka 3 = {jumlah_data_3}")

# ambil posisi data (index)

data = ["Ucup","Rere","Acep","Madang"]

print(f"data = {data}")

index_rere = data.index("Rere")
index_acep = data.index("Acep")

print(f"index si Rere = {index_rere}")
print(f"index si Acep = {index_acep}")

# mengurutkan list
print(f"data angka sebelum sort = \n{data_angka}")
data_angka.sort()
print(f"data angka sort = \n{data_angka}")

print(f"data = {data}")
data.sort()
print(f"data sort = {data}")

# balik listnya
data_angka.reverse()
data.reverse()
print(f"data di reverse = \n{data_angka} \n{data}")