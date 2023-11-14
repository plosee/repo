import time
import main
import json

def Update():

    data = main.TableDict
    data2 = main.TableDict2
    con = main.con
    cur = main.cur
    
    while True:
        time.sleep(5)
        
        if data != data2:
            print('Updating DB...')
            # Inserting DB info into backup and TableDict
            if main.online == True:
                cur.execute("SELECT * FROM Companies")
                data['Companies'] = cur.fetchall()
                cur.execute("SELECT * FROM Warehouses")
                data['Warehouses'] = cur.fetchall()
                cur.execute("SELECT * FROM OpeningHours")
                data['OpeningHours'] = cur.fetchall()
            
                # Inserting DB info into JSON file for backup
                with open('backup.json', 'w') as f:
                    json.dump(data, f, iNDENT=4)
                
            else:
                # Inserting info from Dict to JSON
                with open('backup.json', 'w') as f:
                    json.dump(data, f, iNDENT=4)
                # Updating info from Dict to Dict2
                data2 = data
                print('DB updated.')