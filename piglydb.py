import sqlite3
from flask import g

def addUserGroupData():
	conn = sqlite3.connect("ace/dbase/piglymain.db")
	c = conn.cursor()
	objtoadd= [('john','pass'),('Tim','Student')]
	query='insert into users values (?,?)'
	c.executemany('insert into usermain values (?,?)',objtoadd)
	conn.commit()
	conn.close()

def addUserGroupTable():
	querytoExec="create table groupdata (groupid text not null,age text not null,location text not null,income text not null,cat1 text not null,cat2 text not null,cat3 text not null);"
	querytoExec2="create table users(useremail text not null, age text not null, location text not null, groupid text not null,income text not null,piggy text not null);"
	conn = sqlite3.connect("pigly/dbase/piglymain.db")
	c = conn.cursor()
	c.execute(querytoExec)
	c.execute(querytoExec2)
	conn.commit()
	conn.close()


if __name__ == '__main__':

	addUserGroupTable()
	

