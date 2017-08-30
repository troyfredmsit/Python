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

#This is how you insert data
def enter_data():
	#same beginning. INSERT INTO is the sql to add data, Example is the table, 
	c.execute("INSERT INTO example VALUES('Python',2.7,'Beginner')")
	c.execute("INSERT INTO example VALUES('Python',3.4,'Intermediate')")
	c.execute("INSERT INTO example VALUES('Python',2.8,'Expert')")
	#basically saying commit this data/
	conn.commit()

def enter_dynamic_data():
	lang = input("What language? : ")
	version = float(input("What version? : "))
	skill = input("What skill level? :")

	# Complex insert. Example uses the designation of the columns Language etc, then the Values are ? variables and the corrosponding values are lang,version,skill
	c.execute("INSERT INTO example(Language, Version, Skill) VALUES (?,?,?)", (lang,version,skill))
	conn.commit()

def read_from_database():
	#sets up our variable
	what_skill = input("What skill are we looking for? :")
	what_lang = input("What language? :")

	#SQL command to select all data from the example table
	sql = "SELECT * FROM example WHERE Skill == ? AND Language = ?"

	for row in c.execute(sql, [(what_skill),(what_lang)]):# We launch our sql command using the ? with he ? = what_skill. could have been ?,? with what_skill,version
		print(row)
		print(row[0])

#Enter data
read_from_database()

#close the db
conn.close()

inp = input("")