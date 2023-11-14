import json
import sqlite3
import ChangeValues
import UpdateDB
import Global
from time import sleep
from threading import Thread

TableDict = Global.TableDict
TableDict2 = Global.TableDict2
online = Global.online

# ask user if they wan to use a DB
DBChoice = Global.DBChoice
DBChoice = input('Do you want to connect/create a DB? (y/n): ')

if DBChoice == 'y':
    online = True
    # ask for db name
    DBName = input('Enter DB name (empty for default): ')
    if DBName.endswith('.db'):
        print('Thank you.')
    elif DBName == '':
        DBName = 'default.db'
        print('Thank you.')
    else:
        DBName = DBName + '.db'
        print('Thank you.')
    
    # connect to db
    con = Global.con = sqlite3.connect(DBName, check_same_thread=False)
    cur = Global.cur = con.cursor()
    
    cur.execute('PRAGMA foreign_keys = ON')
    # create tables if they don't exist
    cur.execute("CREATE TABLE IF NOT EXISTS Companies(ID INTEGER PRIMARY KEY AUTOINCREMENT, Name TEXT)")
    cur.execute("CREATE TABLE IF NOT EXISTS Warehouses(ID INTEGER PRIMARY KEY AUTOINCREMENT, CompanyID INTEGER, Name TEXT, Address TEXT, ZipCode TEXT, City TEXT, CountryCode TEXT, FOREIGN KEY (CompanyID) REFERENCES Companies(ID))")
    cur.execute("CREATE TABLE IF NOT EXISTS OpeningHours(ID INTEGER PRIMARY KEY AUTOINCREMENT, WarehouseID INTEGER, Weekday INTEGER, FromHours TEXT, ToHours TEXT, FOREIGN KEY (WarehouseID) REFERENCES Warehouses(ID))")
    con.commit()
    
    # Inserting DB info into TableDict
    cur.execute("SELECT * FROM Companies")
    TableDict['Companies'] = cur.fetchall()
    cur.execute("SELECT * FROM Warehouses")
    TableDict['Warehouses'] = cur.fetchall()
    cur.execute("SELECT * FROM OpeningHours")
    TableDict['OpeningHours'] = cur.fetchall()
    TableDict2 = TableDict
    
    # Inserting DB info into JSON file for backup
    with open('DBBackup.json', 'w') as f:
        json.dump(TableDict, f, indent=4)
        
elif DBChoice == 'n':
    online = False
    # ask for json file name
    DBImport = input('Enter JSON file name: ')
    if DBImport.endswith('.json'):
        print('Thank you.')
    else:
        DBImport = DBImport + '.json'
        print('Thank you.')
    # import json file
    with open(DBImport, 'r') as f:
        TableDict = json.load(f)
    TableDict2 = TableDict

else:
    print('Invalid input. Please try again.')
    exit()

# By now, we should have the data in a dictionary and json file.
# We can now start the program.
def menu():
    print('What option would you like to choose?')
    print('1. Change values')
    print('2. Add values')
    print('3. Delete values')
    print('4. Print values from DB')
    print('5. Print values from backup')
    print('6. Print values from dictionary')
    print('7. Update DB')
    print('8. Exit')

    Choice = input('Enter your choice: ')
    match Choice:
        case '1':
            ChangeValues.ChangeValues()
        case '2':
            ChangeValues.InsertValues()
        case '3':
            ChangeValues.DeleteValues()
        case '4':
            if online == True:
                cur.execute("SELECT * FROM Companies")
                print(cur.fetchall())
                cur.execute("SELECT * FROM Warehouses")
                print(cur.fetchall())
                cur.execute("SELECT * FROM OpeningHours")
                print(cur.fetchall())
            else:
                print('You are not connected to a DB.')
        case '5':
            with open('DBBackup.json', 'r') as f:
                print(json.load(f))
        case '6':
            print(TableDict)
        case '7':
            t1 = Thread(target=UpdateDB.Update)
            t1.start()
            t1.join()
        case '8':
            exit()

menu()