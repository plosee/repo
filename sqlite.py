import sqlite3
import os
import json
import time

# Change these values if you want to add new values to the tables
Company = {
    'ID' : 3,
    'Name' : 'Company3'
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

# Loading JSON file
LoadJSON = json.load(open('db1.json'))

# JSON data into list
Companies = LoadJSON['Companies']
Warehouses = LoadJSON['Warehouses']
OpeningHours = LoadJSON['OpeningHours']

# Create/connect existing database
con = sqlite3.connect('CompanyDB1.db')
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
        
        # check if time has changed
        if os.path.getmtime('db1.json') != prev_time:
            print('JSON file has changed, updating tables...')
            
            # make 3 lists from JSON data
            LoadJSON = json.load(open('db1.json'))
            Companies = LoadJSON['Companies']
            Warehouses = LoadJSON['Warehouses']
            OpeningHours = LoadJSON['OpeningHours']
            
            # update tables based on list data
            # IDs dont work for some reason
            cur.execute('UPDATE Companies SET Name = "{CompanyName}" WHERE ID = {CompanyID}'.format(CompanyID=Companies[0][0], CompanyName=Companies[0][1]))
            cur.execute('UPDATE Warehouses SET Name = "{WarehouseName}", CompanyID = "{CompanyID}" Address = "{WarehouseAddress}", ZipCode = "{WarehouseZipCode}", City = "{WarehouseCity}", CountryCode = "{WarehouseCountryCode}" WHERE ID = {WarehouseID}'.format(WarehouseID=Warehouses[0][0], CompanyID=Warehouses[0][1], WarehouseName=Warehouses[0][2], WarehouseAddress=Warehouses[0][3], WarehouseZipCode=Warehouses[0][4], WarehouseCity=Warehouses[0][5], WarehouseCountryCode=Warehouses[0][6]))
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
        # cur.execute('DELETE FROM Companies WHERE ID = 3')
        # cur.execute('DELETE FROM Warehouses')
        # cur.execute('DELETE FROM Companies')
        con.commit()
    except:
        print("Tables doesn't have any values that match the selection, skipping...")
        pass

# Updating values
# TODO: Update when JSON file is updated
def ChangeValues():
    print('Changing values in tables...')
    try:
        # cur.execute('UPDATE Companies SET Name = "Company3" WHERE ID = 3')
        # cur.execute('UPDATE Warehouses SET Name = "Warehouse1", Address = "Address1", ZipCode = "ZipCode1", City = "City1", CountryCode = "CountryCode1" WHERE ID = 1')
        # cur.execute('UPDATE OpeningHours SET Weekday = 1, FromHours = "FromHours1", ToHours = "ToHours1" WHERE ID = 1')
        con.commit()
    except:
        print('No values to change, skipping...')
        pass
    
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
def OutputJson():
    print('Dumping info into JSON file...')
    cur.execute('SELECT * FROM Companies')
    companies = cur.fetchall()
    cur.execute('SELECT * FROM Warehouses')
    warehouses = cur.fetchall()
    cur.execute('SELECT * FROM OpeningHours')
    openinghours = cur.fetchall()
    
    # making a dictionary from the data to dump into json file
    data = {
        'Companies' : companies,
        'Warehouses' : warehouses,
        'OpeningHours' : openinghours
    }
    
    # dumping the data into json file with indent
    with open('db1.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)

if __name__ == '__main__':
    
    UpdateJSON()
    # AddValues()
    # DeleteValues()
    # ChangeValues()
    PrintTables()
    OutputJson()
    
