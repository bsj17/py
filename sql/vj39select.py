import sqlite3

select_table_query =  '''SELECT * FROM Employees'''

database_name = 'Tvrtka.db'

lista_radnika = [
    ('Mate Matic','mmatic@gmail.com'),
    ('Ana Anic','aanic@hotmail.com'),
    ('Jure Juric','jjuric@brzi.hr')
]



try:
    sc = sqlite3.connect(database=database_name)
    cursor = sc.cursor()

    
    cursor.execute(select_table_query)
    records = cursor.fetchall()
    for record in records:
        print(record)

    cursor.close()
except sqlite3.Error as e:
    print ('greska: ',e)

finally:
    if sc:
        sc.close()

