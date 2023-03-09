katakunci = 6
maksimal = 3
tebakan = 0 

while tebakan <= maksimal:
    inputuser = int(input("masukan angka setan :"))
    tebakan += 1

    if inputuser == katakunci :
        print("Mantap betul")
        break
else:
    print("Sudah 3x, silahkan kembali input")