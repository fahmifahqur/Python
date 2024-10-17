data = "ini adalah data"
print(data)
print(type(data))

# 1. cara membuat string

'''
    1. dengan menggunakan single quote '...'
    2. dengan menggunakan double quote "..."
'''

data = 'Menggunakan single quote'
print(data)

data = "Menggunakan double quote"
print(data)

print('"Halo, apa kabar?"')
print("'Halo, apa kabar?'")
print("ini adalah hari Jum'at")

# 2. Menggunakan tanda \

# membuat tanda ' menjadi string
print('mari sholat Jum\'at')
print('g\'day, isn\'t it?')

# backlash
print("C:\\user\\Ucup")

# tab
print("ucup\totong, jauhan")

# backspace
print("ucup \botong, menjadi dekat")

# newline
print("baris pertama.\nbaris kedua.") # LF -> Line Feed -> unix, macOS, linux
print("baris pertama.\rbaris kedua.") # CR -> Carriage Return -> commodore, acorn, lisp
print("baris pertama.\r\nbaris kedua.") # CRLF -> Line Feed Carriage Return -> dipakai oleh windows

# 3. String Literal atau RAW

# hati-hati
print('C:\new folder') # akan salah pathnya

# menggunakan RAW string
print(r'C:\new folder')

# multiline literal string
print("""
Nama : Fahmi
Kelas : SMA
""")

# multiline literal string dan RAW
print(r"""
Nama : Fahmi
Kelas : SMA\new normal
Website : www.fahmi.com/newID
""")