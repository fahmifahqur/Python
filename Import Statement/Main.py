#  import

# fungsinya adalah untuk mengambil program dari file external .py

# 1. untuk menyambung program dari external
import program_print
import program_dadang

#  2. import data dengan 
import variabel
import pucui

# data ada di namespace variabel
print(variabel.data)
print(pucui.data)

# 3. import dengan fungsi
import matematika

hasil = matematika.tambah(3,4)
print(hasil)