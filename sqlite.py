import sqlite3
import os
import json
import time
from threading import Thread

# Change these values if you want to add new values to the tables
Company = {
    'ID' : 1,
    'Name' : 'Company1'
}

Warehouses = {
    'ID' : 1,
    'CompanyID' : 1,
    'Name' : 'Warehouse1',
    'Address' : 'Address1',
    'ZipCode' : 'ZipCode1',
    'City' : 'City1',
    'CountryCode' : 'CountryCode1'
}

OpeningHours = {
    'ID' : 1,
    'WarehouseID' : 1,
    'Weekday' : 1,
    'FromHours' : 'FromHours1',
    'ToHours' : 'ToHours1'
}

data = ''

# Create/connect existing database
con = sqlite3.connect('CompanyDB1.db', check_same_thread=False)
cur = con.cursor()

# Enable FK constraints
cur.execute('PRAGMA foreign_keys = ON')

print('Creating tables...')
cur.execute("CREATE TABLE IF NOT EXISTS Companies(ID INTEGER PRIMARY KEY AUTOINCREMENT, Name TEXT)")
cur.execute("CREATE TABLE IF NOT EXISTS Warehouses(ID INTEGER PRIMARY KEY AUTOINCREMENT, CompanyID INTEGER, Name TEXT, Address TEXT, ZipCode TEXT, City TEXT, CountryCode TEXT, FOREIGN KEY (CompanyID) REFERENCES Companies(ID))")
cur.execute("CREATE TABLE IF NOT EXISTS OpeningHours(ID INTEGER PRIMARY KEY AUTOINCREMENT, WarehouseID INTEGER, Weekday INTEGER, FromHours TEXT, ToHours TEXT, FOREIGN KEY (WarehouseID) REFERENCES Warehouses(ID))")

def UpdateJSON():
    print('Checking JSON file...')
    # cache a time value to check later
    prev_time = os.path.getmtime('db1.json')
    
    while True:
        print('tick...')
        time.sleep(5)
        print('tock...')
        time.sleep(5)
        
        # check if modification time has changed every 10 seconds
        if os.path.getmtime('db1.json') != prev_time:
            print('JSON file has changed, updating tables...')
            
            # make 3 lists from JSON data
            LoadJSON = json.load(open('db1.json'))
            Companies = LoadJSON['Companies']
            Warehouses = LoadJSON['Warehouses']
            OpeningHours = LoadJSON['OpeningHours']
            
            # update tables based on list data
            cur.execute('UPDATE Companies SET Name = "{CompanyName}" WHERE ID = {CompanyID}'.format(CompanyID=Companies[0][0], CompanyName=Companies[0][1]))
            cur.execute('UPDATE Warehouses SET Name = "{WarehouseName}", CompanyID = "{CompanyID}", Address = "{WarehouseAddress}", ZipCode = "{WarehouseZipCode}", City = "{WarehouseCity}", CountryCode = "{WarehouseCountryCode}" WHERE ID = {WarehouseID}'.format(WarehouseID=Warehouses[0][0], CompanyID=Warehouses[0][1], WarehouseName=Warehouses[0][2], WarehouseAddress=Warehouses[0][3], WarehouseZipCode=Warehouses[0][4], WarehouseCity=Warehouses[0][5], WarehouseCountryCode=Warehouses[0][6]))
            cur.execute('UPDATE OpeningHours SET WarehouseID = "{WarehouseID}", Weekday = "{Weekday}", FromHours = "{FromHours}", ToHours = "{ToHours}" WHERE ID = {OpeningHoursID}'.format(OpeningHoursID=OpeningHours[0][0], WarehouseID=OpeningHours[0][1], Weekday=OpeningHours[0][2], FromHours=OpeningHours[0][3], ToHours=OpeningHours[0][4]))
            
            con.commit()
            break

