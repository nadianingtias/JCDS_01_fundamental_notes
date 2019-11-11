print('halo, ini adalah hari pertama kelas data science di purwadhika')
print(2*4)
'''
ini comment
'''
# ini comment

nama = "budi"       # string
usia = 19           # integer
tinggi = 189.5      # float
jomblo = True        # boolean

imajiner = 5j          #complex

print('1 Halo, aku', nama) 
print('2 Halo, aku ' +nama+ " umurku ", usia)
print('3 Halo, aku ' +nama+ " umurku " + str(usia))
# print('Halo, aku ' ,nama " umurku ", usia) #error, tidak bisa koma digabung dengan +

#------------------------------------------------------------------------------------
# STRING penyisipan

print("jum'at")
print('jum\'at') #untuk mematikan single quote yang hidup

print('4 Halo, aku ' ,nama, " umurku ", usia)
print('5 Halo, aku %s, umurku %d, tinggiku %f' % (nama, usia, tinggi)) ## versi template string
print('6 Halo, aku {}, umurku {}, tinggiku {}'.format(nama, usia, tinggi))
print(f'7 Halo, aku {nama}, umurku {usia}, tinggiku {tinggi}')

teks = "Jasa Raharja"
print(teks.lower())
print(teks.upper())

print(teks.islower())
print(teks.isupper())


print(teks[-5])
print(teks[len(teks)-1]) 
print(teks[-1])
# string[start : stop : step]


teks2 = "Purwadhika Startup Startup & coding School"
print(len(teks2.replace(' ','')))

print(teks2.lower().count('startup'))
print(teks2.lower().count('c'))

for i in range(10):
    print(i)

# import math

# x = 2
# y = math.pow(x, 5)
# print(y)
# print(type(y))
# print(type(int(y)))


#MENCARI banyak HURUF H 
nama = 'Hari ini Hari tidak masuk kelas'
cari = 'h'
x = nama.lower().replace(cari.lower(), '')
jmlCari = len(nama) - len(x)
print(f'jumlah huruf h ada {jmlCari}')

#Mencari banyak kata Hari
cariKata = 'hari'
lenCariKata = len(cariKata)
x = nama.lower().replace(cariKata.lower(), '')
jmlCari = int((len(nama) - len(x))/lenCariKata)
print(f'jumlah kata \'hari\' ada {jmlCari}')

x= 2
y = 144 ** (1/2)
print(y)

print((1,2,3,4,5,6,7,8,9,200))
#pembulatan
bulat = round(3.55550383, 3)
print(bulat)

print(.3+.4)

import math
print(round(0.3))
print(math.pi)
print(math.floor(0.9))
print(math.ceil(3.2))

print(math.factorial(4))

nKambing = 0
nAyam = 0
kakiKambing = 4
kakiAyam = 2
kambingDanAyam = 13
kambingDanAyamKaki = 32
# k + a = 13
# 4*k + 2*a = 32

# 4k + 2a = 32
# 2k + 2a = 26
# 2k = 6
x = (kakiKambing-kakiAyam)
nKambing = (kambingDanAyamKaki - (x*kambingDanAyam))/x
print(nKambing)
print(f"jumlah kambing : {nKambing}")
nAyam = kambingDanAyam - nKambing
print(f"jumlah ayam : {nAyam}")

#
# 4k + 4a = 52
# 4k + 2a = 32
# 2a = 20
#a = 10
x = (kakiKambing)
nAyam = abs(kambingDanAyamKaki - (x*kambingDanAyam))/kakiAyam
print(nAyam)
print(f"jumlah ayam : {nAyam}")
nKambing = kambingDanAyam - nAyam
print(f"jumlah ayam : {nKambing}")

nAyam = abs(kambingDanAyamKaki - kakiKambing*kambingDanAyam)/(kakiKambing - kakiAyam)
print(nAyam)

nKambing = 0
nAyam = 0
kakiKambing = 4
kakiAyam = 2
kambingDanAyam = 13
kambingDanAyamKaki = 32

nKambing = abs(kambingDanAyamKaki - (kakiAyam)*kambingDanAyam)/(kakiKambing - kakiAyam)
print(nKambing)

