import sqlite3
import main

con = main.con
cur = main.cur
TableDict = main.TableDict

def ChangeValues():

    wantedit = input('What values do you want to change? (1. Company/ 2. Warehouse/ 3. OpeningHours/ 4. Quit): ')
    # this time with an UI to make it easier to change values
    match(wantedit):
        case '1':
            x = input('What value do you want to change? (1. ID/ 2. Name/ 3. Quit): ')
            match(x):
                case '1':
                    x = input('What ID do you want to change to?: ')
                    TableDict[0][0] = x
                    TableDict[1][1] = x
                    print('ID changed to {ID}'.format(ID=x))
                    ChangeValues()
                case '2':
                    x = input('What name do you want to change to?: ')
                    TableDict[0][1] = x
                    print('Name changed to {Name}'.format(Name=x))
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
                    x = input('What ID do you want to change to?: ')
                    TableDict[1][0] = x
                    TableDict[2][1] = x
                    print('ID changed to {ID}'.format(ID=x))
                    ChangeValues()
                case '2':
                    x = input('What CompanyID do you want to change to?: ')
                    TableDict[1][1] = x
                    TableDict[0][0] = x 
                    print('CompanyID changed to {CompanyID}'.format(CompanyID=x))
                    ChangeValues()
                case '3':
                    x = input('What name do you want to change to?: ')
                    TableDict[1][2] = x
                    print('Name changed to {Name}'.format(Name=x))
                    ChangeValues()
                case '4':
                    x = input('What address do you want to change to?: ')
                    TableDict[1][3] = x
                    print('Address changed to {Address}'.format(Address=x))
                    ChangeValues()
                case '5':
                    x = input('What ZipCode do you want to change to?: ')
                    TableDict[1][4] = x
                    print('ZipCode changed to {ZipCode}'.format(ZipCode=x))
                    ChangeValues()
                case '6':
                    x = input('What City do you want to change to?: ')
                    TableDict[1][5] = x
                    print('City changed to {City}'.format(City=x))
                    ChangeValues()
                case '7':
                    x = input('What CountryCode do you want to change to?: ')
                    TableDict[1][6] = x
                    print('CountryCode changed to {CountryCode}'.format(CountryCode=x))
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
                    TableDict[2][0] = x
                    print('ID changed to {ID}'.format(ID=x))
                    ChangeValues()
                case '2':
                    x = input('What do you want to change WarehouseID to?: ')
                    TableDict[1][0] = x
                    TableDict[2][1] = x
                    print('WarehouseID changed to {WarehouseID}'.format(WarehouseID=x))
                    ChangeValues()
                case '3':
                    x = input('What Weekday do you want to change to?: ')
                    TableDict[2][2] = x
                    print('Weekday changed to {Weekday}'.format(Weekday=x))
                    ChangeValues()
                case '4':
                    x = input('What FromHours do you want to change to?: ')
                    TableDict[2][3] = x
                    print('FromHours changed to {FromHours}'.format(FromHours=x))
                    ChangeValues()
                case '5':
                    x = input('What ToHours do you want to change to?: ')
                    TableDict[2][4] = x
                    print('ToHours changed to {ToHours}'.format(ToHours=x))
                    ChangeValues()
                case '6':
                    print('Going back...')
                    ChangeValues()
                case _:
                    print('Invalid input, please try again...')
                    ChangeValues()
                    
        case '4':
            print('Quitting...')
            main.menu()
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
                    del TableDict[1][1]
                    del TableDict[0][0]
                    print('Deleted CompanyID.')
                    DeleteValues()
                case '2':
                    del TableDict[0][1]
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
                    del TableDict[1][0]
                    del TableDict[2][1]
                    print('Deleted WarehouseID.')
                    DeleteValues()
                case '2':
                    del TableDict[1][1]
                    del TableDict[0][0]
                    print('Deleted CompanyID.')
                    DeleteValues()
                case '3':
                    del TableDict[1][2]
                    print('Deleted WarehouseName.')
                    DeleteValues()
                case '4':
                    del TableDict[1][3]
                    print('Deleted Address.')
                    DeleteValues()
                case '5':
                    del TableDict[1][4]
                    print('Deleted ZipCode.')
                    DeleteValues()
                case '6':
                    del TableDict[1][5]
                    print('Deleted City.')
                    DeleteValues()
                case '7':
                    del TableDict[1][6]
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
                    del TableDict[2][0]
                    print('Deleted OpeningHoursID.')
                    DeleteValues()
                case '2':
                    del TableDict[1][0]
                    del TableDict[2][1]
                    print('Deleted WarehouseID.')
                    DeleteValues()
                case '3':
                    del TableDict[2][2]
                    print('Deleted Weekday.')
                    DeleteValues()
                case '4':
                    del TableDict[2][3]
                    print('Deleted FromHours.')
                    DeleteValues()
                case '5':
                    del TableDict[2][4]
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
            main.menu()
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
                        TableDict = {}
                        print('Deleted ALL values.')
                        DeleteValues()
                    else:
                        print('Going back...')
                        DeleteValues()
def InsertValues():
    x = input('What table do you want to insert values into? (1. Company/ 2. Warehouse/ 3. OpeningHours/ 4. Default Values/ 5. Quit): ')
    match x:
        case '1':
            x = input('What CompanyID do you want to insert?: ')
            TableDict['Companies'][1][0] = x
            x = input('What CompanyName do you want to insert?: ')
            TableDict['Companies'][1][1] = x
            print('Inserted values.')
            InsertValues()