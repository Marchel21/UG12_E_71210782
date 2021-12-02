#input hari
senin = ['ke-1 Algoritma Graf','ke-3 Sistem Operasi','ke-4 PAK','ke-5 Praktikum INLAN']
selasa = ['ke-2 Matematika Teknik','ke-4 Bhs Indonesia','ke-6 PKN']
kamis = ['ke-1 IMK','ke-3 Logmat','ke-4 Praktekkom']
jumat = ['ke-2 Sistem Basis Data','ke-4 Praktikum Sistem Basis Data','ke-6 INLAN']

#data
go = input("Hi Tutu, Silahkan Masukkan hari yang ingin Anda telusuri : ")

#if dan else
if go == "senin":
    for i in range (len(senin)):
        print("kelas",senin[i])
elif go == "selasa":
    for i in range (len(selasa)):
        print("kelas",selasa[i])
elif go == "rabu":
    print("Hari rabu Anda tidak ada kelas")
elif go == "kamis":
    for i in range (len(kamis)):
        print("kelas",kamis[i])
elif go == "jumat":
    for i in range (len(jumat)):
        print("kelas",jumat[i])