# k - 4
# a - 2
kakiKambing = 4
# kakiAyam = 4
kakimereka = 32
jiwa = 13

selisihKaki = abs(kakiKambing - kakiAyam)
nKambing = abs(kakimereka - (kakiAyam)*jiwa) / selisihKaki
nAyam = abs(kakimereka - (kakiKambing)*jiwa) / selisihKaki

print(nKambing)
print(nAyam)


# k - 4
# s - 2
# kakimereka = 24
# jiwa = 6

# k + s = 6
# 4k + 4s = 24

# 4k + 4s = 24
# 4k + 4s = 24



# mas rudi dan mas kal
ekor = 5
kaki = 12
kakiKambing = 4
kakiAyam = 2

ayam = abs((kakiKambing*ekor-kaki)/kakiAyam)
kambing = abs((kakiAyam*ekor-kaki)/kakiKambing)
print(ayam)
print(kambing)

# BELAJAR INPUT 
# totalHewan = int(input('Ketik total hewan : '))
# print(totalHewan)
# totalkaki = int(input('Ketik total kaki hewan : '))
# print(totalkaki)
# kakiA = int(input('Jumlah kaki A : '))
# print(kakiA)
# kakiB = int(input('Jumlah kaki B : '))
# print(kakiB)
# selisihAB = abs(kakiA - kakiB)
# print(selisihAB)
# A = abs(totalkaki - (kakiB)*totalHewan) / selisihAB
# B = abs(totalkaki - (kakiA)*totalHewan) / selisihAB

# print(f"kaki A : {A}, kaki B : {B}")

# ----------------------SOAL 3 umur ibu dan anak dan ayah
# umurAnak= 0
# umurIbu = 0

# umurAnak = (1/4 * umurIbu) - 0.5 + 19

# umurAnak = 19 + (1/7 * umurIbu)
# umurAnak = 19/7 + 19*umurIbu
# umurIbu = (19/7 - umurAnak )/19
# umurIbu = 1/7 - (19*umurAnak)

# umurAnak = (1/4 * (1/7 - (19*umurAnak)) ) - (1/2) + 19
# umurAnak = (1/28 - 19/4*umurAnak) - 18.5
# umurAnak + 19/4 umurAnak = 

# [start:stop:step]
var = 'abcdefghijklmmmmmmmn'
print(var[::2])
print('z' in var)
print(var.count('m'))

hari = ['sen', 'sel', 'rab', 'kam', 'jum', 'sab', 'min']

#hari ke seratus setelah rabu ?
now = 'min'
stepHari = -3
cariHari = (hari.index(now) + stepHari % len(hari)) % len(hari)

print(f"Hari ini {now}, jadi {stepHari} lagi adalah hari : {hari[cariHari]}")
hari.insert(10, 'nadia')
print(hari)

hari.remove('nadia') #remove dengan value di dalam list
print(hari)

hari.pop()
print(hari)

hari.pop(2)     #remove dengan index yang ada di dalam list
print(hari)

# hari.clear()
print(hari)

hari.reverse()
print(hari)

hari = hari[::-1] #fungsinya sama dengan hari.reverse()
print(hari)

hari.sort()
print(hari)

hari.sort(reverse=True)
print(hari)


x = 'abc'
x = list(x)
print(type(x))
print(x)

x = [1,2,3,4,5]
print(list(reversed(x)))

y = x
y[0] = 0
print(x)
print(y)

z = x[::2].copy()
print(z)

print( x + z)

print(z*2)

z.append(z)
print(z)
a = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(a)

b = [1,2,3,3,5,6,3,3,3,3,]
# print(b.index(3))
print("---")

#method untuk mengeprint index dengan nilai tertentu
def cariIndexN(listX, cari):
    for i in range(len(listX)):
        if listX[i]==cari:
            print(i)

cariIndexN(b,3)

def carIndex(listY, i):
    return [x for x, y in enumerate(listY) if y == i]

#-----TUPLE---------

b = (6, 'y', 7)
b = b.count(6)
print(b)
# b[0] = 9   # tuple itu tidak bisa diubah !! [ IMMUTABLE ] 'tuple' object does not support item assignment

