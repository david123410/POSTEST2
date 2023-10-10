![Untitled Diagram (3) drawio](https://github.com/david123410/POSTEST2/assets/144750420/0cb53a4b-d836-4a20-84d6-9c325666278c)
![image_2023-10-10_120858922](https://github.com/david123410/POSTEST2/assets/144750420/73ef6531-58c2-4a6f-ad32-7449fb8e7b5e)
ini output jika kita menjadi admin dan menggunakan read dan create hasilnya akan print tabel dan akan membuat baris baru 
![image_2023-10-10_121141218](https://github.com/david123410/POSTEST2/assets/144750420/cdf5ae3d-3de6-46eb-89bd-14cdee75081a)
ini output yang dihasilkan jika kita menggunakan update,baris yang dipilih isinya akan diganti dan diprint tabel yang baru
![image_2023-10-10_143316112](https://github.com/david123410/POSTEST2/assets/144750420/ca3a36a4-e1a0-4122-8ef5-8bb1c5400b31)
untuk pembeli milik saya belum jadi, saya sudah coba berbagai cara tapi tidak bisa menghasilkan output yang diinginkan :( 
# POSTEST2
Tugas postest david sebastian sutandy kedua
from prettytable import PrettyTable
global tabel
tabel = PrettyTable()
tabel.field_names = ["Ukuran (Dalam Gram)","Brand","Harga"]
tabel.add_row(["120","Indomaret","18000"])
tabel.add_row(["170","IkanPipih","35000"])
tabel.add_row(["350","5Bintang","80000"])

tabel.add_row(["450","DuaIkan","113000"])
#pilih jadi pembeli atau admin
def pilih():
    masuk = input("Ingin masuk sebagai pembeli/admin : ")
    if masuk == "pembeli":
        pembeli ()
    elif masuk == "admin":
        admin()
    else :
        print ("Input tidak valid")
        pilih()

def pembeli():
    global tabel
    print ("Selamat berbelanja")
    print (tabel)
    keranjang = []
    while True:
        masukan = input("barang apa yang mau dimasukkan ")
        for item in keranjang:
            print (item)
        break

def admin ():
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
        brand = (input ("masukkan jumlah brand"))
        harga = int(input ("masukkan harga"))
        tabel.add_row([ukuran, brand , harga])
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
            for row in tabel._rows:
                if row[apasih] == beliwoi:
                    editukuran = input("Masukkan ukuran baru: ")
                    editbrand = input("Masukkan brand baru: ")
                    editharga = input("Masukkan harga baru: ")
                    row[0]=editukuran
                    row[1]=editbrand
                    row[2]=editharga
                    print ("sudah diganti")
                    print (tabel)
                else :
                    print ("Ukuran tidak tersedia")
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
