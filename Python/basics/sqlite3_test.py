#sqlite python

import sqlite3


def insertdata():
	conn = sqlite3.connect('test.db')
	curs = conn.cursor()
	curs.execute("insert into employee values( 'kuntal' , 53)")
	values=[('divangi', 29), ('shikha', 21 ), ('namrata', 51)]
	curs.executemany('insert into employee values(?, ?)', values)
	conn.commit()
	conn.close()

def accessdata():
	conn = sqlite3.connect('test.db')
	curs = conn.cursor()
	curs.execute("SELECT name, age FROM employee;")
	results = curs.fetchall()
	for r in results:
		print (r)
	conn.commit()
	conn.close()


accessdata()




