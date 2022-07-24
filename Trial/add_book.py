import mysql.connector
def add_book():
  conn = mysql.connector.connect(
       host='localhost', database='library', user='root', password='Munjaemah21')
  cursor = conn.cursor()

  title = input('Enter Book Title :')
  author = input('Enter Book Author : ')
  publisher = input('Enter Book Publisher : ')
  pages = input('Enter Book Pages : ')
  price = input('Enter Book Price : ')
  edition = input('Enter Book Edition : ')
  copies  = int(input('Enter copies : '))
  sql = 'insert into book(title,author,price,pages,publisher,edition,status) values ( "' + \
       title + '","' + author+'",'+price+','+pages+',"'+publisher+'","'+edition+'","available");'
   #sql2 = 'insert into transaction(dot,qty,type) values ("'+str(today)+'",'+qty+',"purchase");'
  #print(sql)
  for _ in range(0,copies):
    conn = mysql.connector.connect(
       host='localhost', database='library', user='root', password='Munjaemah21')
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.close()
    print('\n\nNew Book added successfully')
    wait = input('\n\n\n Press any key to continue....')