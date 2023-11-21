import sqlite3

TableDict : dict = {}
TableDict2 : dict = {}
online : bool = False
api : bool = False
DBChoice = 'default'

con = sqlite3.connect('X:/sqlite/scripts/' + DBChoice + '.db', check_same_thread=False)
cur = con.cursor()

resp = None