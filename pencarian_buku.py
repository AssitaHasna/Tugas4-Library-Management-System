from turtle import clear
import mysql.connector
from pandas import NamedAgg
import main

def pencarian_buku(judul):
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='library',
                                             user='root',
                                             password='')
        cursor = connection.cursor()
        sql_select_query = """select * from buku where judul = %s"""
        # set variable in query
        cursor.execute(sql_select_query, (judul,))
        # fetch result
        search = cursor.fetchall()

        print('Menampilkan Data Buku ') 
        print('-'*120)
        print('\n')
        if search is None:
            print('Judul buku: '+judul+' tidak ditemukan di dalam database perpustakaan')
        else:
            for row in search:
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

judul = input('Masukan Judul Buku yang Anda cari: ')
pencarian_buku(judul)


