import mysql.connector
from pandas import NamedAgg

def pendaftaran_member(id_m,nama,tgl_lahir,alamat,gender,email):
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='library',
                                             user='root',
                                             password='')
        cursor = connection.cursor()
        mySql_insert_query = """INSERT INTO members (id_m, nama, tgl_lahir, alamat, gender, email) 
                                VALUES (%s, %s, %s, %s, %s, %s) """

        record = (id_m, nama, tgl_lahir, alamat, gender, email)
        cursor.execute(mySql_insert_query, record)
        connection.commit()
        print("Data member baru telah sukses dimasukan ke dalam database")

    except mysql.connector.Error as error:
        print("Data member gagal dimasukan ke dalam database {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

id_m = int(input('Masukan ID Member : '))   
nama = input('Masukan Nama Member :')
tgl_lahir = input('Masukan Tanggal Lahir Member YYYY-MM-DD : ')
alamat = input('Masukan Alamat Member : ')
gender = input('Masukan Gender Member P/L : ')
email  = input('Masukan Email Member : ')

pendaftaran_member(id_m,nama,tgl_lahir,alamat,gender,email)