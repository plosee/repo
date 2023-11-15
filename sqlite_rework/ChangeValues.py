import sqlite3
import Global
import UpdateDB

def ChangeValues():

    wantedit = input('What values do you want to change? (1. Company/ 2. Warehouse/ 3. OpeningHours/ 4. Quit): ')
    # this time with an UI to make it easier to change values
    
    # match case goes like this:
    # Ask for what table to change
    # Ask for what value type to change
    # Ask for what ID does the value come from
    
    # example: 
    # Companies -> ID/Name -> ID or Name ID
    match(wantedit):
        case '1':
            x = input('What value do you want to change? (1. ID/ 2. Name/ 3. Quit): ')
            match(x):
                case '1':
                    x = input('What ID do you want to change? (int): ')
                    y = input('What do you want to change it to?: ')
                    # [0] represents company [x-1] | represents ID (because index of name is 1) | [0] represents ID/Name aka value
                    Global.TableDict[0][x-1][0] = y
                    Global.TableDict[1][x-1][1] = y
                    print('ID changed to {ID}'.format(ID=y))
                    ChangeValues()
                case '2':
                    x = input('What ID do you want to change? (int): ')
                    y = input('What do you want to change it to?: ')
                    Global.TableDict[0][x-1][0] = y
                    print('Name changed to {Name}'.format(Name=y))
                    ChangeValues()
                case '3':
                    print('Going back...')
                    ChangeValues()
                case _:
                    print('Invalid input, please try again...')
                    ChangeValues()
                    
        case '2':
            match(input('What value do you want to change? (1. ID/ 2. CompanyID/ 3. Name/ 4. Address/ 5. ZipCode/ 6. City/ 7. CountryCode/ 8. Quit): ')):
                case '1':
                    x = input('What ID do you want to change? (int): ')
                    y = input('What do you want to change it to?: ')
                    Global.TableDict[1][x-1][0] = y
                    Global.TableDict[2][x-1][1] = y
                    print('ID changed to {ID}'.format(ID=y))
                    ChangeValues()
                case '2':
                    x = input('What ID do you want to change? (int): ')
                    y = input('What do you want to change it to?: ')
                    Global.TableDict[1][x-1][1] = y
                    Global.TableDict[0][x-1][0] = y
                    print('CompanyID changed to {CompanyID}'.format(CompanyID=y))
                    ChangeValues()
                case '3':
                    x = input('What ID do you want to change? (int): ')
                    y = input('What do you want to change it to?: ')
                    Global.TableDict[1][x-1][2] = y
                    print('Name changed to {Name}'.format(Name=y))
                    ChangeValues()
                case '4':
                    x = input('What ID do you want to change? (int): ')
                    y = input('What do you want to change it to?: ')
                    Global.TableDict[1][x-1][3] = y
                    print('Address changed to {Address}'.format(Address=y))
                    ChangeValues()
                case '5':
                    x = input('What ZipCode do you want to change to?: ')
                    y = input('What do you want to change it to?: ')
                    Global.TableDict[1][x-1][4] = y
                    print('ZipCode changed to {ZipCode}'.format(ZipCode=y))
                    ChangeValues()
                case '6':
                    x = input('What City do you want to change to?: ')
                    y = input('What do you want to change it to?: ')
                    Global.TableDict[1][x-1][5] = y
                    print('City changed to {City}'.format(City=y))
                    ChangeValues()
                case '7':
                    x = input('What CountryCode do you want to change to?: ')
                    y = input('What do you want to change it to?: ')
                    Global.TableDict[1][x-1][6] = y
                    print('CountryCode changed to {CountryCode}'.format(CountryCode=y))
                    ChangeValues()
                case '8':
                    print('Going back...')
                    ChangeValues()
                case _:
                    print('Invalid input, please try again...')
                    ChangeValues()
        case '3':
            match(input('What value do you want to change? (1. ID/ 2. WarehouseID/ 3. Weekday/ 4. FromHours/ 5. ToHours/ 6. Quit): ')):
                case '1':
                    x = input('What ID do you want to change to?: ')
                    y = input('What do you want to change it to?: ')
                    Global.TableDict[2][x-1][0] = y
                    print('ID changed to {ID}'.format(ID=y))
                    ChangeValues()
                case '2':
                    x = input('What do you want to change WarehouseID to?: ')
                    y = input('What do you want to change it to?: ')
                    Global.TableDict[2][x-1][1] = y
                    Global.TableDict[1][x-1][0] = y
                    print('WarehouseID changed to {WarehouseID}'.format(WarehouseID=y))
                    ChangeValues()
                case '3':
                    x = input('What Weekday do you want to change to?: ')
                    y = input('What do you want to change it to?: ')
                    Global.TableDict[2][x-1][2] = y
                    print('Weekday changed to {Weekday}'.format(Weekday=y))
                    ChangeValues()
                case '4':
                    x = input('What FromHours do you want to change to?: ')
                    y = input('What do you want to change it to?: ')
                    Global.TableDict[2][x-1][3] = y
                    print('FromHours changed to {FromHours}'.format(FromHours=y))
                    ChangeValues()
                case '5':
                    x = input('What ToHours do you want to change to?: ')
                    y = input('What do you want to change it to?: ')
                    Global.TableDict[2][x-1][4] = y
                    print('ToHours changed to {ToHours}'.format(ToHours=y))
                    ChangeValues()
                case '6':
                    print('Going back...')
                    ChangeValues()
                case _:
                    print('Invalid input, please try again...')
                    ChangeValues()
                    
        case '4':
            print('Quitting...')
            quit()
        case _:
            print('Invalid input, please try again...')
            ChangeValues()

