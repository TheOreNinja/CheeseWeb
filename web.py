import bottle
@bottle.route('/')
def index():
	x='it works'
	return bottle.template('pig')

bottle.run(host='localhost', port=8337)
@bottle.route('/Login')
def index():
	x='it works'
	return bottle.template('cow')
