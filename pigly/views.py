"""PIGLY"""

from flask import render_template,request,session,redirect,jsonify,Response
from flask import url_for
from pigly import app
import urllib2
import math
import json

@app.route('/', methods=['GET', 'POST'])
def land():
	return render_template("main.html")

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
			period = trans['transaction-time'][:7]
			if period == '2015-02' or period == '2015-03' and trans['amount'] < 0:
				amount += trans['amount']
		amount_list.append(-amount)
	cat_spends = dict()
	for i in range(len(catname_list)):
		cat_spends[catname_list[i]] = cat_spends.get(catname_list[i],0) + amount_list[i]
	return cat_spends

def _accounts(account_list):
	# print account_list
	accounts = json.loads(account_list)['accounts']
	ac_list = list()
	# for ac in accounts:
	# 	ac_list.append({'last-digits':ac['last-digits'], 
	# 					'balance': ac['balance'],
	# 					'account-type': ac['account-type']})
	# print ac_list
	for ac in accounts:
		ac_list.append((ac['last-digits'],ac['balance']));
	return ac_list

@app.route('/_fin_overview', methods=['GET', 'POST'])
def _fin_overview():
	accounts = request.args.get('accounts',0,type=str)
	# print "\n\n\n",accounts
	# acts = json.dumps(_accounts(accounts))
	return render_template('login.html', accounts=_accounts(accounts))
	# return acts

def _projected_transactions(proj_transaction_list):
	print proj_transaction_list
