''' Fungsi dengan kembalian'''

# template fungsi dengan kembalian
# def nama_fungsi(argument):
#   badan funsgi
#   return output

# fungis kuadrat

def kuadrat(input_angka):
    '''Fungsi Kuadrat'''
    output_kuadrat = input_angka**2
    return output_kuadrat

y = kuadrat(3)
print(y)

print(kuadrat(6))

z = 10 + kuadrat(7)
print(z)

# fungsi tambah

def fungsi_tambah(angka_1,angka_2):
    '''Fungsi return dengan multi input'''
    return angka_1 + angka_2

a = fungsi_tambah(10,9)
print(a)

# fungsi dengan return banyak

def operasi_matematika(angka_1,angka_2):
    tambah = angka_1 + angka_2
    kurang = angka_1 - angka_2
    kali = angka_2 * angka_1
    bagi = angka_2 / angka_1

    return tambah,kurang,kali,bagi

k,l,m,n = operasi_matematika(9,5)

print(f"Hasil tambah = {k}")
print(f"Hasil kurang = {l}")
print(f"Hasil kali = {m}")
print(f"Hasil bagi = {n}")