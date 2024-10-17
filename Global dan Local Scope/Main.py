## Global dan Local Scope

nama_global = "dado" # <-- ini variabel global

# akses variabel global dalam fungsi
def fungsi1():
    print(f"fungsi menampilkan {nama_global}")

fungsi1()

# akses variabel global dalam loop
for i in range(0,3):
    print(f"loop {i} - {nama_global}")

# percabangan
if True:
    print(f"if menampilkan {nama_global}")


## Variabel Local Scope
def fungsi2():
    nama_local = "deril" # <-- variabel local scope

fungsi2()
# print(nama_local) # tidak bisa dilakukan

## Contoh 1: penggunaan akses variabel
def say_dung():
    print(f"Hello {nama}")

nama = "ding"
say_dung()

## Contoh 2: merubah variabel global
angka = 0
name = "dang"

def ubah_angka(nilai_baru, nama_baru):
    global angka #fungsi ini mendapat akses merubah
    global name
    angka=nilai_baru
    name = nama_baru

print(f"sebelum {angka,name}")
ubah_angka(10,"deng")
print(f"sesudah {angka,name}")

## Contoh 3:
angka = 0

for i in range(0,5):
    angka += i
    angka_dummy = 0

print(angka)
print(angka_dummy)
    
if True:
    angka = 10
    angka_dummy = 10


print(angka)
print(angka_dummy)