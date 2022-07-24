


def pilihan_fitur(input_pilihan):
    if input_pilihan == 1:
        import pencarian_buku
    elif input_pilihan == 2:
        import pendaftaran_buku
    elif input_pilihan == 3:
        import pendaftaran_member
    elif input_pilihan == 4:
        import update_data_buku
    elif input_pilihan == 5:
        import update_data_member
    elif input_pilihan == 6:
        import peminjaman_buku
    elif input_pilihan == 7:
        import pengembalian_buku
    else:
        print('Anda salah memasukan data input')

def main():
    try:
        while True:
            print('-'*120)
            print('1. Pencarian Buku')
            print('2. Pendaftaran Buku Baru')
            print('3. Pendaftaran Member Baru')
            print('4. Update Data Buku')
            print('5. Update Data Member')
            print('6. Peminjaman Buku')
            print('7. Pengembalian Buku')
            print('-'*120)

            input_pilihan = int(input('Pilih menu yang ingin Anda gunakan: '))
            print('-'*120)
            pilihan_fitur(input_pilihan)

    except KeyboardInterrupt:
        pass
if __name__ == "__main__":
    main()

