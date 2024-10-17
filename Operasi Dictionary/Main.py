# operator dictionary

data_dict = {
    "cup":"ucup pastu",
    "dang":"dadang suherman",
    "ting":"ayu ting-ting"
}

# panjang dictionary
LENDICT = len(data_dict)
print(f"panjang dictionary: {LENDICT}")

# mengecek key exist atau tidak
KEY = "cup"
CHECKKEY = KEY in data_dict
print(f"apakah {KEY} ada di data_dict: {CHECKKEY}")

# mengakses value (read) dengan get
print(data_dict["cup"])
print(data_dict.get("cup"))
print(data_dict.get("tis","key tidak ditemukan")) # cek key dengan message tidak ditemukan

# mengupdate data
data_dict["cup"] = "ucup ganteng"
print(data_dict)
data_dict["sep"] = "asep proti"
print(data_dict)

data_dict.update({"cup":"ucup pastu"})
print(data_dict)
data_dict.update({"farhan":"gilaaks"}) # kalau tidak ada di add ajah
print(data_dict)

# mendelete data pada dictionary
del data_dict["farhan"]
print(data_dict)

