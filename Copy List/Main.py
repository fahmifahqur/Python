## Teknik menduplikat List

a = ["Ucup","Dadang","Madang"]
print(f"a = {a}")

b = a
print(f"b = {b}")

# akan merubah member dari a

# ini akan merubah kedua list
a[1] = "Mikel"
b.sort()
print(f"a = {a}")
print(f"b = {b}")

# addres dari kedua list a dan b
print(f"addres a = {hex(id(a))}")
print(f"addres b = {hex(id(b))}")

# menduplikat list dengan copy

print("membuat list c dangan a.copy()")
c = a.copy()

print(f"addres a = {hex(id(a))}")
print(f"addres b = {hex(id(b))}")
print(f"addres c = {hex(id(c))}")

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")

print ("Kita ubah data 0")
c[0] = "Dadang"

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")

print ("Kita ubah data 1")
a[1] = "Otong"

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")