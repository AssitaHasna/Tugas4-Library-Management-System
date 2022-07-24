from turtle import clear
import mysql.connector
from datetime import date

def peminjaman_buku(id_tr,id_m,id_b,tgl_peminjaman):
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='library',
                                             user='root',
                                             password='')
        cursor = connection.cursor()
        mySql_insert_query = """INSERT INTO transaction (id_tr, id_m, id_b, tgl_peminjaman) 
                                VALUES (%s, %s, %s, %s) """

        record = (id_tr,id_m,id_b,tgl_peminjaman)
        cursor.execute(mySql_insert_query, record)
        connection.commit()
        print("Data peminjaman buku telah sukses dimasukan ke dalam database")

    except mysql.connector.Error as error:
        print("Data peminjaman buku gagal dimasukan ke dalam database {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

id_tr = int(input('Masukan ID Transaction : '))   
id_m = input('Masukan ID Members :')
id_b = input('Masukan ID Buku : ')
tgl_peminjaman = input('Masukan Tanggal Peminjaman YYYY-MM-DD : ')

peminjaman_buku(id_tr,id_m,id_b,tgl_peminjaman)

