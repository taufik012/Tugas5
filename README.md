# Tugas Praktikum 5

## Program

Membuat program sederhana yang akan menampilkan daftar nilai Mahasiswa menggunakan **Dictionary**. Dengan menampilkan **Menu** (Tambah data, Ubah data, Hapus data, Tampilkan data, Cari data).

* Berikut Programnya :


**Flowchart**

# Penjelasan

* Deklarasi data Dictonary  data = {}

* Membuat perulangan while

    
    while True:

        c = input("[(L)ihat, (T)ambah, (U)bah, (H)apus, (C)ari, (K)eluar] : ")


## Menambah data

* Jika memasukan huruf 't' maka akan melakukan penambahan data

* Input nama, nim, tugas, uts, uas

* Jika nilai nim, tugas, uts, uas tidak di isi dengan angka maka value eror dan akan di minta input ulang

* nama sebagai key dan data yang lainnya value

    elif c.lower() == 't':
        print()

        while (True):
            nama = input("Nama          : ")
            if nama == '':
                print('Nama tidak boleh kosong')
            else:
                break
        while (True):
            try:
                nim = int(input("NIM           : "))
                if nim == '':
                    print('Masukan Nim dengan Angka')
            except ValueError:
                print('Masukan Nim dengan Angka')
            else:
                break
        while (True):
            try:
                tugas  = int(input("Nilai Tugas   : "))
                if tugas == '':
                    print('Masukan Nilai TUGAS dengan Angka')
            except ValueError:
                print('Masukan Nilai TUGAS dengan Angka')
            else:
                break
        while (True):
            try:
                uts  = int(input("Nilai UTS     : "))
                if uts == '':
                    print('Masukan Nilai UTS dengan Angka')
            except ValueError:
                print('Masukan Nilai UTS dengan Angka')
            else:
                break
        while (True):
            try:
                uas  = int(input("Nilai UAS     : "))
                if uas == '':
                    print('Masukan Nilai UAS dengan Angka')
            except ValueError:
                print('Masukan Nilai UAS dengan Angka')
            else:
                break
        akhir = round((float(tugas) * 0.3)+(float(uts) * 0.35)+(float(uas) * 0.35),2)
        data[nama] = [nama, nim, tugas, uts, uas, akhir]


## Mengubah data

* Jika memasukan huruf 'u' maka akan melakukan perubahan data

* Maka akan mngeinput nama/key yg ingin di ubah

* Jika nama ada di data maka data bisa di ubah

* jika nama tidak ada di data maka data tidak di temukan dan meminta input ulang

    elif c.lower() == 'u':
        nama = input("Masukan nama untuk ubah data : ")

        if nama in data.keys():
            del data[nama]
            print("\nMasukan Pembaruan Data")

            while (True):
                nama = input("Nama          : ")
                if nama == '':
                    print('Nama tidak boleh kosong')
                else:
                    break
            while (True):
                try:
                    nim = int(input("NIM           : "))
                    if nim == '':
                        print('Masukan Nim dengan Angka')
                except ValueError:
                    print('Masukan Nim dengan Angka')
                else:
                    break
            while (True):
                try:
                    tugas = int(input("Nilai Tugas   : "))
                    if tugas == '':
                        print('Masukan Nilai TUGAS dengan Angka')
                except ValueError:
                    print('Masukan Nilai TUGAS dengan Angka')
                else:
                    break
            while (True):
                try:
                    uts = int(input("Nilai UTS     : "))
                    if uts == '':
                        print('Masukan Nilai UTS dengan Angka')
                except ValueError:
                    print('Masukan Nilai UTS dengan Angka')
                else:
                    break
            while (True):
                try:
                    uas = int(input("Nilai UAS     : "))
                    if uas == '':
                        print('Masukan Nilai UAS dengan Angka')
                except ValueError:
                    print('Masukan Nilai UAS dengan Angka')
                else:
                    break
            akhir = round((float(tugas) * 0.3) + (float(uts) * 0.35) + (float(uas) * 0.35), 2)
            data[nama] = [nama, nim, tugas, uts, uas, akhir]

        else:
            print("Data {} tidak ditemukan".format(nama))

## Mencari data

* Jika memasukan huruf 'c' maka akan melakukan pencarian data

* Maka akan menginput nama/key yang di cari

* jika nama ada di data maka data akan muncul

* jika nama tidak ada maka data tidak di temukan

    elif c.lower() == 'c':
        nama = input("Masukan nama yang di cari : ")
        if nama in data.keys():

            print("===========================================================================")
            print("| NO |      NAMA       |       NIM        | TUGAS |  UTS  |  UAS  | AKHIR |")
            print("===========================================================================")
            print("| {0:15} | {1:16} | {2:5} | {3:5} | {4:5} | {5:5} |".format(nama, data[nama][1], data[nama][2], data[nama][3], data[nama][4], data[nama][5]))
            print("===========================================================================")
        else:
            print("Data {} tidak ditemukan".format(nama))

## Menghapus data

* Jika memasukan huruf 'h' maka akan melakukan penghapusan data

* Maka akan menginput nama/key yang di cari

* lalu masukan nama yang ingin di hapus 

* maka data akan terhapus

    elif c.lower() == 'h':
    
        nama = input("Masukan nama untuk menghapus data : ")
        if nama in data.keys():
            del data[nama]
            print("Data {} dihapus".format(nama))
        else:
            print("Data {} tidak ditemukan".format(nama))
    else:
        print("")


## Melihat data

* Jika memasukan huruf 'l' maka akan menampilkan semua data

    elif c.lower() == 'l':

        print("Daftar Nilai")
        print("===========================================================================")
        print("| NO |      NAMA       |       NIM        | TUGAS |  UTS  |  UAS  | AKHIR |")
        print("===========================================================================")
        no = 1
        for tabel in data.values():
            print("|{0:3} | {1:15} | {2:16} | {3:5} | {4:5} | {5:5} | {6:5} |"
                  . format(no, tabel[0], tabel[1], tabel[2], tabel[3], tabel[4], tabel[5]))
            no += 1
        print("===========================================================================")


## Keluar

* Jika memasukan huruf 'k' maka program akan berhenti

        if c.lower() == 'k':
        break
