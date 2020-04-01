##def segitiga ():
##    for i in range(5):
##        for j in range(i+1):
##            print("*", end= ' ')
##        print()
##    return(i)
##segitiga()

##def persegiEmpat(a,b):
##    for i in range(a):
##        if i == 0 or i == a-1:
##            print("@"*a)
##        else:
##            x = a- b
##            print ("@"+" "*(a-2)+"@")
##persegiEmpat(4,5)

##def jumlahHurufVokal(input):
##    total = 0
##    voc = ["a", "i", "u", "e", "o"]
##    for i in input:
##        if i in voc:
##            total+=1
##    return [len(input), total]
##
##def jumlahHurufKonsonan(input):
##    total = 0
##    voc = ["a", "i", "u", "e", "o"]
##    for i in input:
##        if i in voc:
##            total+=1
##    return [len(input), len(input)-total]

##v = jumlahHurufVokal("virliana")
##k = jumlahHurufKonsonan("virliana")

##print(v)
##print(k)

##def rerata(b):
##    sum = 0
##    for i in b :
##        sum += i
##    nilai=(sum/len(b))
##    return nilai

##from math import sqrt as sq
##def apakahPrima(n):
##    n = int(n)
##    assert n>=0
##    primaKecil = [2,3,5,7,11]
##    bukanPrKecil = [0,1,4,6,8,9,10]
##    if n in primaKecil:
##        return True
##    elif n in bukanPrKecil:
##        return False
##    else:
##        for i in range(2,int(sq(n))+1):
##            if n%1 ==0: #Jika nanti hasilnya bukan prima
##                return False
##                break
##            else: #Jika nanti hasilnya prima
##                return True
##
##print(apakahPrima(112))
##print(apakahPrima(57))
##print(apakahPrima(25))

##from math import sqrt as sq
##def apakahPrima(n):
##    n = int(n)
##    assert n >= 0
##    primaKecil = [2,3,5,7,11]
##    bukanPrKecil = [0,1,4,6,8,9,10]
##    if n in primaKecil:
##        return True
##    elif n in bukanPrKecil:
##        return False
##    else :
##        for i in range (2, int(sq(n))+1) :
##            if n%i == 0:
##                return False
##                break
##        else :
##            return True
##
##for i in range (2,1001):
##    print(str(i)+" "+str(apakahPrima(i)))

##def faktorPrima(x) :
##    a = []
##    b = []
##    hasil = 0
##    bil = x
##    prima =True
##    for i in range(2,x):
##        prima = True
##        for u in range(2, i) :
##            if i % u == 0 :
##               prima = False
##        if prima :
##            a.append(i)
##    idx = 0
##    while bil > 1 :      
##        try:
##            if (bil%a[idx]) == 0 : 
##                hasil = bil/a[idx]
##                bil = hasil
##                b.append(a[idx])
##            else :
##                idx = idx + 1
##        except IndexError :
##            break
##    print (b)


##
##def apakahTerkandung(a,b):
##    return a in b
##
##h = "ma"
##k = "Universitas muhammadiyah surakarta"
##print (apakahTerkandung(h, k))
##print (apakahTerkandung("solo", k))

##for i in range(1,100):
##    if(i % 3) == 0 and (i % 5) == 0 :
##        i = "solo indah"
##    elif(i % 3) == 0:
##        i = "solo"
##    elif(i % 5) == 0:
##        i = "indah"
##    print(i)

##from math import sqrt as akar
##def selesaikanABC(a,b,c):
##    a = float(a)
##    b = float(b)
##    c = float(c)
##    D = b**2 - 4*a*c
##    if (D < 0):
##        print("Determinan negatif. Persamaan tidak mempunyai akar real.")
##    else:
##        x1 = (-b + akar(D))/(2*a)
##        x2 = (-b - akar(D))/(2*a)
##        hasil = (x1,x2)
##        return hasil

##def apakahKabisat(n):
##    if n%4==0:
##        if n%100==0 and n%400==0:
##            return True
##        elif n%100==0 and n%400!=0:
##            return False
##        return True
##    return False
##
##print(apakahKabisat(1851))
##print(apakahKabisat(1900))
##print(apakahKabisat(2000))
##print(apakahKabisat(2400))

##import random
##
##r = random.randint(1,100)
##a = """Permainan tebak angka.
##Saya menyimpan sebuah angka bulat antara 1 sampai 100. Coba Tebak."""
##
##print(a)
##
##b = "Masukkan tebakan ke-"
##f = ":> "
##c = 1
##d = str(c)
##
##for i in range(1,100):
##    e = (b+d+f)
##    a = int(input(e))
##    c+=1
##    d = str(c)
##    if(a < r):
##        print("Itu terlalu kecil. Coba lagi.")
##    elif(a > r):
##        print("Itu terlalu besar. Coba lagi.")
##    elif(a == r):
##        print("benar")
##        break
##

##def katakan(bil):
##    angka = ["","Satu ","Dua ","Tiga ","Empat ","Lima ","Enam ",
##             "Tujuh ","Delapan ","Sembilan ","Sepuluh ","Sebelas "]
##    hasil = ""
##    n = int(bil)
##    if n >= 0 and n <= 11:
##
## 
##        hasil = angka[n]
##    elif n < 20:
##        hasil = katakan(n-10) + " Belas "
##    elif n < 100:
##        hasil = katakan(n/10) + " Puluh " + katakan(n%10)
##    elif n < 200:
##        hasil = " Seratus " + katakan(n-100)
##    elif n < 1000:
##        hasil = katakan(n/100) + " Ratus " + katakan(n%100)
##    elif n < 2000:
##        hasil = " Seribu " + katakan(n-1000)
##    elif n < 1000000:
##        hasil = katakan(n/1000) + " Ribu " + katakan(n%1000) 
##    elif n < 1000000000:
##        hasil = katakan(n/1000000) + " Juta " + katakan(n%1000000)
##    elif n > 1000000000:
##        hasil = 'Maaf, program tidak membaca angka lebih dari Satu Milyar'
##    return hasil
##
##
##a = 1
##while a != 0:
##    a = input(' Masukkan angka dari 1 sd 1.000.000.000: ')
##    huruf = katakan(a)
##    print(huruf +' Rupiah')


def formatRupiah(n):
    y = str(n)
    if len(y) <= 3 :
        return 'Rp ' + y
    else:
        p = y[-3:]
        q = y[:-3]
        return (formatRupiah(q) + '.' + p)
        print ('Rp' + (formatRupiah(q)) + '.' + p)