def DeleteValues():
    x = input('From what table do you want to delete? (1. Company/ 2. Warehouse/ 3. OpeningHours/ 4. Quit/ 5. Delete ALL!): ')
    match x:
        case '1':
            x = input('What value do you want to delete? (1. ID/ 2. Name): ')
            match x:
                case '1':
                    x = input('What ID do you want to delete? (int): ')
                    del Global.TableDict[0][x-1][0]
                    del Global.TableDict[1][x-1][1]
                    print('Deleted CompanyID.')
                    DeleteValues()
                case '2':
                    x = input('What ID do you want to delete? (int): ')
                    del Global.TableDict[0][x-1][1] 
                    print('Deleted CompanyName.')
                    DeleteValues()
                case '3':
                    print('Going back...')
                    DeleteValues()
                case _:
                    print('Invalid input, please try again...')
                    DeleteValues()
        case '2':
            x = input('What value do you want to delete? (1. ID/ 2. CompanyID/ 3. Name/ 4. Address/ 5. ZipCode/ 6. City/ 7. CountryCode): ')
            match x:
                case '1':
                    x = input('What ID do you want to delete? (int): ')
                    del Global.TableDict[1][x-1][0] 
                    print('Deleted WarehouseID.')
                    DeleteValues()
                case '2':
                    x = input('What ID do you want to delete? (int): ')
                    del Global.TableDict[0][x-1][0] 
                    del Global.TableDict[1][x-1][1]
                    print('Deleted CompanyID.')
                    DeleteValues()
                case '3':
                    x = input('What ID do you want to delete? (int): ')
                    del Global.TableDict[0][x-1][0] 
                    print('Deleted WarehouseName.')
                    DeleteValues()
                case '4':
                    x = input('What ID do you want to delete? (int): ')
                    del Global.TableDict[0][x-1][0] 
                    print('Deleted Address.')
                    DeleteValues()
                case '5':
                    x = input('What ID do you want to delete? (int): ')
                    del Global.TableDict[0][x-1][0] 
                    print('Deleted ZipCode.')
                    DeleteValues()
                case '6':
                    x = input('What ID do you want to delete? (int): ')
                    del Global.TableDict[0][x-1][0] 
                    print('Deleted City.')
                    DeleteValues()
                case '7':
                    x = input('What ID do you want to delete? (int): ')
                    del Global.TableDict[0][x-1][0] 
                    print('Deleted CountryCode.')
                    DeleteValues()
                case '8':
                    print('Going back...')
                    DeleteValues()  
                case _:
                    print('Invalid input, please try again...')
                    DeleteValues()
        case '3':
            x = input('What value do you want to delete? (1. ID/ 2. WarehouseID/ 3. Weekday/ 4. FromHours/ 5. ToHours): ')
            match x:
                case '1':
                    x = input('What ID do you want to delete? (int): ')
                    del Global.TableDict[2][x-1][0] 
                    print('Deleted OpeningHoursID.')
                    DeleteValues()
                case '2':
                    x = input('What ID do you want to delete? (int): ')
                    del Global.TableDict[2][x-1][1]
                    del Global.TableDict[1][x-1][0] 
                    print('Deleted WarehouseID.')
                    DeleteValues()
                case '3':
                    x = input('What ID do you want to delete? (int): ')
                    del Global.TableDict[2][x-1][2]
                    print('Deleted Weekday.')
                    DeleteValues()
                case '4':
                    x = input('What ID do you want to delete? (int): ')
                    del Global.TableDict[2][x-1][3]
                    print('Deleted FromHours.')
                    DeleteValues()
                case '5':
                    x = input('What ID do you want to delete? (int): ')
                    del Global.TableDict[2][x-1][4]
                    print('Deleted ToHours.')
                    DeleteValues()
                case '6':
                    print('Going back...')
                    DeleteValues()
                case _:
                    print('Invalid input, please try again...')
                    DeleteValues()
        case '4':
            print('Quitting...')
            quit()
        case '5':
            x = input('Are you sure you want to delete ALL values? (y/n): ')
            if x == 'y':
                x = input('Are you REALLY sure you want to delete ALL values? (y/n): ')
            else:
                print('Going back...')
                DeleteValues()
                if x == 'y':
                    x = input('Are you REALLY REALLY sure you want to delete ALL values? (y/n): ')
                else:
                    print('Going back...')
                    DeleteValues()
                    if x == 'y':
                        print('Deleting ALL values...')
                        Global.TableDict = {}
                        print('Deleted ALL values.')
                        DeleteValues()
                    else:
                        print('Going back...')
                        DeleteValues()
