from prettytable import PrettyTable
global tabel
tabel = PrettyTable()
tabel.field_names = ["Ukuran (Dalam Gram)","Brand","Harga (Dalam rupiah)"]
tabel.add_row(["120","Indomaret","18.000"])
tabel.add_row(["170","Ikan Pipih","35.000"])
tabel.add_row(["350","5 Bintang","80.000"])
tabel.add_row(["450","Dua Ikan","113.000"])
#pilih jadi pembeli atau admin
def pilih():
    masuk = input("Ingin masuk sebagai pembeli/admin : ")
    if masuk == "pembeli":
        pembeli ()
    elif masuk == "admin":
        operasi()
    else :
        print ("Input tidak valid")
        pilih()

def pembeli():
    global tabel
    print ("Selamat berbelanja")
    print (tabel)
    beliwoi = int (input ("Ukuran apa yag ingin anda beli?"))
    if beliwoi in tabel :
        berapa = int(input("Masukkan jumlah barang yang ingin dibeli"))
        if berapa <= tabel[beliwoi]["Stok"]:
            totalnya = berapa * tabel[beliwoi]["Harga"]
            print (totalnya)
        else :
            print ("Stok habis")
    else :
        print ("Barang tidak tersedia")
def admin():
    Nama_saya = input("Selamat datang di mode admin, silahkan masukkan nama")
    Paswort = input("Input password")
    if Nama_saya == "david sebastian sutandy" and Paswort == "hahaha":
        print ("Login berhasil")
        operasi ()
    else :
        print ("pasword/username salah")
        admin()
def operasi ():
    global tabel
    mauapa = input ("Apa yang ingin kamu lakukan create,read,update,delete")
    if mauapa == "create" :
        ukuran = int(input ("masukkan ukuran"))
        brand = (input ("masukkan jumlah stok"))
        editharga = int(input ("masukkan harga"))
        tabel.add_row([ukuran, brand , editharga])
        print (tabel)
        operasi()
    elif mauapa == "read" :
        from prettytable import PrettyTable
        print(tabel)
        operasi()
    elif mauapa == "update":
            print (tabel)
            beliwoi = (input("Masukkan ukuran berapa yang ingin diganti"))
            apasih = tabel.field_names.index("Ukuran (Dalam Gram)")
            rows_updetcok = False
            for row in tabel._rows:
                if row[apasih] == beliwoi:
                    editukuran = input("Masukkan ukuran baru: ")
                    editbrand = input("Masukkan brand baru: ")
                    editharga = input("Masukkan harga baru: ")
                    row[0]=editukuran
                    row[1]=editbrand
                    row[2]=editharga

                    rows_updatecok = True 
                if rows_updatecok : 
                    print (tabel)
                else :
                    print ("ukuran tidak tersedia")
                    
    elif mauapa == "delete":
        print (tabel)
        hapus = int(input("Masukkan baris ke berapa yang ingin dihapus"))
        tabel.del_row(hapus-1)
        print (tabel)
        operasi()
    else :
        print ("Input salah")
        operasi()
pilih()
