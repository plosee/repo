import time
import Global
import json

def Update():
    
    while True:
        time.sleep(5)
        
        if Global.TableDict != Global.TableDict2:
            print('Updating DB...')
            # Inserting DB info into backup and Global.TableDict
            if Global.online == True:
                # making data into tuples (????) why does it make it into tuples
                Companies = Global.TableDict['Companies']
                Warehouses = Global.TableDict['Warehouses']
                OpeningHours = Global.TableDict['OpeningHours']
            
                # print(Companies)
                # print(Warehouses)
                # print(OpeningHours)
                
                Global.cur.execute("SELECT * FROM Companies")
                z = Global.cur.fetchall()
                
                # check for missing table data
                if z != []:
                    Global.cur.execute('UPDATE Companies SET Name = "{CompanyName}" WHERE ID = {CompanyID}'.format(CompanyID=Companies[0], CompanyName=Companies[1]))
                    Global.cur.execute('UPDATE Warehouses SET Name = "{WarehouseName}", CompanyID = "{CompanyID}", Address = "{WarehouseAddress}", ZipCode = "{WarehouseZipCode}", City = "{WarehouseCity}", CountryCode = "{WarehouseCountryCode}" WHERE ID = {WarehouseID}'.format(WarehouseID=Warehouses[0], CompanyID=Warehouses[1], WarehouseName=Warehouses[2], WarehouseAddress=Warehouses[3], WarehouseZipCode=Warehouses[4], WarehouseCity=Warehouses[5], WarehouseCountryCode=Warehouses[6]))
                    Global.cur.execute('UPDATE OpeningHours SET WarehouseID = "{WarehouseID}", Weekday = "{Weekday}", FromHours = "{FromHours}", ToHours = "{ToHours}" WHERE ID = {OpeningHoursID}'.format(OpeningHoursID=OpeningHours[0], WarehouseID=OpeningHours[1], Weekday=OpeningHours[2], FromHours=OpeningHours[3], ToHours=OpeningHours[4]))
                    Global.con.commit()

                else:
                    Global.cur.execute('INSERT INTO Companies(ID, Name) VALUES("{CompanyID}", "{CompanyName}")'.format(CompanyID=Companies[0], CompanyName=Companies[1]))
                    Global.cur.execute('INSERT INTO Warehouses(ID, CompanyID, Name, Address, ZipCode, City, CountryCode) VALUES("{WarehouseID}", "{CompanyID}", "{WarehouseName}", "{WarehouseAddress}", "{WarehouseZipCode}", "{WarehouseCity}", "{WarehouseCountryCode}")'.format(WarehouseID=Warehouses[0], CompanyID=Warehouses[1], WarehouseName=Warehouses[2], WarehouseAddress=Warehouses[3], WarehouseZipCode=Warehouses[4], WarehouseCity=Warehouses[5], WarehouseCountryCode=Warehouses[6]))
                    Global.cur.execute('INSERT INTO OpeningHours(ID, WarehouseID, Weekday, FromHours, ToHours) VALUES("{OpeningHoursID}", "{WarehouseID}", "{Weekday}", "{FromHours}", "{ToHours}")'.format(OpeningHoursID=OpeningHours[0], WarehouseID=OpeningHours[1], Weekday=OpeningHours[2], FromHours=OpeningHours[3], ToHours=OpeningHours[4]))
                    Global.con.commit()
                    
                # Inserting DB info into JSON file for backup
                with open('backup.json', 'w') as f:
                    json.dump(Global.TableDict, f, indent=4)
                    
                print('DB updated with backup.')
                
                # Global.cur.execute("SELECT * FROM Companies")
                # print(Global.cur.fetchall())
                # Global.cur.execute("SELECT * FROM Warehouses")
                # print(Global.cur.fetchall())
                # Global.cur.execute("SELECT * FROM OpeningHours")
                # print(Global.cur.fetchall())
                
                # print(Global.TableDict)
                
            else:
                # Inserting info from Dict to JSON
                with open('backup.json', 'w') as f:
                    json.dump(Global.TableDict, f, indent=4)
                # Updating info from Dict to Dict2
                Global.TableDict2 = Global.TableDict
                print('Backup updated.')