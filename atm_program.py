import random
import datetime
from customer import Customer

atm = Customer(id)

#looping pemeriksaan
while True:
    id = int(input("Masukkan PIN Anda: "))
    trial = 0
    while True:
        print("Selamat datang di ATM!")
        print("\n1 - Cek Saldo \t 2 - Debet \t 3 - Simpan \t 4 - Ganti Pin \t 5 - Keluar ")
        selectmenu = int(input("\nSilakan pilih menu: "))
        if selectmenu == 1:
            print("\nSaldo Anda sekarang: Rp. " + str(atm.checkSaldo()) + "\n" )
        elif selectmenu == 2:
            nominal = float(input("Masukkan nominal saldo: "))
            verify_debet = input("Konfirmasi: Anda akan melakukan debet dengan nominal berikut? y/n " + str(nominal) + " ")
                
            if verify_debet == "y":
                print("Saldo awal Anda adalah: Rp. " + str(atm.checkSaldo()) +"")
            else:
                break
            if nominal < atm.checkSaldo():
                atm.debetSaldo(nominal)
                print("Transaksi debet berhasil!")
                print("Saldo Anda sekarang: Rp. " + str(atm.checkSaldo()) + "")
            else:
                print("Maaf. Saldo Anda tidak cukup untuk melakukan debet!")
                print("Silakan lakukan penambahan nominal saldo")
        elif selectmenu == 3:
            nominal = float(input("Masukkan nominal saldo: "))
            verify_deposit = input("Konfirmasi: Anda akan melakukan penyimpanan dengan nominal berikut? y/n " + str(nominal) + " ")

            if verify_deposit == "y":
                atm.depositSaldo(nominal)
                print("Saldo Anda sekarang adalah: Rp." + str(atm.checkSaldo()) + "\n" )
            else:
                break
        elif selectmenu == 4:
            verify_pin = int(input("Masukkan PIN Anda: "))

            while verify_pin != int(atm.checkPin()):
                print("PIN Anda salah, silakan masukkan PIN:")

            updated_pin = int(input("Silakan masukkan PIN baru: "))
            print("PIN Anda berhasil diganti!")

            verify_newpin = int(input("Coba masukkan PIN baru: "))

            if verify_newpin == updated_pin:
                print("PIN baru Anda sukses!")
            else:
                print("maaf, PIN Anda salah!")

        elif selectmenu == 5:
            print("Resi tercetak otomatis saat Anda keluar, \n Harap simpan tanda terima ini \n sebagai bukti transaksi Anda!")
            print("No. Rekord: ", random.randint(10000, 1000000))
            print("Tanggal: ", datetime.datetime.now())
            print("Saldo akhir: ", atm.checkSaldo())
            print("Terima kasih telah menggunakan ATM!")
            exit()
        else:
            print("Error, Maaf, menu tidak tersedia")

    #looping verifikasi
    while (id != int(atm.checkPin()) and trial < 3 ):
        id = int(input("PIN Anda salah. Silakan masukkan PIN Anda kembali."))
        trial += 1
        if trial == 3:
            print("Error. Silakan ambil kartu dan coba lagi!")
            exit()
