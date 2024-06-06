import sqlite3

select_query = "SELECT sqlite_version();"

try:
    sqliteConnection = sqlite3.connect('SQLite_Python.db')

    cursor = sqliteConnection.cursor()
    print('spojeni smo na bazu')

    cursor.execute(select_query)

    records = cursor.fetchall()
    
    print('Sqlite verzija: ',records[0])

    cursor.close()
except Exception as e:
    print('greska je:',e)


finally:
    if sqliteConnection:
        sqliteConnection.close()
        print("zatvorena konekcija na bazu")