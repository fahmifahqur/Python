# latihan konversi satuan temperature

# program konversi celcius ke satuan lain

print("PROGRAM KONVERSI TEMPERATURE\n")

celcius = float(input('Masukan suhu dalam celcius : '))
print("Suhu adalah",celcius, "Celcius")


# reamur
reamur = (4/5) * celcius
print("Suhu dalam Reamur adalah",reamur, "Reamur")


# fahrenheit
fahrenheit = ((9/5) * celcius) + 32
print("Suhu dalam Fahrenheit adalah",fahrenheit, "Fahrenheit")

# kelvin
kelvin = celcius + 273
print("Suhu dalam Kelvin adalah",kelvin, "Kelvin")

# pr
fahrenheit = float(input('Masukkan Suhu dalam Fahrenheit: '))
celcius = ((5/9) * fahrenheit) - 32
kelvin = celcius + 273
print("Suhu dalam Kelvin:", kelvin)

kelvin = float(input('Masukkan suhu dalam kelvin: '))
celcius = kelvin - 273
fahrenheit = ((9/5) * celcius) + 32
print("Suhu dalam Fahrenheit:", fahrenheit)
