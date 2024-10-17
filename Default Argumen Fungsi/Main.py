'''Default Argument'''

# def fungsi(argumen):
# def fungsi(argument = nilai defaultnya):

def say_hello(nama = "Kamu"):
    '''fungsi dengan default argument'''
    print(f"Hallo {nama}")

say_hello("Gantenggg")
say_hello()

def sapa_dia(nama, pesan = "Apa Kabss??"):
    '''Fungsi dengan satu input biasa dan satu default biasa'''
    print(f"hai {nama}, {pesan}")

sapa_dia("Gimnas","Hai Gantengggs")
sapa_dia("Hintu")

# contoh 3

def hitung_pangkat(angka, pangkat):
    hasil = angka**pangkat
    return hasil

print(hitung_pangkat(3,2))

hasil = hitung_pangkat(pangkat=2, angka=4)
print(hasil)

# contoh 4

def fungsi(input1=1,input2=2,input3=3,input4=4):
    hasil = input1 + input2 + input3 + input4
    return hasil

print(fungsi())
print(fungsi(input3=10))