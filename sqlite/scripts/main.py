import json
import sqlite3
import ChangeValues
import UpdateDB
import Global

from time import sleep
from threading import Thread

TableDict = Global.TableDict
TableDict2 = Global.TableDict2

PATH = 'X:/sqlite/JSON/backup.json'
PATH_CHANGE = 'X:/sqlite/JSON/'

# ask user if they want to use a DB
DBChoice = Global.DBChoice
DBChoice = input('Do you want to connect/create a DB? (y/n): ')

if DBChoice == 'y':
    Global.online = True
    # ask for db name and format it correctly
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
    Global.con = sqlite3.connect('X:/sqlite/scripts/' + DBName, check_same_thread=False)
    con = Global.con
    Global.cur = con.cursor()
    cur = Global.cur
    # i'm really dumb so i made them local variables and ofcourse i'm too lazy to change them again
    # enable foreign keys
    cur.execute('PRAGMA foreign_keys = ON')
    # create tables if they don't exist
    cur.execute("CREATE TABLE IF NOT EXISTS Companies(ID INTEGER PRIMARY KEY AUTOINCREMENT, Name TEXT)")
    cur.execute("CREATE TABLE IF NOT EXISTS Warehouses(ID INTEGER PRIMARY KEY AUTOINCREMENT, CompanyID INTEGER, Name TEXT, Address TEXT, ZipCode TEXT, City TEXT, CountryCode TEXT, FOREIGN KEY (CompanyID) REFERENCES Companies(ID))")
    cur.execute("CREATE TABLE IF NOT EXISTS OpeningHours(ID INTEGER PRIMARY KEY AUTOINCREMENT, WarehouseID INTEGER, Weekday INTEGER, FromHours TEXT, ToHours TEXT, FOREIGN KEY (WarehouseID) REFERENCES Warehouses(ID))")
    con.commit()
    
    # Inserting DB info into TableDict
    cur.execute("SELECT * FROM Companies")
    Global.TableDict['Companies'] = cur.fetchall()
    cur.execute("SELECT * FROM Warehouses")
    Global.TableDict['Warehouses'] = cur.fetchall()
    cur.execute("SELECT * FROM OpeningHours")
    Global.TableDict['OpeningHours'] = cur.fetchall()
    Global.TableDict2 = Global.TableDict
    
elif DBChoice == 'n':
    Global.online = False
    # ask for json file name
    DBImport = input('Enter JSON file name: ')
    if DBImport.endswith('.json'):
        print('Thank you.')
    elif DBImport == '':
        DBImport = 'backup.json'
        print('Thank you.')
    else:
        DBImport = DBImport + '.json'
        print('Thank you.')
    # import json file into the dictionary
    with open(PATH_CHANGE + DBImport, 'r') as f:
        Global.TableDict = json.load(f)
    Global.TableDict2 = Global.TableDict

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
            t1 = Thread(target=ChangeValues.ChangeValues)
            t1.start()
            t1.join()
            t2 = Thread(target=menu)
            t2.start()
            t2.join()
        case '2':
            t1 = Thread(target=ChangeValues.InsertValues)
            t1.start()
            t1.join()
            
        case '3':
            t1 = Thread(target=ChangeValues.DeleteValues)
            t1.start()
            t1.join()
        case '4':
            if Global.online == True:
                print('========================================')
                cur.execute("SELECT * FROM Companies")
                print(cur.fetchall())
                cur.execute("SELECT * FROM Warehouses")
                print(cur.fetchall())
                cur.execute("SELECT * FROM OpeningHours")
                print(cur.fetchall())
                print('========================================')
                menu()
            else:
                print('You are not connected to a DB.')
                menu()
        case '5':
            print('========================================')
            with open('X:/sqlite/JSON/backup.json', 'r') as f:
                print(json.load(f))
            print('========================================')
            menu()
        case '6':
            print('========================================')
            print(Global.TableDict)
            print('========================================')
            menu()
        case '7':
            t1 = Thread(target=UpdateDB.Update)
            t1.start()
            t1.join()
            menu()
        case '8':
            exit()

menu()