# Adding values to tables
def AddValues():
    try:
        print('Adding values to tables...')
        # cur.execute('INSERT INTO Companies VALUES({CompanyID},"{CompanyName}")'.format(CompanyID=Company['ID'], CompanyName=Company['Name']))
        # cur.execute('INSERT INTO Warehouses VALUES({WarehouseID},{CompanyID},"{WarehouseName}","{WarehouseAddress}","{WarehouseZipCode}","{WarehouseCity}","{WarehouseCountryCode}")'.format(WarehouseID=Warehouses['ID'], CompanyID=Company['ID'], WarehouseName=Warehouses['Name'], WarehouseAddress=Warehouses['Address'], WarehouseZipCode=Warehouses['ZipCode'], WarehouseCity=Warehouses['City'], WarehouseCountryCode=Warehouses['CountryCode']))
        # cur.execute('INSERT INTO OpeningHours VALUES({OpeningHoursID},{WarehouseID},{Weekday},"{FromHours}","{ToHours}")'.format(OpeningHoursID=OpeningHours['ID'], WarehouseID=Warehouses['ID'], Weekday=OpeningHours['Weekday'], FromHours=OpeningHours['FromHours'], ToHours=OpeningHours['ToHours']))
        con.commit()
    except:
        print("DB already has all values assigned, skipping...")
        pass

# Deleting values from tables
def DeleteValues():
    try:
        print('Deleting values from tables...')
        # cur.execute('DELETE FROM Companies')
        # cur.execute('DELETE FROM Warehouses')
        # cur.execute('DELETE FROM OpeningHours')
        con.commit()
    except:
        print("Tables doesn't have any values that match the selection, skipping...")
        pass

# Updating values
def ChangeValues():
    wantedit = input('What values do you want to change? (1. Company/2. Warehouse/3. OpeningHours): ')
    # this time with an UI to make it easier to change values
    match(wantedit):
        case '1':
            x = input('What value do you want to change? (1. ID/2. Name): ')
            match(x):
                case '1':
                    x = input('What ID do you want to change to?: ')
                    cur.execute('UPDATE Companies SET ID = {ID}'.format(ID=x))         # ID Constraint still applies, so it won't change
                    print('ID changed to {ID}'.format(ID=x))
                    ChangeValues()
                case '2':
                    x = input('What name do you want to change to?: ')
                    cur.execute('UPDATE Companies SET Name = "{Name}"'.format(Name=x))
                    print('Name changed to {Name}'.format(Name=x))
                    ChangeValues()
                case _:
                    print('Invalid input, please try again...')
                    ChangeValues()
                    
        case '2':
            match(input('What value do you want to change? (1. ID/2. CompanyID/3. Name/4. Address/5. ZipCode/6. City/7. CountryCode): ')):
                case '1':
                    x = input('What ID do you want to change to?: ')
                    cur.execute('UPDATE Warehouses SET ID = {ID}'.format(ID=x))
                    print('ID changed to {ID}'.format(ID=x))
                    ChangeValues()
                case '2':
                    x = input('What CompanyID do you want to change to?: ')
                    cur.execute('UPDATE Warehouses SET CompanyID = {CompanyID}'.format(CompanyID=x))
                    print('CompanyID changed to {CompanyID}'.format(CompanyID=x))
                    ChangeValues()
                case '3':
                    x = input('What name do you want to change to?: ')
                    cur.execute('UPDATE Warehouses SET Name = "{Name}"'.format(Name=x))
                    print('Name changed to {Name}'.format(Name=x))
                    ChangeValues()
                case '4':
                    x = input('What address do you want to change to?: ')
                    cur.execute('UPDATE Warehouses SET Address = "{Address}"'.format(Address=x))
                    print('Address changed to {Address}'.format(Address=x))
                    ChangeValues()
                case '5':
                    x = input('What ZipCode do you want to change to?: ')
                    cur.execute('UPDATE Warehouses SET ZipCode = "{ZipCode}"'.format(ZipCode=x))
                    print('ZipCode changed to {ZipCode}'.format(ZipCode=x))
                    ChangeValues()
                case '6':
                    x = input('What City do you want to change to?: ')
                    cur.execute('UPDATE Warehouses SET City = "{City}"'.format(City=x))
                    print('City changed to {City}'.format(City=x))
                    ChangeValues()
                case '7':
                    x = input('What CountryCode do you want to change to?: ')
                    cur.execute('UPDATE Warehouses SET CountryCode = "{CountryCode}"'.format(CountryCode=x))
                    print('CountryCode changed to {CountryCode}'.format(CountryCode=x))
                    ChangeValues()
                case _:
                    print('Invalid input, please try again...')
                    ChangeValues()
        case '3':
            match(input('What value do you want to change? (1. ID/2. WarehouseID/3. Weekday/4. FromHours/5. ToHours): ')):
                case '1':
                    x = input('What ID do you want to change to?: ')
                    cur.execute('UPDATE OpeningHours SET ID = {ID}'.format(ID=x))
                    print('ID changed to {ID}'.format(ID=x))
                    ChangeValues()
                case '2':
                    x = input('What WarehouseID do you want to change to?: ')
                    cur.execute('UPDATE OpeningHours SET WarehouseID = {WarehouseID}'.format(WarehouseID=x))
                    print('WarehouseID changed to {WarehouseID}'.format(WarehouseID=x))
                    ChangeValues()
                case '3':
                    x = input('What Weekday do you want to change to?: ')
                    cur.execute('UPDATE OpeningHours SET Weekday = {Weekday}'.format(Weekday=x))
                    print('Weekday changed to {Weekday}'.format(Weekday=x))
                    ChangeValues()
                case '4':
                    x = input('What FromHours do you want to change to?: ')
                    cur.execute('UPDATE OpeningHours SET FromHours = "{FromHours}"'.format(FromHours=x))
                    print('FromHours changed to {FromHours}'.format(FromHours=x))
                    ChangeValues()
                case '5':
                    x = input('What ToHours do you want to change to?: ')
                    cur.execute('UPDATE OpeningHours SET ToHours = "{ToHours}"'.format(ToHours=x))
                    print('ToHours changed to {ToHours}'.format(ToHours=x))
                    ChangeValues()
                case _:
                    print('Invalid input, please try again...')
                    ChangeValues()
                    
        case _:
            print('Invalid input, please try again...')
            ChangeValues()
            
    # cur.execute('UPDATE Companies SET Name = "Company3"')
    # cur.execute('UPDATE Warehouses SET Name = "Warehouse1", Address = "Address1", ZipCode = "ZipCode1", City = "City1", CountryCode = "CountryCode1"')
    # cur.execute('UPDATE OpeningHours SET Weekday = 1, FromHours = "FromHours1", ToHours = "ToHours1"')
    con.commit()

    
