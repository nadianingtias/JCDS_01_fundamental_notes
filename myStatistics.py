from functools import reduce

class MyStatistic:
    def __init__(self, myList):
        self.list = myList

    def getMean(self):
        return reduce(lambda a,b:a+b, self.list)/len(self.list)

    def getMedian(self):
        copyList = self.list.copy()
        copyList.sort()  # 1. urutkan list
        p = len(copyList) #2. cari tau panjang list
        mid = int(p/2) #3. membagi 2 list
        if p % 2 == 1: #cek panjang list
            return copyList[mid+1] #jika list ganjil
        else: 
            return (copyList[mid-1]+ copyList[mid])/2 #jika list genap

    def getMode(self):
        copySet = self.list.copy()
        copySet.sort()
        copySet = list(set(copySet))
        
        countSet = list(map(lambda a: self.list.count(a), copySet))
        return copySet[countSet.index(max(countSet))]
        # return copySet.index(list(countSet).index(max(countSet)))