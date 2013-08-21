import bottle

@bottle.route('/')
def home_page():
	fruits = ['apple', 'orange', 'grape', 'kiwi']
	#return bottle.template('mytemplate', username= "Douglas", things = fruits)
	return bottle.template('formtemplate', {'username': "Douglas", 
	                                                       'things': fruits})

@bottle.post('/favorite_fruit')
def favorite_fruit():
	fruit = bottle.request.forms.get("fruit")
	if (fruit == None or fruit == ""):
		fruit = "no fruit selected"
		
	return bottle.template('fruit_selection.tpl', {'fruit':fruit})
	
	
bottle.debug(True)
bottle.run(host = 'localhost',  port = 8082)	