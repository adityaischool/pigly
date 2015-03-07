from urllib2 import Request, urlopen, URLError
import json
import datetime
from flask import session

#Main module to load UserData from Master

def getGroupData(usermail):
	conn = sqlite3.connect("app/dbase/hearstdata.db")
	c = conn.cursor()
	#	query='select login,passw,mappedteacher from loginclass'
	query2='select groupid from users where usermail =?'
	c.execute(query2,(usermail))
	results = [dict(groupid=row[0]) for row in c.fetchall()]
	print results
	#	table groupdata (groupid ,age ,location ,income ,cat1 ,cat2 ,cat3 );"
	#	useremail , age , location , groupid ,income );"
	query2='select groupid from users where usermail =?'
	c.execute(query2,(usermail))
	results = [dict(groupid=row[0]) for row in c.fetchall()]
	query2='select groupid ,age ,location ,income ,cat1 ,cat2 ,cat3 from groupdata where groupid =?'
	c.execute(query2,(results['groupid']))
	results2 = [dict(groupid=row[0],cat1=row[4],cat2=row[5],cat3=row[6]) for row in c.fetchall()] 
	
	return results2
	conn.close()

def compareData():
	usermail=session['username']
	#get group id for user
	#get group expenses by categ
	groupData=getGroupData(usermail)
	print results2
	#get user expenses by hitting api
	userExpenses=api.getUserExpenses(session['useremail'],groupData)
	userBalance=api.getUserBalance(session['useremail'])
	days=datetime.date.today().day
	
	#break dictionary into categ
	#get till day categ expenses
	#compare this wuth user expenses
	#recommend challenges
	# get wizard to compare expenses with 
	# if userBalance < 0 ; lock pig !!!

