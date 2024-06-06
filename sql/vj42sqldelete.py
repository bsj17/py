import sqlite3

delete_something_from_table_query =  '''DELETE from Employees where id=?'''

delete_evertything_from_table = '''DELETE FROM Employees'''

database_name = 'Tvrtka.db'




try:
    sc = sqlite3.connect(database=database_name)
    cursor = sc.cursor()

    #cursor.execute(delete_something_from_table_query,(1,))
    cursor.execute(delete_evertything_from_table)
    sc.commit()
    cursor.close()
except sqlite3.Error as e:
    print ('greska: ',e)

finally:
    if sc:
        sc.close()