def InsertValues():
    x = input('What table do you want to insert values into? (1. Company/Warehouse/OpeningHours | 2. Default Values (ONLY FOR FIRST TIME USE)/ 5. Quit): ')
    match x:
        case '1':
            print('Inserting values into Company table...')
            x1 = input('What ID do you want to insert? (int): ')
            x2 = input('What name do you want to insert? (str): ')
            Global.TableDict[0].append((x1,x2))
            
            print('Inserted values {x1} and {x2}.'.format(x1=x1,x2=x2))
            print('====================================================')
            print('Inserting values into Warehouse table...')
            
            x1 = input('What ID do you want to insert? (int): ')
            x2 = input('What CompanyID do you want to insert? (int): ')
            x3 = input('What name do you want to insert? (str): ')
            x4 = input('What address do you want to insert? (str): ')
            x5 = input('What ZipCode do you want to insert? (str): ')
            x6 = input('What City do you want to insert? (str): ')
            x7 = input('What CountryCode do you want to insert? (str): ')
            Global.TableDict[1].append((x1,x2,x3,x4,x5,x6,x7))
            
            print('Inserted values {x1}, {x2}, {x3}, {x4}, {x5}, {x6}, {x7}.'.format(x1=x1,x2=x2,x3=x3,x4=x4,x5=x5,x6=x6,x7=x7))
            print('====================================================')
            print('Inserting values into OpeningHours table...')
            
            x = input('What ID do you want to insert? (int): ')
            x = input('What WarehouseID do you want to insert? (int): ')
            x = input('What Weekday do you want to insert? (int): ')
            x = input('What FromHours do you want to insert? (str): ')
            x = input('What ToHours do you want to insert? (str): ')
            print('Inserted values.')
            InsertValues()
        case '2':
            # Default values
            Global.TableDict = {
                'Companies': (1, 'IKEA'),
                'Warehouses': (1, 1, 'IKEA', 'IKEAvej 1', '0000', 'IKEAby', 'DK'),
                'OpeningHours': (1, 1, 1, '00:00', '23:59')
            }
            
            print('Inserted default values.')
            UpdateDB.Update()