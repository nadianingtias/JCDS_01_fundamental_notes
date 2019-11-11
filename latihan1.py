def getReverse(inputKal):
    kalimatReverse = ''
    listKata = inputKal.split(' ')
    for kata in listKata: 
        # print(kata[::-1], end=" ")
        kalimatReverse += kata[::-1] + ' '
    return kalimatReverse

# mencetak pola bintang
def star(x):
    star = ''
    for i in range(x):
        star +='* '
        print(star)
def rstar(x):
    star = ''
    for i in range(x):
        star = '* '*(x-i)
        print(star)
def angkaPyramid(x):
    for i in range(x+1):
        for j in range(i):
            print(j+1, end=' ')
        print('')
def angkaPanah(x):
    for i in range((x+1)):
        for j in range(i):
                print(j+1, end=' ')
        print('')
    for i in range((x+1)):
        for j in range(x-i-1):
                print(j+1, end=' ')
        print('')
def angkaAtas1(x):
    for i in range(x+1):
        print((str(i)+' ')* i)
def angkaAtas2(x):
    for i in range(x):
        print((str(i+1)+' ')* (x-i))
def angkaAtas3(x):
    for i in range(x+1):
        for j in range(i):
            print(x-j, end=' ')
        print()

def angkaAtas4(x):
    print("str")
    for i in range(x):
        res=''
        for j in range(x-i):
            res += str(x-j) +' '
        print(res)

def pangkat(x, pangkat):
    res=1
    for i in range(pangkat):
        res*=x
    return res

def pangkatPlus(x, pangkat):
    # 2^3 = 2*2 *2
    # 2*2 = 2 + 2 = 4
    # 4*2 = 4 + 4 = 8

    # 3^4 = 3*3*3*3

    # 3*3 = 3+3+3 = 9
    # 9*3 = 9+9+9 = 27
    # 27*3 = 27+27+27 = 81
    res=0
    tem = x
    for b in range(pangkat-1):
        if b == 0:
            for i in range(x):
                res += tem
        else:
            for i in range(x-1):
                res += tem
        tem = res
    return tem

# 2^3 = 2 * 2^2
# 2^2 = 2 * 2^1
# 2^1 = 2
def pangkatRecursion(x, pangkat):
    if pangkat != 1:
        return x * pangkatRecursion(x,pangkat-1)
    else:
        return x

def faktorial(x):
    if x<=0:
        return 1
    elif x<=2:
        return x
    else:
        return x * (faktorial(x-1))
def faktorialLoop(x):
    res=1
    for i in range(x):
        res *= i+1
    return res
def sep():
    print("----------------------------------------------------")

def lambdaFunction():
    '''
    x = lambda -> function tanpa nama def
    ketika kita butuh function dalam sebuah variabel, 
    tapi tidak mau define function 
    '''
    print("belajar lambda function")
    x = lambda a : a*2
    print("x : ", x(10))

    y = lambda a,b,c : a + b + c
    print("y : ", y(2,5,6))

def myFunction(x):
    return lambda a : a**x
pangkat_2 = myFunction(2)
pangkat_3 = myFunction(3)

bol = lambda a : True if a % 2 == 0 else False
cekGenapGanjil = lambda x : "ganjil" if x%2 != 0 else "genap"

printt = lambda x :  print(x)

def mapFunction():
    # x = map(func, [iterable var])
    '''
    map = mengeksekusi fungsi tertentu untuk setiap elemen dalam 
    suatu variabel yang iterable
    '''
    a = ["cokelat", "melon", "nangka"]
    b = ["apel", "jeruk", "nanas"]
    def combi(a,b): return a+' '+b
    print(list(map(combi, a,b)))

    d = [2,4,6,8,10]
    pangkat = lambda a : a*a #a**2
    print(list(map(pangkat, d)))
    print(pangkat(3))

    zHasil = map(lambda a: a**2, d)
                # fungsi        #iterable
    print(list(zHasil))

def filterFunction():
    sep()
    listX = range(11)
    listXX = range(20)
    print(list(listX))

    def lebihLima(x):
        if x<=5: return False
        else: return True
    listY = filter(lebihLima, listX)
    # kalau True dia masuk, kalau false dia dibuang oleh filter()
    print(list(listY))

    list5keatas = filter(lambda a: True if a >=5 else False, listX)
    print("angka 5 ke atas : ",list(list5keatas))

    # cek2angka = lambda a, b: True if a < 5 and b > 5 else False
    # filterCek2angka = filter(cek2angka, listX, listXX)

from functools import reduce #butuh import library untuk using reduce function

