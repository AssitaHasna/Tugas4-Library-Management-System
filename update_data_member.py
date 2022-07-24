from turtle import clear
import mysql.connector
from pandas import NamedAgg



def show_data_members(id_m):
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='library',
                                             user='root',
                                             password='Munjaemah21')
        cursor = connection.cursor()
        sql_select_query = """select * from members where id_m = %s"""
        # set variable in query
        cursor.execute(sql_select_query, (id_m,))
        # fetch result
        record = cursor.fetchall()

        print('Menampilkan Data Members ') 
        print('-'*120)
        print('\n')

        for row in record:
            print("1. Id_m = ", row[0], )
            print("2. Nama = ", row[1])
            print("3. Tanggal Lahir = ", row[2])
            print("4. Alamat = ", row[3])
            print("5. Gender = ", row[4])
            print("6. Email = ", row[5], "\n")

    except mysql.connector.Error as error:
        print("Member yang Anda cari tidak ditemukan di dalam database {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            ask_ubah = input('Apakah Anda ingin mengubah record members? (y/n): ')
            if ask_ubah == 'y':
                ubah_record(id_m)

def ubah_record(id_m):
    members_update = int(input('\n Pilih record data yang ingin Anda ubah (no: 2 s/d 6): '))
    try:
        connection = mysql.connector.connect(host='localhost',
                                        database='library',
                                        user='root',
                                        password='')
        cursor = connection.cursor()
        if members_update == 1:
            print('Record yang Anda pilih tidak dapat diubah')
            show_data_members(id_m)
        elif members_update == 2:
            nama_baru = input('Masukan nama baru: ')
            sql_update_query = """Update members set nama = %s where id_m = %s"""
            input_data = (nama_baru, id_m)
        elif members_update == 3:
            tanggal_lahir_baru = input('Masukan tanggal lahir baru: ')
            sql_update_query = """Update members set tanggal lahir = %s where id_m = %s"""
            input_data = (tanggal_lahir_baru, id_m)
        elif members_update == 4:
            alamat_baru = input('Masukan alamat baru: ')
            sql_update_query = """Update members set alamat = %s where id_m = %s"""
            input_data = (alamat_baru, id_m)
        elif members_update == 5:
            gender_baru = input('Masukan gender baru: ')
            sql_update_query = """Update members set gender = %s where id_m = %s"""
            input_data = (gender_baru, id_m)
        elif members_update == 6:
            email_baru = input('Masukan nama email baru: ')
            sql_update_query = """Update members set email = %s where id_m = %s"""
            input_data = (email_baru, id_m)
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
            show_data_members(id_m)

def update_data_members(id_m):
    show_data_members(id_m)

id_m = int(input('Masukan ID members yang Anda cari: '))
update_data_members(id_m)


