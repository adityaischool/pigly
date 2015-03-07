from urllib2 import Request, urlopen, URLError
from flask import session


def getUserExpenses(username):
	#hit api to get user getUserExpenses
	#group this months expenses by category- since no category yet, simply randomise data
	#return dictionary(categ1-100$,categ2-200$)