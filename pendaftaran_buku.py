import mysql.connector
from pandas import NamedAgg

def pendaftaran_buku(id_b,judul,author,penerbit,kategori,stok):
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='library',
                                             user='root',
                                             password='')
        cursor = connection.cursor()
        mySql_insert_query = """INSERT INTO buku (id_b, judul, author, penerbit, kategori, stok) 
                                VALUES (%s, %s, %s, %s, %s, %s) """

        record = (id_b, judul, author, penerbit, kategori, stok)
        cursor.execute(mySql_insert_query, record)
        connection.commit()
        print("Data buku baru telah sukses dimasukan ke dalam database")

    except mysql.connector.Error as error:
        print("Data buku gagal dimasukan ke dalam database {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

id_b = int(input('Masukan ID Buku : '))   
judul = input('Masukan Judul Buku :')
author = input('Masukan Author Buku : ')
penerbit = input('Masukan Penerbit Buku : ')
kategori = input('Masukan kategori Buku : ')
stok  = int(input('Masukan jumlah Buku : '))

pendaftaran_buku(id_b,judul,author,penerbit,kategori,stok)
