data_0 = [1,2]
data_1 = [3,4]

data_list_biasa = [1,2,3,4]

print(f"list biasa = {data_list_biasa}")

list_2D = [data_0,data_1,5,6]

print(f"list 2D = {list_2D}")

# contoh penggunaan

peserta_0 = ["cupi",24,"Laki-Laki"]
peserta_1 = ["itung",26,"Laki-Laki"]
peserta_2 = ["rere", 45,"Wanita"]

list_peserta = [peserta_0,peserta_1,peserta_2]

print(f"peserta = {list_peserta}")

for peserta in list_peserta:
    print(f"nama\t: {peserta[0]}")
    print(f"umur\t: {peserta[1]}")
    print(f"jenis kelamin\t: {peserta[2]}\n")


# dengan reference

list_copy = list_peserta.copy();
print(f"peserta = {list_copy}")
peserta_0[0] = "mikel"
print(f"peserta = {list_copy}")
print(f"peserta = {list_peserta}")