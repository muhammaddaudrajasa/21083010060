print("          assalamualaikum shalom omswastiatustu namo budayya salam kebajikan        ")
print("---------------------- selamat datang di hasil panen kami ----------------------")
print("                               selamat mencoba                                  ")
# Program untuk menghitung hasil panen

while True:
  # Input luas lahan dalam hektar
  luas_lahan = float(input("Masukkan luas lahan (dalam hektar): "))

  # Input hasil per hektar dalam ton
  hasil_per_hektar = float(input("Masukkan hasil per hektar (dalam ton): "))

  # Input jumlah bulan
  jumlah_bulan = float(input("Masukkan jumlah bulan: "))


  # Meminta input dari user
  jumlah_tanaman = int(input("Berapa jumlah tanaman yang Anda miliki? "))
  # Meminta input dari pengguna untuk jenis tanaman yang dipanen
  jenis_tanaman = input("Masukkan jenis tanaman yang dipanen: ")
  jumlah_bibit_padi = int(input("Berapa jumlah bibit padi yang Anda tanam? "))
  jumlah_bibit_jagung = int(input("Berapa jumlah bibit jagung yang Anda tanam? "))

  # Menghitung jumlah hasil panen tanaman padi
  hasil_panen_padi = luas_lahan * hasil_per_hektar * jumlah_bulan * jumlah_bibit_padi / jumlah_tanaman

  # Hitung hasil panen tanaman jagung
  hasil_panen_jagung= luas_lahan * hasil_per_hektar * jumlah_bulan * jumlah_bibit_jagung / jumlah_tanaman

  #Tampilkan hasil panen
  print("Hasil panen padi: ", str(int( hasil_panen_padi)), "ton")

  #Tampilkan hasil panen
  print("Hasil panen jagung: ", str(int( hasil_panen_jagung)), "ton")

  # Hitung hasil panen
  hasil_panen = hasil_panen_jagung + hasil_panen_padi

  #Tampilkan hasil panen
  print("Hasil panen semuanya: ", str(int( hasil_panen)), "ton")


  # Inisialisasi variabel untuk menyimpan hasil panen
  hasil = " ton "

  ulangi = input("Apakah Anda ingin mengulang program ini? (y/n)")
  if ulangi.lower() == 'y':
    continue
  elif ulangi.lower() == 'n':
    break
  else:
    print("Masukkan y atau n")