listA = [1,2,3,4,5,6]
tupleA = tuple(listA)

print(tupleA)

tupleB = tupleA

listAA = [0]
tupleAA = (0,) # tuple hanya 1 elemen tidk jadi tuple jika belum ada koma nya

print(listAA)
print(type(tupleAA))

tupA = (1,2,3)
tupB = tupA * 4
print(tupB)

lisB = list(tupB)
print(lisB)

# kenapa harus ada tuple ? untuk mengamankan list dari Database yang tidak boleh diubah2

#======================== Day KAMIS, 24 Oktober 2019

x = [
    (
        1,
        ['a','b','c'],
        (4,5,6)
    )
]
x[0][1][2] = 'Andi'
print(x)
lis = [1,2,3]
tup = tuple(lis)
print(type(tup))


# SET = type data tanpa indexing, 
# dan elemennya unik, tidak ada redundansi
# set itu mutable, tapi elemen2nya immutable
# hasill .add() nya diletakkan random di dalam variabel set
set0 = {1,2,3,4,5,1}
print(type(set0))
print(set0)

set0.add('a')
set0.add('b')
set0.add('c')
set0.add('d')
set0.add('e')
print(set0)

for i in set0:
    print(i)



# mengupdate SET dengan update()
set0.update("andi") #hasilnya akan menambah a, n, d, i
set0.update([10,11,12,13]) #hasil akan menambah 10, 11, 12, 13
set0.add((10,11,12,13)) #hasil akan menambah saatu tuple baru berisi 10, 11, 12,13
print(set0)
set0.remove((10,11,12,13))
print(set0)
set0.remove('e')
print(set0)
set0.pop()
print(set0)
set0.pop()
print(set0)

set0.clear()
print(set0)

del set0
# print(set0)


# MENCARI IRISAN
lis1 =[1,2,3,4,5]
lis2 = [2,3,5,6,7]

set1 = set(lis1)
set2 = set(lis2)

print(set.intersection(set1,set2))
print(set1)

#MENCARI GABUNGAN (notasi gabungan = | atau set.union(set1, set2))
print(set.union(set1, set2))
set3 = set1 | set2
print(set3)

#mencari Selisih / difference
print(set.difference(set1, set2)) #ada di A gada di B
print(set1 - set2)
print(set.difference(set2, set1)) #ada di B gada di A
print(set2 - set1)

#simetric
print(set.symmetric_difference(set1,set2))
print(set1^set2)

p = {1,2,4,7,9,19}
q = {5,6,7,9,12,16,17,19}
r = {3,6,8,19}

#soal internet
pnq =  set.intersection(p,q)
print(pnq)
pnqn = set.intersection(p,q,r)
print(pnqn)

#soal SMP internet
p = {-4,-3,-2,-1,0,1,2,3,4}
q = {-7,-6,-5,-4,-3,-2,-1,0,1}
r = {2,-1,0,1,2,3,4,5,6,7}

puq = p | q
print(puq)
puq = list(puq)
print(puq)
puq.reverse()
print(puq)

pur = p | r
qur = q | r

print(type(puq))
print(pur)
print(qur)

# ------------ Dictionary -------------
andi = {
    'name' : 'andi',
    'age' : 22,
    'is_married' : False,
    'job' : 'PNS',
    'cars' : ['Alphard', 'Xpander','Innova'],
    'address' : {
        'street' : 'Mawar Ungu',
        'RT' : 5, 'RW' : 121, 'kecamatan' : 'serpong',
        'zipcode' : 61234,
        'geo' : {
            'lat' : 111.22,
            'lng' : 78.28
        }
    }
}

print(andi['name'])
print(andi['age'])
print(andi['is_married'])

print(andi.get('job', 'Maaf andi masih nganggur'))
# print(andi['job']) #rising ERROR !!
andi['name'] = "Budi"

print(andi.keys())
print(andi.items())
print(type(andi.items()))

x = ['name', 'age', 'is_married']
print(andi.fromkeys(x))


print('# mengakses nested Dictionary')
print(andi['address']['geo'])

