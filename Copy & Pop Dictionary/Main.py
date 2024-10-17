#  copy dictionary

teman_teman = {
    "cup":"ucup tina",
    "ting":"ayu ting-ting",
    "dang":"dadang narma",
    "man":"maman yatni"
}

friends = teman_teman.copy()

print(f"teman-teman: {teman_teman}\n")
print(f"friends: {friends}\n")

teman_teman["cup"]="ucup keren"
print(f"teman-teman: {teman_teman}\n")
print(f"friends: {friends}\n")

# pop dictionary
dataAyu = friends.pop("ting")
print(f"data ayu = {dataAyu}\n")
print(f"friends = {friends}\n")

# popitem dictionary (data terakhir saja)
dataTerakhir = friends.popitem()
print(f"data terakhir = {dataTerakhir}\n")
print(f"friends = {friends}\n")