import datetime as dt 
from hariwaktu import Hariwaktu 
from myStatistics import MyStatistic
class Ibu:
    def __init__ (self, x ):
        self.x = x

class Anak(Ibu):
    def __init__(self, x, y):
        Ibu.__init__(self, x)
        self.y = y

class Cucu(Anak): # multilevel inheritance
    def __init__(self, x, y, z):
        Anak.__init__(self, x, y)
        self.z = z

class Karnivora:
    def __init__(self):
        self.taring = True
        self.makanan = 'daging'
class Herbivora:
    def __init__(self):
        self.geraham = True
        self.makanan = 'daun'
class Omnivora(Karnivora, Herbivora):
    def __init__(self):
        Herbivora.__init__(self)
        Karnivora.__init__(self)
        
        self.seri  = True
        self.makanan = 'mcd' 

def main():
    objA = Cucu('nadia', 'Data Scientist', 'True')
    print(vars(objA))

    manusia = Omnivora()
    print(vars(manusia))
    print(Omnivora.__mro__)

    x = dt.datetime.now()
    print(x)
    print(x.strftime('%d')) #tgl
    print(x.strftime('%A')) #hari
    print(x.strftime('%m')) #bln
    print(x.strftime('%B')) #nama bulan
    print(x.strftime('%Y')) #thn
    print('-------')
    print(x.strftime('%H')) #24 jam
    print(x.strftime('%I')) #12 jam
    print(x.strftime('%p')) # am/pm
    print(x.strftime('%M')) #min
    print(x.strftime('%S')) #sec
    print('--------')


    print(x.strftime('hari ini %A sekarang adalah %H:%M:%S WIB'))
    hariIni = Hariwaktu(x)
    # now = time(x)

    print(hariIni.hari)
    print(hariIni.bulan)

    angka = [1,3,9,2,6,4,7,8,5,5]
    # angka.sort()
    myStat = MyStatistic(angka)
    print("list : ", angka)
    print("mean : ",myStat.getMean())
    print("median : ",myStat.getMedian())
    print("modus : ",myStat.getMode())

if __name__ == '__main__':
    main()
    

    