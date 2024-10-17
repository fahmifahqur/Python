# 1. Mode write, dia akan membuat file baru jika tidak ada, lalu akan menimpa atau overwrite isinya

with open("data_1.txt",'w',encoding="utf-8") as file:
    file.write("Coba duluu")

with open("data_1.txt",'w',encoding="utf-8") as file:
    file.write("Coba ygy")

# 2. Mode append

with open("data_2.txt",'w',encoding="utf-8") as file:
    file.write("Coba duluu\n")

with open("data_2.txt",'a',encoding="utf-8") as file:
    file.write("Coba gann\n")

with open("data_2.txt",'a',encoding="utf-8") as file:
    file.write("Coba tapi ditambah")

# 3. Mode r+

with open("data_3.txt",'w',encoding="utf-8") as file:
    file.write("data ke 3\n")

with open("data_3.txt",'r+',encoding="utf-8") as file:
    file.write("baris-1 \n")
    file.write("baris-2 \n")
    file.write("baris-3 \n")

with open("data_3.txt",'r+',encoding="utf-8") as file:
    data = file.read()
    print(data)

with open("data_3.txt",'r+',encoding="utf-8") as file:
    file.write("Dudung") # menimpa isi text sesuai dengan panjang data