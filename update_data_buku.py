from turtle import clear
import mysql.connector
from pandas import NamedAgg



def show_data_buku(id_b):
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='library',
                                             user='root',
                                             password='')
        cursor = connection.cursor()
        sql_select_query = """select * from buku where id_b = %s"""
        # set variable in query
        cursor.execute(sql_select_query, (id_b,))
        # fetch result
        record = cursor.fetchall()

        print('Menampilkan Data Buku ') 
        print('-'*120)
        print('\n')

        for row in record:
            print("1. Id_b = ", row[0], )
            print("2. Judul = ", row[1])
            print("3. Author = ", row[2])
            print("4. Penerbit Buku = ", row[3])
            print("5. Kategori Buku = ", row[4], "\n")

    except mysql.connector.Error as error:
        print("Buku yang Anda cari tidak ditemukan di dalam database {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            ask_ubah = input('Apakah Anda ingin mengubah record data? (y/n): ')
            if ask_ubah == 'y':
                ubah_record(id_b)

def ubah_record(id_b):
    buku_update = int(input('\n Pilih record data yang ingin Anda ubah (no: 2 s/d 5): '))
    try:
        connection = mysql.connector.connect(host='localhost',
                                        database='library',
                                        user='root',
                                        password='Munjaemah21')
        cursor = connection.cursor()
        if buku_update == 1:
            print('Record yang Anda pilih tidak dapat diubah')
            show_data_buku(id_b)
        elif buku_update == 2:
            judul_baru = input('Masukan judul baru: ')
            sql_update_query = """Update buku set judul = %s where id_b = %s"""
            input_data = (judul_baru, id_b)
        elif buku_update == 3:
            author_baru = input('Masukan nama author baru: ')
            sql_update_query = """Update buku set author = %s where id_b = %s"""
            input_data = (author_baru, id_b)
        elif buku_update == 4:
            penerbit_baru = input('Masukan nama penerbit baru: ')
            sql_update_query = """Update buku set penerbit = %s where id_b = %s"""
            input_data = (penerbit_baru, id_b)
        elif buku_update == 5:
            kategori_baru = input('Masukan nama kategori baru: ')
            sql_update_query = """Update buku set kategori = %s where id_b = %s"""
            input_data = (kategori_baru, id_b)
        else:
            print('Anda salah memasukan data input')

        cursor.execute(sql_update_query, input_data)
        connection.commit()
        print("Record telah sukses diupdate ")
    except mysql.connector.Error as error:
        print("Gagal mengubah record: {}".format(error))
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            show_data_buku(id_b)

def update_data_buku(id_b):
    show_data_buku(id_b)

id_b = int(input('Masukan ID Buku yang Anda cari: '))
update_data_buku(id_b)


