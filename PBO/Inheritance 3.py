# Inheritance / pewarisan 
# super class / parent class
class Manusia:
    #konstruktor 
    def __init__(self, nama, jk, usia):
        self.nama = nama 
        self.jk = jk 
        self.usia = usia 

    def info (self):
        print("Nama: {}\nJenis Kelamin: {}\nUsia: {}".format(self.nama, self.jk, self.usia))
        print("------------------------------")

    def makan(self): 
        print("Sedang makan nasi")
        print("------------------------------")

class Pelajar(Manusia): 
    #konsturktor anak 
    def __init__(self, nama, jk, usia, nis, nilai):
        Manusia.__init__(self, nama, jk, usia)
        self.nis = nis 
        self.nilai = nilai 

    def belajar(self):
        print("{} Sedang belajar".format(self.nama))
        print("------------------------------")

    #method overriding 
    def makan(self): 
        print("{} sedang sarapan pagi dengan roti".format(self.nama))
        print("------------------------------")

#sub class/child class
class Pekerja(Manusia):
    #konstruktor anak 
    def __init__(self, nama, jk, usia, nip, gaji):
        Manusia.__init__(self,  nama, jk, usia)
        self.nip = nip 
        self.gaji = gaji 

    def bekerja(self):
        print("{} sedang bekerja".format(self.nama))
        print("------------------------------")

# instansiasi objek 
Rudi = Pelajar("Rudianto", "laki-lai", 16, "15234", 90)
Wawan = Pekerja("Iwan", "laki-laki", 29, "1987463", 5000000)

#Pemangiilan 
Rudi.info()
Rudi.belajar()
Rudi.makan() #memanggil method anak
Wawan.info()
Wawan.bekerja()
Wawan.makan() #memanggil method induk 
