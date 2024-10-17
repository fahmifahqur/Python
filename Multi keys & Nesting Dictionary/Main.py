import datetime

mahasiswa1 = {
    'nama':'cing acing',
    'nim':'21335008',
    'sks_lulus':144,
    'beasiswa':False,
    'lahir':datetime.datetime(2003,5,13)
}

mahasiswa2 = {
    'nama':'dung dudung',
    'nim':'21335010',
    'sks_lulus':144,
    'beasiswa':False,
    'lahir':datetime.datetime(2001,3,6)
}

mahasiswa3 = {
    'nama':'ting ayu ting',
    'nim':'21335012',
    'sks_lulus':144,
    'beasiswa':True,
    'lahir':datetime.datetime(2002,8,22)
}

data_mahasiswa = {
    'MAH001':mahasiswa1,
    'MAH002':mahasiswa2,
    'MAH003':mahasiswa3
}

print(f"{'KEY':<6} {'Nama':<17} {'SKS':<3} {'Beasiswa':<9} {'Lahir':<10}")
print("-"*50)

for mahasiswa in data_mahasiswa:
    KEY = mahasiswa

    NAMA = data_mahasiswa[KEY]['nama']
    NIM = data_mahasiswa[KEY]['nim']
    SKS = data_mahasiswa[KEY]['sks_lulus']
    BEASISWA = data_mahasiswa[KEY]['beasiswa']
    LAHIR = data_mahasiswa[KEY]['lahir'].strftime('%x')

    print(f"{KEY:<6} {NAMA:<17} {SKS:<3} {BEASISWA:^9} {LAHIR:<10}")
