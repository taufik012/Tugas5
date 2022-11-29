# Tugas Praktikum 5

## Program

Membuat program sederhana yang akan menampilkan daftar nilai Mahasiswa menggunakan **Dictionary**. Dengan menampilkan **Menu** (Tambah data, Ubah data, Hapus data, Tampilkan data, Cari data).

* Berikut Programnya :


**Flowchart**


![flowchart](https://user-images.githubusercontent.com/115480692/204458985-ecb2225f-63b2-47f0-afa3-9c50ffb6cbab.jpg)



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
        

### Output

![t](https://user-images.githubusercontent.com/115480692/204459335-8854ebe8-6e81-4cd2-92c3-f9e152b2d3aa.png)


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
            
### Output

![u](https://user-images.githubusercontent.com/115480692/204459462-e74e9ae9-620f-4376-8c2b-1aa05e989b1b.png)


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

### Output

![c](https://user-images.githubusercontent.com/115480692/204459545-b6edc09a-755d-47b4-a7df-5c1652152a47.png)



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


### Output

![h](https://user-images.githubusercontent.com/115480692/204459625-0c8e20d1-6032-4c98-a656-a40d614137e2.png)



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

### Output

![l](https://user-images.githubusercontent.com/115480692/204459696-ccd18ae6-38bc-420e-a2d6-9db9c87acd68.png)


## Keluar

* Jika memasukan huruf 'k' maka program akan berhenti

        if c.lower() == 'k':
        break

### Output

![k](https://user-images.githubusercontent.com/115480692/204459774-53ee7a43-fbf8-47d5-9a27-b381257bd9b5.png)

# Program selesai


