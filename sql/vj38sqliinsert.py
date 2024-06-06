import sqlite3

insert_into_table_query =  '''INSERT INTO Employees (name,email)
                            values(?,?)'''

database_name = 'Tvrtka.db'

lista_radnika = [
    ('Mate Matic','mmatic@gmail.com'),
    ('Ana Anic','aanic@hotmail.com'),
    ('Jure Juric','jjuric@brzi.hr')
]



try:
    sc = sqlite3.connect(database=database_name)
    cursor = sc.cursor()

    for radnik in lista_radnika:
        cursor.execute(insert_into_table_query,radnik)
    
    sc.commit()
    cursor.close()
except sqlite3.Error as e:
    print ('greska: ',e)

finally:
    if sc:
        sc.close()
