import time
import Global
import json
import sqlite3

# secondary check exists to check if the DB has been updated
# if secondary check doesn't line up with primary check, then it means that most likely db is outdated

def Update():
    # check if api is enabled
    if Global.api == True:
        # read the json file and store it in TableDict
        with open('X:/sqlite/JSON/backup.json', 'r') as f:
            Global.TableDict = json.load(f)
            
        # make sure that the secondary check is the same as the primary check
        Global.TableDict2 = Global.TableDict
        Global.online = True
    
    # if primary check doesn't match up with secondary check, update the DB
    if Global.TableDict != Global.TableDict2:
        print('Updating DB...', flush=True)
        # Inserting DB info into backup and Global.TableDict
        if Global.online == True:
            
            # Putting Dictionary data into temorary lists
            Companies = Global.TableDict['Companies']
            Warehouses = Global.TableDict['Warehouses']
            OpeningHours = Global.TableDict['OpeningHours']
            
            # Fetching data from the DB Tables
            Global.cur.execute("SELECT * FROM Companies")
            TableC = Global.cur.fetchall()
            Global.cur.execute('SELECT * FROM Warehouses')
            TableW = Global.cur.fetchall()
            Global.cur.execute('SELECT * FROM OpeningHours')
            TableO = Global.cur.fetchall()
            
            # check for missing table data
            # if company table data is empty, then most likely all tables are empty
            # so we insert all data from the dictionary into the DB
            if TableC != []:
                # iterate through the companies table data
                # in this case, we are checking the lists inside of it
                for List in Global.TableDict['Companies']:
                    # if the list is not in the table, insert it
                    # also it's really funky, sqlite loves tuples and outputs them as [(1, 'test')] (list of tuples)
                    if tuple(List) not in TableC:
                        Global.cur.execute('INSERT INTO Companies(ID, Name) VALUES("{CompanyID}", "{CompanyName}")'.format(CompanyID=List[0], CompanyName=List[1])) # List[0] is the ID, List[1] is the Name
                        
                for List in Global.TableDict['Warehouses']:
                    if tuple(List) not in TableW:
                        Global.cur.execute('INSERT INTO Warehouses(ID, CompanyID, Name, Address, ZipCode, City, CountryCode) VALUES("{WarehouseID}", "{CompanyID}", "{WarehouseName}", "{WarehouseAddress}", "{WarehouseZipCode}", "{WarehouseCity}", "{WarehouseCountryCode}")'.format(WarehouseID=List[0], CompanyID=List[1], WarehouseName=List[2], WarehouseAddress=List[3], WarehouseZipCode=List[4], WarehouseCity=List[5], WarehouseCountryCode=List[6]))
                        
                for List in Global.TableDict['OpeningHours']:
                    if tuple(List) not in TableO:
                        Global.cur.execute('INSERT INTO OpeningHours(ID, WarehouseID, Weekday, FromHours, ToHours) VALUES("{OpeningHoursID}", "{WarehouseID}", "{Weekday}", "{FromHours}", "{ToHours}")'.format(OpeningHoursID=List[0], WarehouseID=List[1], Weekday=List[2], FromHours=List[3], ToHours=List[4]))
                
            else:
                # only happens when db doesn't have any data
                # most likely bugridden execution. needs testing
                Global.cur.execute('INSERT INTO Companies(ID, Name) VALUES("{CompanyID}", "{CompanyName}")'.format(CompanyID=Companies[0], CompanyName=Companies[1]))
                Global.cur.execute('INSERT INTO Warehouses(ID, CompanyID, Name, Address, ZipCode, City, CountryCode) VALUES("{WarehouseID}", "{CompanyID}", "{WarehouseName}", "{WarehouseAddress}", "{WarehouseZipCode}", "{WarehouseCity}", "{WarehouseCountryCode}")'.format(WarehouseID=Warehouses[0], CompanyID=Warehouses[1], WarehouseName=Warehouses[2], WarehouseAddress=Warehouses[3], WarehouseZipCode=Warehouses[4], WarehouseCity=Warehouses[5], WarehouseCountryCode=Warehouses[6]))
                Global.cur.execute('INSERT INTO OpeningHours(ID, WarehouseID, Weekday, FromHours, ToHours) VALUES("{OpeningHoursID}", "{WarehouseID}", "{Weekday}", "{FromHours}", "{ToHours}")'.format(OpeningHoursID=OpeningHours[0], WarehouseID=OpeningHours[1], Weekday=OpeningHours[2], FromHours=OpeningHours[3], ToHours=OpeningHours[4]))
            # commiting at the end because otherwise it'll most likely throw an error
            Global.con.commit()
            
            # Inserting Dict into JSON file for backup
            with open('backup.json', 'w') as f:
                json.dump(Global.TableDict, f, indent=4)
                
            print('DB updated with backup.', flush=True) # flush=True | no clue how it works, i remember putting them into every print statement since it should've worked with flask but it didn't and i'm too lazy to remove them
            
            # making sure that the secondary check is the same as the primary check so that the program doesn't update the DB unnecessarily
            Global.TableDict2 = Global.TableDict
            
        else:
            # Inserting info from Dict to JSON
            with open('backup.json', 'w') as f:
                json.dump(Global.TableDict, f, indent=4)
                
            # Updating info from Dict to Dict2
            Global.TableDict2 = Global.TableDict
            
            print('Backup updated.', flush=True)