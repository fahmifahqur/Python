'''Fungsi dengan argument (input)'''

#Template
# def nama_fungsi(argument):
#    Badan fungsi

def hello_world(nama):
    '''Fungsi Hellow World menerima input dengan variable nama'''
    print(f"Selamat datang {nama}")


hello_world("Nita")

# program tambah

def tambah(angka_1,angka_2):
    '''fungsi tambah'''
    hasil = angka_1 + angka_2
    print(f"{angka_1} + {angka_2} = {hasil}")

tambah(1,6)
tambah(239,12)

def say_hi(List_peserta):
    '''fungsi say hi'''
    data_peserta = List_peserta.copy()
    for peserta in data_peserta:
        print(f"YTTA {peserta}")

anggota_girlband = ["Nita","Gita","Ayu"]

say_hi(anggota_girlband)
