#soal ayah dan andi
nAndi = 1
nAyah = 1
totalAyahDanAndi = 50
tahun = -4
ayahBandingAndi = 6/1

kiri = totalAyahDanAndi + abs(tahun*ayahBandingAndi) + tahun
print(kiri)
andi = kiri/(ayahBandingAndi + nAndi)
print(f"Andi : {andi}")
ayah = totalAyahDanAndi - andi
print(f"ayah : {ayah}")

# SOAL IBU DAN ANAK
tahun = -19
banding1 = 7/1
banding2 = 4/1
selisih = 0.5
# ibu = 
x = abs(tahun * banding1) + abs(selisih*(banding1*banding2))
ibu = x/(banding1-banding2)
anak = 19 + (ibu/7)

print(f"umur ibu : {ibu}")
print(f"umur anak : {anak}")

# soal PR
S = {0,1,2,3,4,5,6,7,8,9,10}
A = {2,3,5,7}
B = {5,7,9}

# Tentukan :
A = A
B = B
AnB = A & B
AuB = A | B
AirisanAuB = A & (A | B)
BirisanAuB = B & (A | B)
AuBirisanAuB = (A | B ) & ( A | B)
AuBgabunganAuB = (A & B) | (A | B)

print("==== soal himpunan di dalam set ====")
print(f"A = {A}")
print(f"B = {B}")
print(f"A n B = {AnB}")
print(f"A u B : {AuB}")
print(f"A n (A u B) : {AirisanAuB}")
print(f"B n (A u B) : {BirisanAuB}")
print(f"(A n B) n (A u B) : {AuBirisanAuB}")
print(f"(A u B) u (A u B) : {AuBgabunganAuB}")


# string = "lintang"
# string[1] = 'o'
# print(string)
dictAbjad  = {
    'a':'.-',
    'b':'-...',
    'c':'-.-.',
    'd':'-..',
    'e':'.',
    'f':'..-.',
    'g':'--.',
    'h':'....',
    'i':'..',
    'j':'.---',
    'k':'-.-',
    'l':'.-..',
    'm':'--',
    'n':'-.',
    'o':'---',
    'p':'.--.',
    'q':'--.-',
    'r':'.-.',
    's':'...',
    't':'-',
    'u':'..-',
    'v':'...-',
    'w':'..-',
    'x':'-..-',
    'y':'-.--',
    'z':'--..',
    ' ':' '
}
sep = "\n======================================================================="
def getMorse(kata):
    result = ''
    print(kata, ' = ', end = ' ')
    for letter in kata.lower():
        print(dictAbjad.get(letter), end ="/")
        result += dictAbjad.get(letter)
    print(sep)
    return result

listAbjad = tuple(dictAbjad.keys())
def getCaesarCipher(kata, step):
    result =''
    print(kata, ' = ', end = ' ')
    for letter in kata:
        print(listAbjad[((listAbjad.index(letter.lower()) + int(step)) % len(dictAbjad))], end='')
        result += listAbjad[((listAbjad.index(letter.lower()) + int(step)) % len(dictAbjad))]
    print(sep)
    return result

caesarCipherResult = getCaesarCipher(input("Caesar cipher dengan kata : "), input("Step : "))
print(caesarCipherResult)

def malangers(kalimat):
    splitsent = kalimat.split('a')
    result = ''
    # print(splitsent)
    for letter in splitsent:
        result += letter[::-1]+ ' '
    return result

def getLuas(sisi):
    luas = sisi*sisi
    return luas

def main():
    print(sep)
    x = getMorse(input("membuat morse dengan kalimat : "))
    sisi = 7
    luasX = getLuas(sisi)
    print(luasX)

    volume = luasX * sisi

    morseResult = getMorse(input("membuat morse dengan kalimat : "))
    # print(morseResult)

    caesarCipherResult = getCaesarCipher(input("Caesar cipher dengan kata : "), input("Step : "))
    # print(caesarCipherResult)

    reverseByWordResult = malangers(input("reverse by kata : "))
    print(reverseByWordResult)



if __name__ == '__main__':
    print(" ")
    # main()

   