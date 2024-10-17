# operator dalam bentuk method

## merubah case dari string

# merubah semua ke upper case

salam = "bro!"
print("normal = " + salam)
salam = salam.upper()
print("upper = " + salam)

# merubah semua ke lower case
alay = "aKu KecE AbiesSZSSss"
print("normal = " + alay)
alay = alay.lower()
print("lower = " + alay)

## pengecekan dengan is method

# contoh untuk pengecekan lower case
salam = "sist"
apakah_lower = salam.islower() # hasilnya bool
print(salam + " is lower = " + str(apakah_lower))
apakah_upper = salam.isupper() # hasilnya bool
print(salam + " is upper = " + str(apakah_upper))

# isalpha() <-- untuk mengecek semuanya huruf
# isalnum() <-- huruf dan angka
# isdecimal() <-- angka saja
# issapace() <-- spasi, tab, newline \n
# istitle() <-- semua kata dimulai dengan huruf besar

judul = "It Is Okay Not To Be Orkay"
cek_judul = judul.istitle() # hasil bool
print(judul + " is title = " + str(cek_judul))

## ngecek komponen startswith() endswith() <-- keren
cek_start = "Sangjangnim Oppa".startswith("Sangjangnim")
print("start = " + str(cek_start))

cek_end = "Sangjangnim Oppak".endswith("Oppak")
print("end = " + str(cek_end))

## penggabungan komponan join() split()
pisah = ['aku','sayang','kamu']
gabung = ','.join(pisah)
print(pisah)

gabung = ' '.join(pisah)
print(gabung)

gabung = ' ehem '.join(pisah)
print(gabung)

gabung = "akuehemsayangehemkamu"
print(gabung.split('ehem'))

## alokasi karakter rjust(), ljust(), center()

kanan = "kanan".rjust(10)
print("'"+kanan+"'")

kiri = "kiri".ljust(10)
print("'"+kiri+"'")

tengah = "tengah".center(20,"-")
print("'"+tengah+"'")

# kebalikannya -> strip()
tengah = "tengah".strip(":") 
print("'"+tengah+"'")

## metode lain

# 1. Capitalize() <- Membuat karakter pertama di string menjadi upper
tes_capitalize = "ayam goreng enak"
cek_hasil = tes_capitalize.capitalize()
print(cek_hasil)

tes_capitalize = "AYAM GORENG ENAK"
cek_hasil = tes_capitalize.capitalize()
print(cek_hasil)

# 2. Casefold() <-- sama dengan lower()
# bedanya, casefold() mengkonversi karakter tidak umum menjadi lowercase karakter umum
# Contoh  : 'ß' (german) = menjadi 'ss'
tes_casefold = "außen IS AN GERMAN WORD"
cek_hasil = tes_casefold.casefold()
print(cek_hasil)

# 3. Swapcase() <-- Uppercase jadi lowercase dan kebalikannya
tes_swapcase = "Ayam Goreng Suharti"
cek_hasil = tes_swapcase.swapcase()
print(cek_hasil)

# 4. Expandtabs () <-- Mengatur lebar tab (\t)
tes_expandtabs = "Ayam\tGoreng\tSuharti"
cek_hasil = tes_expandtabs.expandtabs(10)
print(cek_hasil)