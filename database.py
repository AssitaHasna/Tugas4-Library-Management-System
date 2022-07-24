import mysql.connector
from mysql.connector import Error


# Membuat Koneksi Ke Server
nama_host = "localhost" # disesuaikan dengan nama komputer yang digunakan
user = "root" # disesuaikan dengan nama user yang digunakan 
password = "" # disesuaikan dengan password yang dibuat

myconn = mysql.connector.connect(host = nama_host, user = user, passwd = password, auth_plugin='mysql_native_password')

mycursor = myconn.cursor()

query_membuat_db = "CREATE DATABASE library"
mycursor.execute(query_membuat_db)

# Membuat Table Members
nama_host = "localhost" 
user = "root" 
password = "" # disesuaikan dengan password yang dibuat
db = "library"

mydb = mysql.connector.connect(host=nama_host, user=user, passwd=password, database=db)
mycursor = mydb.cursor()

query_membuat_tabel = """
CREATE TABLE members(
    id_m INT,
    nama VARCHAR(40),
    tgl_lahir DATE,
    alamat VARCHAR(60),
    gender VARCHAR (1),
    email VARCHAR(60),
    constraint members primary key(id_m)
);
"""
query_insert_data = """
INSERT INTO members VALUES(101, 'Jung Eunha', '1997-05-30', 'Seoul', 'P', 'eunhakiyowo@gmail.com'),
(102, 'Jeon Jungkook', '1997-09-01', 'Busan', 'L', 'jkjkhensem@gmail.com'),
(103, 'Lee Haechan', '2000-06-06', 'Jeju', 'L', 'haechanfulsun2gmail.com'),
(104, 'Min Yoongi', '1993-03-09', 'Daegu', 'L', 'geniusagustd@gmail.com'),
(105, 'Ran Takahashi', '2001-09-02', 'Kyoto', 'L', 'watashiranran@gmail.com');
"""

# mengeksekusi query
mycursor.execute(query_membuat_tabel)
mycursor.execute(query_insert_data)
mydb.commit()


# Membuat Table Buku
nama_host = "localhost" 
user = "root" 
password = "" # disesuaikan dengan password yang dibuat
db = "library"

mydb = mysql.connector.connect(host=nama_host, user=user, passwd=password, database=db)
mycursor = mydb.cursor()

query_membuat_tabelbuku = """
CREATE TABLE buku(
    id_b INT,
    judul VARCHAR(60),
    author VARCHAR(50),
    penerbit VARCHAR(60),
    kategori VARCHAR(60),
    stok INT,
    constraint buku primary key(id_b)
);
"""
query_insert_databuku = """
INSERT INTO buku VALUES(1001, 'Langit Bercerita', 'Ocean Belva', 'Rainbow Media', 'Fiksi', 3),
(1002, 'Python for Beginner', 'Richard Lee', 'Peron', 'Non Fiksi', 4),
(1003, 'Desert Recipe', 'John Wick', 'CFD', 'Non Fiksi', 2);
"""

# mengeksekusi query
mycursor.execute(query_membuat_tabelbuku)
mycursor.execute(query_insert_databuku)
mydb.commit()


# Membuat Table Transaksi
nama_host = "localhost" 
user = "root" 
password = "" # disesuaikan dengan password yang dibuat
db = "library"

mydb = mysql.connector.connect(host=nama_host, user=user, passwd=password, database=db)
mycursor = mydb.cursor()

query_membuat_tabeltransaction = """
CREATE TABLE transaction(
    id_tr INT,
    id_m INT,
    id_b INT,
    tgl_peminjaman DATE,
    tgl_pengembalian DATE,
    constraint transaction primary key(id_tr)
);
"""
query_insert_datatransaction= """
INSERT INTO transaction VALUES(1, 103, 1001, '2022-07-21', '2022-07-24'),
(2, 105, 1002, '2022-07-22', '2022-07-25');
"""

# mengeksekusi query
mycursor.execute(query_membuat_tabeltransaction)
mycursor.execute(query_insert_datatransaction)
mydb.commit()