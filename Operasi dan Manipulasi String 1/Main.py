# operasi dan manipulasi string

# 1. menyambung string (concatenate)
nama_pertama = "Fahmi"
nama_tengah = "F"
nama_akhir = "Rozi"

nama_lengkap = nama_pertama + " " + nama_tengah + "'" + nama_akhir
print(nama_lengkap)

# 2. Menghitung panjang string
panjang = len(nama_lengkap)
print("panjang dari " + nama_lengkap + " = " + str(panjang))

# 3. Operator untuk string

# mengecek apakah ada komponen char atau string di string

f = "f"
status = f in nama_lengkap
print("string " + f + " ada di " + nama_lengkap + " = " + str(status))

F = "F"
status = F in nama_lengkap
print("string " + F + " ada di " + nama_lengkap + " = " + str(status))

f = "f"
status = f not in nama_lengkap
print("string " + f + " ada di " + nama_lengkap + " = " + str(status))

# mengulang string
print("wk"*15)
print(10*"wk")

# indexing
print("index ke-0 : " + nama_lengkap[0])
print("index ke-5 : " + nama_lengkap[5])
print("index ke-(-1): " + nama_lengkap[-1])
print("index ke-(-2): " + nama_lengkap[-2])
print("index ke-[0:3]:" + nama_lengkap[0:4])
print("index ke-[3:8]:" + nama_lengkap[3:9])
print("index ke-[0,2,4,6,8,10]:" + nama_lengkap[0:10:2])

# item paling kecil
print("paling kecil : " + min(nama_lengkap))
# item paling besar
print("paling kecil : " + max(nama_lengkap))

ascii_code = ord(" ")
print("ASCII code untuk spasi adalah " + str(ascii_code))
data = 117
print("char intuk ASCII adalah " + chr(data))

# 4. operator dalam bentuk methode

data = "otong surotong pararotong"
jumlah = data.count("o")
print("jumlah o pada " + data + " = " + str(jumlah))