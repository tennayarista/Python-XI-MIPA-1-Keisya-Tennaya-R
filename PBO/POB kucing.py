class Kucing:
    '''Dasar kelas untuk semua kucing'''
    jumlah_kucing = 0 

    def __init__(self, nama, usia, namapakan, ras, riwayat_penyakit):
        self.nama = nama 
        self.usia = usia
        self.namapakan = namapakan
        self.ras = ras 
        self.riwayat_penyakit = riwayat_penyakit 
        Kucing.jumlah_kucing += 1

    def tampilkan_jumlah(self):
        print("Total kucing", Kucing.jumlah_kucing)

    def tampilkan_profil(self): 
        print("Nama :", self.nama)
        print("Usia :", self.usia)

    def tampilkan_infotambahan(self):
        print("Nama pakan :", self.namapakan)
        print("Ras :", self.ras)

    def tampilkan_infokesehatan(self):
        print("Riwayat penyakit: ", self.riwayat_penyakit)

#Membuat objek pertama dari kelas Kucing 
kucing1 = Kucing("Memei", "kitten", "bolt", "mixdom", "keracunan")
#Membuat objek kedua dari kelas Kucing 
kucing2 = Kucing("Hazel", "adult", "Maxi", "persmed", "scabies")
#Membuat objek ketiga dari kelas Kucing 
kucing3 = Kucing("Gombloh", "kitten", "Maxi", "domestic", "fraktura")

kucing1.tampilkan_profil()
kucing1.tampilkan_infotambahan()
kucing1.tampilkan_infokesehatan()
kucing2.tampilkan_profil()
kucing2.tampilkan_infotambahan()
kucing2.tampilkan_infokesehatan()
kucing3.tampilkan_profil()
kucing3.tampilkan_infokesehatan()
print("Total kucing :", Kucing.jumlah_kucing)