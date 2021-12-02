def nilai_penuh1(list_angka) :
    nilai_terbesar = list_angka[0]
    for nilai in list_angka :
      if nilai > nilai_terbesar :
        nilai_terbesar = nilai
    return nilai_terbesar
def nilai_penuh2(list_angka) :
    nilai_terkecil = list_angka[0]
    for nilai in list_angka:
      if nilai < nilai_terkecil :
        nilai_terkecil = nilai
    return nilai_terkecil
listangka1 = [3, 20, 100, -35, 50]
listangka2 = [3, 20, 90, 35, 75]
print(listangka1)
print("nilai terbesar:", nilai_penuh1(listangka1))
print("nilai terkecil:", nilai_penuh2(listangka1))
print(listangka2)
print("nilai terbesar:", nilai_penuh1(listangka2))
print("nilai terkecil:", nilai_penuh2(listangka2))
