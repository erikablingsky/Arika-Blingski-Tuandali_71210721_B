class Karyawan:
    _jenisKelamin = None
    _upahPerHari = None
    def __init__(self,n,u):
        self._nama = n
        self._umur = u
    def getNama(self):
        return self._nama
    def getUmur(self):
        return self._umur
    def getjenisKelamin(self):
        return self._jenisKelamin
    def getupahPerHari(self):
        return self._upahPerHari
    def setjenisKelamin(self,j):
        self._jenisKelamin = j
    def setupahPerHari(self,u):
        self._upahPerHari = u
    def printinfo(self):
        print("========= INFO =========")
        print("Nama             :",self.getNama())
        print("Umur             :",self.getUmur())
        print("Jenis Kelamin    :",self.getjenisKelamin())
        print("Upah per Hari    :",self.getupahPerHari())
    def hitungGajiBulanan(self,h):
        if self.getupahPerHari() == None:
            print("ERROR! Upah per Hari belum di inputkan")
        else:
            print("Gaji Bulanan :",self.getupahPerHari()*h)

orang1 = Karyawan("Haniff", 90)
orang1.printinfo()

orang2 = Karyawan("Sindu",190)
orang2.setjenisKelamin("Laki-laki")
orang2.setupahPerHari(30000)
orang2.printinfo()

orang1.hitungGajiBulanan(28)
orang2.hitungGajiBulanan(30)