#menambah key dan value di dalam dictionary [UPDATEkey-value di dalam dictionary]
andi['salary'] = 25000000
andi.update({'no_ktp' : 12345675443})

# print(andi.clear())
print(andi)

andilist = list(andi.items()) # ambil pasangan key -value
andilist = list(andi.values()) #ambil values saja
print(andilist)
print(andilist[5]['geo'])

days = {
    'senin' : 'monday',
    'selasa' : 'tuesday',
    'rabu' : 'wednesday',
    'kamis' : ' thursday',
    'jumat' : 'friday',
    'sabtu' : 'saturday',
    'minggu' : 'sunday'
}

i= True
# KONVERSI HARI2 DALAM BAHASA INDO-ENGLISH
# while i == True:
#     day = input("ketik nama hari : ")
#     artinya = days.get(day.lower(), "tidak ada hari tersebut di dalam bahasa indonesia")
#     print(f"bahasa inggris {day} = {artinya}")

# daysKeys = list(days.keys()) #daftar indo
# daysValues = list(days.values()) #daftar eng 6

# while i == True:
# day = input("type the day : ")
# if day in daysValues:
#     artinya = daysKeys[daysValues.index(day.lower())]
#     print(f"bahasa of {day.upper()} = {artinya.upper()}")
# else:
#     artinya = daysValues[daysKeys.index(day.lower())]
#     print(f"bahasa of {day.upper()} = {artinya.upper()}")

# belajar condition

#jika di if langsun dicek value boolean false maka langsung masuk else atau elif di bawah nya
if False:
    print("ini true")
else:
    print("ini false")

x = 2; y=5
print(x < 10 and y > 0)

nilai = 98
if nilai >= 82:
    result = 'A'
elif nilai >=72:
    result = 'B'
elif nilai >=62:
    result = 'C'
elif nilai >= 52:
    result = 'D'
else:
    result = 'E'

print(f" Nilai kamu : {nilai}, jadi kamu golongan : {result}")

day = 'senin'
for indo, eng in days.items():
    if indo == day:
        print(f"indo : {day}, english : {eng}")

print(days.items())
print(list(days.items()))


daysKeys = list(days.keys()) #daftar indo
daysValues = list(days.values()) #daftar eng 6
day = input("type the day : ")
if day in daysValues:
    artinya = daysKeys[daysValues.index(day.lower())]
    print(f"bahasa of {day.upper()} = {artinya.upper()}")
else:
    artinya = daysValues[daysKeys.index(day.lower())]
    print(f"bahasa of {day.upper()} = {artinya.upper()}")

# 28 Oct 2019
# function 
def hello():
    print("hello world!")
def kuadrat3():
    print(2 ** 3)
def pangkat(angka1, angka2):
    print(angka1 ** angka2)

kuadrat3()
# pangkat(
#     float(input("ketik angka 1 : ")),
#     float(input("ketik angka 2 : "))
# )

'''
buat sebuah function 1 parameter untuk menentukan ganjil atau genap
'''
def cekGanjilGenap(x):
    if x % 2 != 0:
        print("ganjil")
    else:
        print("genap")

# cekGanjilGenap(float(input("\nmasukkan angka yang ingin dicek : ")))
# print(2.2 % 2)

'''
buat function untuk input angka, operator, input angka 2, output hasil dari
'''
def operasi():
    angka1 = float(input("masukkan angka 1 : "))
    operan = input("masukkan operan (+ - * /): ")
    angka2 = float(input("masukkan angka 2 : "))
    res = 0
    if operan == '+':
        res = angka1 + angka2
        print(angka1, operan ,angka2)
    elif operan == '-':
        res = angka1 - angka2
        print(angka1, operan ,angka2)
    elif operan == '*':
        res = angka1 * angka2
        print(angka1, operan ,angka2)
    elif operan == '/':
        res = angka1 / angka2
        print(angka2, operan ,angka2)
    else :
        print("maaf operan anda salah")
    print(f"hasil : {res}")
# operasi()

students= ['andi', 'budi', 'caca']
def tes(x):
    print(x[0])
    print(x[2])
    
