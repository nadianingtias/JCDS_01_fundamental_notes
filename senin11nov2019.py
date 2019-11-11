class Fibo:
    def cek(self, fiboKe):
        hasil = ''
        # misal input 5 return 3
        # 0 1 1 2 3
        fibo = [0,1]
        for i in range(fiboKe-1):
            update = fibo[i]+fibo[i+1]
            fibo.append(update)
        print(fibo)
        return fibo[-1]
    def cekFiboRek(self, fiboKe):
        if fiboKe < 2: return fiboKe
        else:
            return cekFiboRek(fiboKe-1) + cekFiboRek(fiboKe-2)
class MyString:
    def invert(self, kalimat):
        res=''
        for i in kalimat:
            # print(i)
            if i.islower():
                i = i.upper()
            else: i = i.lower()
            res = res + i
        return res
if __name__ == '__main__':
    from pprint import pprint

    fibo = Fibo()
    print(fibo.cek(int(input("masukkan urutan fibo : "))))
    
    stringKu = MyString()
    x = "NaDia"
    invert = stringKu.invert(x)
    print(f" String '{x}' menjadi : ",invert)

    x = [
        [1,2,3,10],
        [4,5,6,11],
        [7,8,9,12]
    ]
    # hasil
    # 20 10 00
    # 21 11 01
    # 22 12 02

    result = []
    for i in range(len(x[0])):
        temList=[]
        for j in range(len(x)):
            # print(x[len(x)-1-j][i], end='')
            temList.append(x[len(x)-1-j][i])
        result.append(temList)
        # print('')
    pprint(result)