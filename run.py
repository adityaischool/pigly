#!flask/bin/python
from pigly import app
from pigly import views
app.config['Callback'] = 'http://localhost:5000/oauth2callback'
app.run(host='0.0.0.0', debug = True)