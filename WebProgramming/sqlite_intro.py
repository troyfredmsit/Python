#sqlite DB function
import sqlite3

#create the database connection to non existant DB to create the db. This will also connect us if it does exist
conn = sqlite3.connect("tutorial.db")
#used for selecting and/or altering data
c = conn.cursor()

##Create table
def  create_table():
	#C is our cursor. Use all CAPS for SQL items, lower for non SQL CREATE TABLE, SELECT etc.
	#example is the name of the table to be created. the variables are the columns space and he SQL version of the data VARCHAR, REAL and TEXT
	c.execute("CREATE TABLE example(Language VARCHAR, Version REAL, Skill TEXT)")
create_table()
#close the db
conn.close()