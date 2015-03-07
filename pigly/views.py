"""PIGLY"""

from flask import render_template,request,session,redirect,jsonify,Response
from flask import url_for
from pigly import app
import urllib2



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
	print "FLASK"
	print transaction_list


