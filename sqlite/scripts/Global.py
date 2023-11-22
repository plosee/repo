import sqlite3

# primary and secondary check
TableDict : dict = {}
TableDict2 : dict = {}

# online and api check. used to make some actions available or not for less processing and more confusion 
# api check, no clue if it's used anywhere
online : bool = False
api : bool = False

# default db name
DBChoice = 'default'

# sqlite
con = sqlite3.connect('X:/sqlite/scripts/' + DBChoice + '.db', check_same_thread=False)
cur = con.cursor()

# response flask
resp = None

# probably deprecated and have no use anymore
# but i'm too scare to remove them
InsertData = True
UpdateData = True
DeleteData = True