# Printing table data
def PrintTables():
    cur.execute('SELECT * FROM Companies')
    print('======Table 1=====')
    print(cur.fetchall())
    print('======Table 2=====')
    cur.execute('SELECT * FROM Warehouses')
    print(cur.fetchall())
    print('======Table 3=====')
    cur.execute('SELECT * FROM OpeningHours')
    print(cur.fetchall())

# Dumping info into json file
# def OutputJson():
#     print('Dumping info into JSON file...')
#     cur.execute('SELECT * FROM Companies')
#     companies = cur.fetchall()
#     cur.execute('SELECT * FROM Warehouses')
#     warehouses = cur.fetchall()
#     cur.execute('SELECT * FROM OpeningHours')
#     openinghours = cur.fetchall()
    
#     # making a dictionary from the data to dump into json file
#     datadict = {
#         'Companies' : companies,
#         'Warehouses' : warehouses,
#         'OpeningHours' : openinghours
#     }
    
#     # dumping the data into json file with indent
#     with open('db1.json', 'w') as json_file:
#         json.dump(data, json_file, indent=4)

def StringOutput():
    global data
    
    print('Putting all values into a string...')
    cur.execute('SELECT * FROM Companies')
    companies = cur.fetchall()
    cur.execute('SELECT * FROM Warehouses')
    warehouses = cur.fetchall()
    cur.execute('SELECT * FROM OpeningHours')
    openinghours = cur.fetchall()

    datadict = {
        'Companies' : companies,
        'Warehouses' : warehouses,
        'OpeningHours' : openinghours
    }
    
    data = str(datadict)
    print(data)
    
if __name__ == '__main__':

    t1 = Thread(target=ChangeValues)
    t2 = Thread(target=StringOutput)
    t1.start()
    t2.start()
    t1.join()
    t2.join()

    
    # AddValues()
    # DeleteValues()
    # ChangeValues()
    # PrintTables()
    # OutputJson()
    
    
    pass
