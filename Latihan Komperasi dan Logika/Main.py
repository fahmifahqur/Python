# latihan logika dan komparasi

# membuat gabungan area rentang dari angka

#+++++++3--------10++++++++

inputUser = float(input("masukan angka yang bernilai\nkurang dari 3 \natau \nlebih besar dari 10\n:"))

# +++++3---------------
# Memeriksa angka kurang dari 3
isKurangDari = (inputUser < 3)
print("Kurang dari 3 =", isKurangDari)

# -----------10
# Memeriksa angka lebih dari 10
isLebihDari = (inputUser > 10)
print("Lebih dari 10 =", isLebihDari)

#+++++++3--------10++++++++

isCorrect = isKurangDari or isLebihDari
print("Angka yang anda masukan: ", isCorrect)


# ----3++++10-----
# kasus irisan
print("\n",10*"=","\n")
inputUser = float(input("masukan angka yang bernilai\nlebih dari 3 \ndan \nkurang dari 10\n:"))

# ----3+++++++
# lebih dari 3
isLebihDari = inputUser > 3
print("Lebih dari 3 =",isLebihDari)

# ++++10------
# kurang dari 10
isKurangDari = inputUser < 10
print("Kurang dari 10 =",isKurangDari)

# ----3++++10-----
isCorrect = isKurangDari and isLebihDari
print("Angka yang anda masukan: ", isCorrect)

# pr
print("GABUNGAN")
InputData = float(input("Masukkan Data : "))

Angka1 = (InputData >= 0 and InputData <= 5)
print(Angka1)

Angka2 = (InputData >= 8 and InputData <= 11)
print(Angka2)

Hasilnya = Angka1 or Angka2
print("Answer :",Hasilnya)

print("IRISAN")
InputData = float(input("Masukkan Data : "))

Angka1 = (InputData <= 0 or InputData >= 5)
print(Angka1)

Angka2 = (InputData <= 8 or InputData >= 11)
print(Angka2)

Hasilnya = Angka1 and Angka2
print("Answer :",Hasilnya)
