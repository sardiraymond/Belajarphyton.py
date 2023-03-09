# Definisi int on variabel input (masukan angka)

angka=int(input("masukan angka \n"))

if angka == 3:
    print("ganteng")
elif angka  >3 and angka < 5 :
    #print("kelebihan")
    if angka <5:
        print ("luarbiasa")
    else :
        print ("modyar")
elif angka <5 and angka <3 :
    print ("Lu pasti bingung")
else:
    print ("cape yak")    


    # alasan kenapa Print "luarbiasa" -> gak mungkin, karna range angka >3 sd <5,
    # dan di baris ke 9, diluar range