#membuat bangun datar layang-layang
#input data
angka = int(input("Masukkan Angka : "))
batas = angka;
#perulangan 1
for x in range (0,angka):
    for y in range (-2, batas+1):
        print(" ", end="")
    
    for z in range (0,x+1):
        print("* ",end="")
    batas-=1
    print("")
#perulangan 2
batas=angka;
for x in range (1,angka):
    for y in range (-4, x):
        print(" ",end="")

    for z in range (1,batas):
        print("* ",end="")
    batas-=1
    print("")
