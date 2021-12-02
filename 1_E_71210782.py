#input data awal deret
x = int(input("Masukkan awal deret: "))

#input data akhir deret
y = int(input("Masukkan akhir deret: "))

#rumus perulangan
for i in range (x,y):
    if(i%2==0) and (i%5 !=0) and (i%9 !=0):
        print(i, " ",end="")
