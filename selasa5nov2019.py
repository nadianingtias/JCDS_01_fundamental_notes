from pprint import pprint

class Mobil:
    warna = 'merah'
    tahun = 2010
    roda = 4
class MobilCustom():
    # ask :: how to init not full instance
    def __init__(self, warna, tahun, roda):
        self.warna = warna
        self.tahun = tahun
        self.roda = roda
    # def __init__(self, warna):
    #     self.warna =warna

    def jadul(self):
        if self.tahun < 2010:
            return True
        else : return False
    
    def tes(self):
        print(self.warna, self.tahun, self.roda, self.jadul())

#CARA INHERIT 1
class Car(MobilCustom): #(CHILD) inheritance from MobilCustom
    gps = True
    # pass
    # Use the pass keyword when you do not want to add any other properties or methods to the class.

# CARA INHERIT 2
class Person:
    def __init__(self, nama, gelar):
        self.name = nama
        self.gelar = gelar
class Wisudawan:
    def __init__(self, nama, gelar, ipk):
        Person.__init__(self, nama, gelar)
        self.ipk = ipk

#CARA INHERIT 3
class Wisudawati:
    def __init__(self, nama, gelar):
        super().__init__(nama, gelar)
class Student:
    def __init__(self, nama, usia):
        self.nama = nama
        self.usia = usia

def mengubahDataJadiObjek():
    data = [
        {'nama': 'Nadia Ningtias', 'usia': 21},
        {'nama': 'Andi', 'usia': 22},
        {'nama': 'Budi', 'usia': 23},
        {'nama': 'caca', 'usia': 24},
    ]
    namas = ['nad', 'and', 'bud', 'cac']
    print("----------------------------------------------------")
    # print(list(map(lambda a: vars()[a], namas)))


    tem = [] # list of object yang akan digenerate
    for i in range(len(data)):
        # print(dt)
        vars()[namas[i]] = Student( data[i].get('nama'), data[i].get('usia'))
        tem.append( Student(data[i].get('nama'), data[i].get('usia')))
        print(vars()[namas[i]].__dict__)
    
    for obj in tem:
        pprint(obj.__dict__)

    print(tem[0].nama)
    # print(nad.__dict__)

def persegiBerdasarSisi():
    class Persegi:
        def __init__(self, sisi):
            self.sisi = sisi
            self.keliling = sisi*4
            self.luas = sisi**2
    # class PersegiPanjang:

    persegi1 = Persegi(5)
    pprint(persegi1.__dict__)

def latihan5November():
    mobil1 = Mobil()
    print(mobil1.roda)
    print(mobil1.warna)

    car1 = Car('item', 2019, 4)
    print(car1.warna)
    mobilCustom1 = MobilCustom('hitam', 2016, 4)
    # mobilCustom2 = MobilCustom('ijo')
    # mobilCustom1.tes()

    nadia = Person("nadia", 'S.St')
    nadiaN = Wisudawan("Nadia Ningtias", "S.Tr",3.5)
    print(nadia.name)
    print(nadiaN.ipk)

    # VIEWING dictionary / (Object)
    

    pprint(vars(nadiaN))
    print(nadiaN.__dict__)
    print(vars(nadiaN))
    print(vars)

    #ACCESSING atributte
    print(getattr(nadiaN, 'gelar'))
    print(hasattr(nadiaN,'usia'))
    print(hasattr(nadiaN,'name'))

    #objek yang sudah jadi bisa ditambah atribute 
    nadiaN.warna = "cokelat"
    setattr(nadiaN,"alamat", "BSD City")
    

    #menghapus atribute dari objek
    delattr(nadiaN, 'alamat')
    del nadiaN.warna
    pprint(vars(nadiaN))

    mengubahDataJadiObjek()
    persegiBerdasarSisi()

# I V L C D M
# 3456 ->MMM CD L V I
cheat = [0, 
            ('I','V'), 
            ('X','L'), 
            ('C', 'D'), 
            ('M', '')
        ]
    
# def keRomawiUnder4000(angka):
#     strAngka = str(angka)
#     lenAngka = len(strAngka)
#     hasilRomawi=''
#     for i in range(1, lenAngka+1):
#         pop = strAngka[-1 * i]
#         if pop == '4':
#             # print(cheat[i][2])
#             hasilRomawi = cheat[i][2] + hasilRomawi
#         elif int(pop) <4:
#             # print(cheat[i][0]*int(pop))
#             hasilRomawi = cheat[i][0]*int(pop) + hasilRomawi
#         elif int(pop) == 9:
#             hasilRomawi = cheat[i][3] + hasilRomawi
#         elif int(pop/5):
#             # print(cheat[i][1]+cheat[i][0]*int(pop))
#             hasilRomawi = cheat[i][1]+cheat[i][0]*(int(pop)-5) + hasilRomawi
#     print(f"angka {angka} : ", hasilRomawi)
#     return hasilRomawi

first = ['I','X','C','M','']
second = ['V','L','D','']
cheat2 = [first, second]
def keRomawiUnder4000(angka): #34 4
    strAngka = str(angka)
    lenAngka = len(strAngka)
    hasilRomawi=''
    for i in range(1, lenAngka+1): #satuan, puluhan, ratusan, ribuan
        pop = int(strAngka[-1 * i])
        if pop == 4:
            hasilRomawi = cheat2[0][i-1] + cheat2[1][i-1] + hasilRomawi
        elif pop == 9:
            hasilRomawi = cheat2[0][i-1] + cheat2[0][i] + hasilRomawi
        else:               #ket:1,2,3, 5, 6,7,8
            hasilRomawi = (int(pop/5)*cheat2[1][i-1]) + (cheat2[0][i-1]*(pop%5)) + hasilRomawi
    print(f"angka {angka} : ", hasilRomawi)
    return hasilRomawi
def convertRomawi(ang):
    hasil =''
    angka = ang
    while angka !=0:
        locSatuan = len(str(angka))-1
        pembagi = (10**(locSatuan))
        muncul = int(angka/pembagi)
        if muncul == 9:
            hasil = hasil + cheat2[0][locSatuan] + cheat2[0][locSatuan+1]
        elif muncul == 4:
            hasil = hasil + cheat2[0][locSatuan] + cheat2[1][locSatuan]
        else:   #ket: 1,2,3, 5,6,7,8
            hasil = hasil + int(muncul/5)*cheat2[1][locSatuan] + (muncul%5)*cheat2[0][locSatuan]
        angka = angka % pembagi
    print(f"angka {ang} : ", hasil)
    return (hasil)

def tugas5November():
    angka = 3222
    keRomawiUnder4000(angka)
    convertRomawi(angka)   
    # print(rom)     
def main():
    latihan5November()
    tugas5November()

if __name__ == '__main__':
    main()
    