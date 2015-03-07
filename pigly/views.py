"""PIGLY"""

from flask import render_template,request,session,redirect,jsonify,Response
from flask import url_for
from pigly import app
import urllib2
import math

@app.route('/', methods=['GET', 'POST'])
def land():
	return render_template("login.html")



#AJAX - analytics dashboard 
@app.route('/_getAnalytics', methods=['GET', 'POST'])
def _getAnalytics():
	print "Inside analytics"
	time = json.loads(request.args.get('time'))
	timeperiod = "DAY"
	print "TIME VALUE =",time
	print timeperiod
	driverID = "default@default.com"
	val = travelManager.GetRides(driverID,time,timeperiod)
	return Response(json.dumps(val),mimetype='application/json')


@app.route('/_categories', methods=['GET', 'POST'])
def _transactions(transaction_list):
	transactions = json.loads(transaction_list)['transactions']
	cat_len = int(math.floor(len(transactions)*0.25))
	print cat_len
	cat_list = [transactions[:cat_len], transactions[cat_len:cat_len*2], transactions[cat_len*2:cat_len*3], transactions[cat_len*3:]]
	amount_list = list()
	catname_list = ['Food and Drinks', 'Travel', 'Electronics', 'Clothes and Shoes']
	for transactions in cat_list:
		amount = 0
		for trans in transactions:
			if trans['transaction-time'][:7] == '2015-03' and trans['amount'] < 0:
				amount += trans['amount']
		amount_list.append(-amount)
	cat_spends = dict()
	for i in range(len(catname_list)):
		cat_spends[catname_list[i]] = cat_spends.get(catname_list[i],0) + amount_list[i]
	return cat_spends
	




