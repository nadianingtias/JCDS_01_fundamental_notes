import datetime as dt 
days = {
            'senin' : 'monday',
            'selasa' : 'tuesday',
            'rabu' : 'wednesday',
            'kamis' : ' thursday',
            'jumat' : 'friday',
            'sabtu' : 'saturday',
            'minggu' : 'sunday'
        }
months = {
            'januari' : 'january',
            'februari' : 'february',
            'maret' : 'march',
            'mei':'may',
            'juni':'june',
            'juli':'july',
            'agustus' : 'august',
            'oktober' : 'october',
            'desember':'december'
}
class Hariwaktu:
    def __init__(self, x):
        self.hari = self.hariIndo(x.strftime('%A'))
        self.tanggal = x.strftime('%d')
        self.bulan = self.bulanIndo(x.strftime('%B'))
        self.tahun = x.strftime('%Y')
        self.jam = x.strftime('%H')
        self.menit = x.strftime('%M')
        self.detik = x.strftime('%S')
       
    def hariIndo(self, day):
        daysKeys = list(days.keys()) #daftar indo
        daysValues = list(days.values()) #daftar eng 6
        # print(daysValues)
        if day.lower() in daysValues:
            artinya = daysKeys[daysValues.index(day.lower())]
            return artinya
        else:
            artinya = daysValues[daysKeys.index(day.lower())]
            return artinya

    def bulanIndo(self, month):
        monthKeys = list(months.keys()) #daftar indo
        monthValues = list(months.values()) #daftar eng 6
        # print(daysValues)
        if month.lower() in monthValues:
            artinya = monthKeys[monthValues.index(day.lower())]
            return artinya
        elif month.lower() in monthKeys:
            artinya = monthValues[monthKeys.index(day.lower())]
            return artinya
        else: return month