'''
function ubah huruf vokal menjadi o
'''
def oVocal(text):
    voc = ['a','e','u','i']
    for vo in voc:
        text = text.lower().replace(vo, 'o')
    # text = text.replace(voc[0], 'o')
    # text = text.replace(voc[1], 'o')
    # text = text.replace(voc[2], 'o')
    # text = text.replace(voc[3], 'o')
    print(text)
# oVocal(input('masukkan kata ubah jadi o vocal : '))

#RETURN function
def luasPersegi(sisi):
    luas = sisi * sisi
    return luas

sisiA = 6
luasPersegiA = luasPersegi(sisiA)
print(luasPersegiA)

# WHILE looping

pertamax = 5
while pertamax < 10 :
    print("gunakan premium")
    pertamax += 1

students = ['andi', 'budi', 'caca', 'deni', 'elsa', 'fifi']
index = 0
while index < len(students):
    print(students[index])
    index += 1

x = [1,2,3,4,5,6,7,8,9,10]
y = []
i = 0
while i <= (len(x)-1): 
    y.append(x[i]**2)
    i+=1
print(y)

for letter in 'geeksforgeeks':  
    if letter == 'e' or letter == 's': 
         continue
    print ('Current Letter :', letter )
    var = 10

#while, break, studi case password input
state = False
password = '123'
chance = 3
inputPass = input("masukkan password : ")

while state == False:
    if inputPass == password:
        state = True
        print("Pasword Benar !")
    else :
        inputPass = input("Password salah, masukkan password : ")
        chance -= 1
        if chance == 0 :
            break

#FOR loop
kota  = ['Jakarta', 'Bandung', 'Surabaya']
for city in kota:
    print(city)

for i in range(len(kota)):
    print(kota[i])

for i in range(2,20,2): #start, stop, step
    if i == 8:
        continue
    if i == 12:
        break
    print(i)
else:
    print('ok cuy')

for i in range(10):
    if i % 2 == 0:
        print('wow')
    else:
        print(i)

# FizzBuzz
# kelipatan 3 print Fizz
# kelipatan 5 print Fizz
# kelipatan 3 dan 5 print FizzBuzz

def fizzBuzz(num):
    if num%3 == 0 and num%5 == 0:
        print("FizzBuzz")
    elif num%3 == 0:
        print("Fizz")
    elif num%5 == 0:
        print("Buzz")
    else:
        print("try again")

# while True:
#     fizzBuzz(float(input("input fizzbuzz : ")))

#
x = [1,2,3,4,5,6,7]

#1
x.reverse()
print(x)

#2
x = [2,4,6,8,10,12]
print(x[::-1])

#3
y = []
for i in range(len(x)):
    y.append( x[(len(x)-1)-i] )
x = y.copy()
print(x)

#4
x = [2,4,6,8,10,12]
i = len(x)-1
z = []
while i >=0:
    z.append(x[i])
    i -= 1
print(z)

#ubah lintang jadi lontong tanpa replace

string = 'lintang'
listStr = list(string)

vocal = ['a', 'i', 'u', 'e', 'o']
for i in range(len(listStr)):
    if listStr[i] in vocal:
        listStr[i] = 'o'

string = ''.join(listStr)
print(listStr)
print(string)


string = 'Lintang'
# Define your variables
result = ''
vocal = ['a', 'i', 'u', 'e', 'o']
for i in string:
        if i in vocal:
                i = '0'
        result += i
print(result)
string = result
print(string)

# make a function that prove PALINDROME word
# k a t a k

# PALINDROM
# 1 line using index manipulation
def ispalindrome(word):
    return word == word[::-1]
print(ispalindrome("katak"))

# PALINDROM
# USING RECURSION
def ispalindrome2(word):
    print("jalan")
    if len(word) < 2: #exit gate -> ketika masih 2 harus dicek, kalau sudah 1 atau ABIS true
        return True
    if word[0] == word[-1]: 
        print(word[1:-1])
        return ispalindrome(word[1:-1]) #=> RECURSION IS HERE !!
    else:
        return False
print(ispalindrome2("malayalam"))


#NEXT
