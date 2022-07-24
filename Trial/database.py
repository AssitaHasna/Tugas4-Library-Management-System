import mysql.connector
from mysql.connector import Error


# Membuat Koneksi Ke Server
nama_host = "localhost" # disesuaikan dengan nama komputer yang digunakan
user = "root" # disesuaikan dengan nama user yang digunakan 
password = "Munjaemah21" # disesuaikan dengan password yang dibuat

myconn = mysql.connector.connect(host = nama_host, user = user, passwd = password, auth_plugin='mysql_native_password')

mycursor = myconn.cursor()

query_membuat_db = "CREATE DATABASE library"
mycursor.execute(query_membuat_db)

# Membuat Table Members
nama_host = "localhost" 
user = "root" 
password = "Munjaemah21" 
db = "library"

mydb = mysql.connector.connect(host=nama_host, user=user, passwd=password, database=db)
mycursor = mydb.cursor()

query_membuat_tabel = """
CREATE TABLE members(
    id INT,
    name VARCHAR(30),
    class VARCHAR(15),
    address VARCHAR(100),
    phone VARCHAR (15),
    email VARCHAR(60),
    constraint members primary key(id)
);
"""
query_insert_data = """
INSERT INTO members VALUES(101, 'Jung Eunha', '1', 'Seoul', '1111111', 'eunhakiyowo@gmail.com'),
(102, 'Jeon Jungkook', '2', 'Busan', '2222222', 'jkjkhensem@gmail.com'),
(103, 'Lee Haechan', '1', 'Jeju', '3333333', 'haechanfulsun2gmail.com'),
(104, 'Min Yoongi', '2', 'Daegu', '4444444', 'geniusagustd@gmail.com'),
(105, 'Ran Takahashi', '1', 'Kyoto', '55555555', 'watashiranran@gmail.com');
"""

# mengeksekusi query
mycursor.execute(query_membuat_tabel)
mycursor.execute(query_insert_data)
mydb.commit()


# Membuat Table Buku
nama_host = "localhost" 
user = "root" 
password = "Munjaemah21" 
db = "library"

mydb = mysql.connector.connect(host=nama_host, user=user, passwd=password, database=db)
mycursor = mydb.cursor()

query_membuat_tabelbook = """
CREATE TABLE book(
    id INT,
    title VARCHAR(60),
    author VARCHAR(50),
    pages INT,
    price FLOAT(6,2),
    status VARCHAR (10),
    publisher VARCHAR(60),
    edition VARCHAR(15),
    constraint book primary key(id)
);
"""
query_insert_databook = """
INSERT INTO book VALUES(1001, 'Langit Bercerita', 'Ocean Belva', 60, 6500, 'available', 'Rainbow Media', '3'),
(1002, 'Python for Beginner', 'Richard Lee', 70, 7500, 'available', 'Peron', '4'),
(1003, 'Desert Recipe', 'John Wick', 80, 8700, 'available', 'CFD', '2');
"""

# mengeksekusi query
mycursor.execute(query_membuat_tabelbook)
mycursor.execute(query_insert_databook)
mydb.commit()


# Membuat Table Transaksi
nama_host = "localhost" 
user = "root" 
password = "Munjaemah21" 
db = "library"

mydb = mysql.connector.connect(host=nama_host, user=user, passwd=password, database=db)
mycursor = mydb.cursor()

query_membuat_tabeltransaction = """
CREATE TABLE transaction(
    tid INT,
    b_id INT,
    m_id INT,
    doi DATE,
    dor DATE,
    fine FLOAT(5,2),
    constraint transaction primary key(tid)
);
"""
query_insert_datatransaction= """
INSERT INTO transaction VALUES(1, 1001, 101, '2022-07-21', '2022-07-24', NOT NULL),
(2, 1002, 105, '2022-07-22', '2022-07-25', NOT NULL);
"""

# mengeksekusi query
mycursor.execute(query_membuat_tabeltransaction)
mycursor.execute(query_insert_datatransaction)
mydb.commit()