def reduceFunction():
    
    # lambda1 = lambda a: a in [2,3,4,5]
    angka = [1,2,3,4,5]
    # mengetahui perkalian dalam list
    hasil =1
    for i in angka:
        hasil *= i
    print(hasil)
    z = reduce(lambda a,y : a*y, angka)
    print(z)

    stringContoh = ["ini", "ibu", "budi"]
    print(' '.join(stringContoh))
    kalimat = reduce(lambda a,y : a+' ' +y, stringContoh)
    print(kalimat)
    myString = "Nadia Ningtias"
    myName = reduce(lambda a,x: a+ ' '+x, myString)
    print(myName)

def customFunction():
    angka = [1,2,3,4]
    z = filter( lambda a: a>3, map(lambda x: x*2, angka))
    print(list(z))

    z = map( lambda a: a*2, filter(lambda x: x>3, angka))
    print(list(z))

    # CASE SOAL : var nomor = [1-100]
    # => angka genap => setiap angka genap di* 2
    # => hasilnya dijumlahkan satu sama lain
    nomor = range(1,101)
    total = reduce( lambda a,x: a+x,
                                    list(map(lambda a: a*2 , 
                                                            list(filter(lambda a : a%2==0, nomor))
                                            )
                                        )
                    )
    print("total : ", total)
    #pengecekan
    hasil=0
    for i in nomor:
        # print(i)
        if i%2 == 0:
            hasil += i*2
    print("hasil : ", hasil)

    #CASE mencari bilangan prima dari 0-100
    # [2,3,5,]
    cekAngka =7
    x = map(lambda a: a, list(range(2,cekAngka)))
    print(list(x))
    pembagi = list(range(2,cekAngka))
    print(pembagi)
    maps = (map(lambda x,a: False if x%a== 0 else True, list(x), pembagi))
    print(list(maps))

    print("coba",(reduce(lambda a,b : a*b , [1,2,3,4,5])))

    def cekPrimaRekursi(angkatetap,angka):
        # if angka ==2:
        #     return True
        if angka == 1: return False
        if angka == 2: return True
        elif angkatetap % (angka-1)==0:
            # print(angkatetap, angka-1)
            # print("bukan"); 
            return False
        else:
            # print(angkatetap, angka-1)
            # print("lanjut")
            return cekPrimaRekursi(angkatetap, angka-1)
    x=10
    print(f"primakah ?{x} :", cekPrimaRekursi(x,x))
    x=1
    print(f"primakah ?{x} :", cekPrimaRekursi(x,x))

    # lambdaCekPrima = lambda cek, iter: True if angka <= 2 False if cek %(iter-1)==0 else lambdaCekPrima(cek, iter-1)  
    
    # print("cek ini",lambdaCekPrima(13))
    # map(lambdaCekPrima, )

    def cekprima(x):
        prima = False
        listX = range(2,x)
        if x>1 :
            if x == 2:
                prima = True
            for i in listX:
                if x % i==0:
                    prima = False
                    break
                else:
                    prima = True
        else:
            return False
        return prima
    print(cekprima(27))
    sep()
    def cekprima2(x):
        prima = False
        listX = range(2,x)
        if x>1 :
            if x == 2:
                return True
            for i in listX:
                if x % i == 0:
                    print("eh bukan")
                    break
                    return False
                else:
                    return True
        else:
            return False
        # return prima
    print(cekprima2(27))

    primaNumber = list(filter(cekprima, range(101)))
    print(primaNumber)
    print(len(primaNumber))

    sep()
    nums = range(2, 101)
    gums = []
    for i in range(2, 10):
        gums = filter(lambda x: x == i or x % i == 0, nums)
    print(list(gums))

    primelist = lambda n : [ x 
                                for x in range(2, n) #2,3,4,5,6,..,...100
                                    if not 0 in map(lambda z : x % z, range(2,x)) #
                            ]
    print(list(map(str, primelist(100))))


def senin4Nov():
    lambdaFunction()
    print(pangkat_2(4))
    print(bol(24))
    print(cekGenapGanjil(30))

    printt("Nadia Ningtias")
    print(printt("Nadia"))

    mapFunction()
    # print(pangkat(3))
    filterFunction()
    reduceFunction()
    customFunction()

def main():
    # inputKalimat = input("masukkan kalimat : ")
    # hasilReverse = getReverse(inputKalimat)
    # print(f"{inputKalimat} dibalik menjadi = {hasilReverse}")  
    star(5)
    rstar(10)
    angkaPyramid(5)
    angkaPanah(5)
    angkaAtas1(5)
    print('')
    angkaAtas2(5)
    angkaAtas3(5)
    print(' ')
    angkaAtas4(5)

    print(pangkat(2,3))
    print(pangkatPlus(3,3))
    print(pangkatRecursion(2,3))

    #faktorial!
    #4*3*2*1 = 24
    x= 0
    print(f"faktorial {x} : {faktorial(x)}")
    
    print(f"faktorial loop {x} : {faktorialLoop(x)}")

    sep()
    senin4Nov()

if __name__ == '__main__':
    main()

