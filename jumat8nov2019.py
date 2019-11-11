from pprint import pprint

# DATA
# read = r
# write = w
# append = a

data = open('MODUL1-basic_python\data-baru.txt', 'a')
data.write('ini adalah 123')
data.write('ini adalah 321')

data = open('MODUL1-basic_python\ video.mp4', 'w')
data.write('My Video')

# data = open('MODUL1-basic_python\ gambarPDF.pdf', 'w')
# data.write('My Video')

data = open('MODUL1-basic_python\ filePY.py', 'w')
data.write('print("hello word Nadia")\n')
data.write('def hitungLuas():')

# Mengeksekusi script python di dalam file .txt
data  = open('MODUL1-basic_python\data.txt', 'r')
# print(data.read())
# exec(data.read())
# data.readline()

appendd  = open('jumat8nov2019.py', 'a')
appendd.write(data.read())


# data1 = open('MODUL1-basic_python\data.txt', 'r')
# kontenData1 = (data1.read())
# split = kontenData1.split(', ')[::-1]

# print(split)
# data2 = open('MODUL1-basic_python\data.txt', 'w')
# for i in range( len(split)):
#     data2.write(split[i]+'\n')
# #Andi, Budi, Caca
# Andi, Budi, Caca
class Person:
    def __init__(self, nama, usia, kota):
        self.nama = nama
        self.usia = usia
        self.kota = kota

# UNTUK membaca file yang berada di LUAR folder 
# file = open('./../../MODUL1-basic_python/file.csv', 'r')
# UNTUK membaca file yang berada di DALAM folder
file = open('./MODUL1-basic_python/file.csv', 'r')
rowsFile = file.readlines() 
listPerson = []

# LOOPING FOR - membuat objek Person
# for row in range(1,len(c)):
#     # print(c[row])
#     split = rowsFile[row].split(',')
#     # print(split)
#     personX = Person(split[0], int(split[1]), split[2][:-1])
#     pprint(personX.__dict__)
#     listPerson.append(personX)
# pprint(listPerson)
# ini : Caca

# MAP with LAMBDA FUNCTION
listPerson = list(map(lambda x: Person(x.split(',')[0], int(x.split(',')[1]), x.split(',')[2][:-1]), rowsFile[1:]))
# print(listPerson)

for x in listPerson:
    print(vars(x))
    x.__dict__
    pprint(vars(x))

["nama", "usia","kota/n"]
head = rowsFile[0].split(',')
head[-1] = head[-1][ :-1]
print(head)
split = list(map(lambda x: x.split(','), rowsFile[1:]))
print(split)
listDictPerson =[]
for row in range(len(split)):
    temDict = {}
    for i in range(len(head)):
        if i == 1:
            temDict[head[i]] = int(split[row][i]
            temDict.update({ head[i] : int(split[row][i]) })
        elif i == 2 :
            temDict.update({ head[i] : split[row][i][:-1] })
        else:
            temDict.update({ head[i] : split[row][i] })
    listDictPerson.append(temDict)
pprint(listDictPerson)

fileJSon = open('1.json', 'w')
fileJSon.write(str(listDictPerson))