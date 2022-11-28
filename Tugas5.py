data = {}

print("Program Input Nilai")
print("====================")

while True:

    c = input("[(L)ihat, (T)ambah, (U)bah, (H)apus, (C)ari, (K)eluar] : ")

# EXIT PROGRAM
    if c.lower() == 'k':
        break

# PRINT DATA
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


# MENAMBAH DATA
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
                    print('Masukan TUGAS dengan Angka')
            except ValueError:
                print('Masukan TUGAS dengan Angka')
            else:
                break
        while (True):
            try:
                uts  = int(input("Nilai UTS     : "))
                if uts == '':
                    print('Masukan UTS dengan Angka')
            except ValueError:
                print('Masukan UTS dengan Angka')
            else:
                break
        while (True):
            try:
                uas  = int(input("Nilai UAS     : "))
                if uas == '':
                    print('Masukan UAS dengan Angka')
            except ValueError:
                print('Masukan UAS dengan Angka')
            else:
                break
        akhir = round((float(tugas) * 0.3)+(float(uts) * 0.35)+(float(uas) * 0.35),2)
        data[nama] = [nama, nim, tugas, uts, uas, akhir]

# EDIT DATA
    elif c.lower() == 'u':
        nama = input("Masukan nama untuk edit data : ")

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
                        print('Masukan TUGAS dengan Angka')
                except ValueError:
                    print('Masukan TUGAS dengan Angka')
                else:
                    break
            while (True):
                try:
                    uts = int(input("Nilai UTS     : "))
                    if uts == '':
                        print('Masukan UTS dengan Angka')
                except ValueError:
                    print('Masukan UTS dengan Angka')
                else:
                    break
            while (True):
                try:
                    uas = int(input("Nilai UAS     : "))
                    if uas == '':
                        print('Masukan UAS dengan Angka')
                except ValueError:
                    print('Masukan UAS dengan Angka')
                else:
                    break
            akhir = round((float(tugas) * 0.3) + (float(uts) * 0.35) + (float(uas) * 0.35), 2)
            data[nama] = [nama, nim, tugas, uts, uas, akhir]

        else:
            print("Data {} tidak ditemukan".format(nama))

# MENCARI DATA
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

# HAPUS DATA
    elif c.lower() == 'h':
        nama = input("Masukan nama untuk menghapus data : ")
        if nama in data.keys():
            del data[nama]
            print("Data {} dihapus".format(nama))
        else:
            print("Data {} tidak ditemukan".format(nama))
    else:
        print("")