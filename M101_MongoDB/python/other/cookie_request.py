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
		
	bottle.response.set_cookie("fruit", fruit)
	bottle.redirect('show_fruit')
	
	
@bottle.route('/show_fruit')
def show_fruit():
	fruit = bottle.request.get_cookie("fruit")
	return bottle.template('fruit_selection.tpl', {'fruit':fruit})
	
bottle.debug(True)
bottle.run(host = 'localhost',  port = 8082)	

#~ <html>
#~ <head>
#~ <title>
#~ Hello World!
#~ </title>
#~ </head>
#~ <body>
#~ <p>
#~ Welcome {{username}}
#~ <p>
#~ <ul>
#~ %for thing in things:
#~ <li>{{thing}}</li>
#~ %end
#~ </ul>
#~ <p>
#~ <form action = "/favorite_fruit" method = "POST">
#~ What is your favorite fruit?
#~ <input type="text" name="fruit" size="40" value=""><br>
#~ <input type="submit" value="Submit">
#~ </form>
#~ </body>
#~ </html>

#~ <! DOCTYPE html>
#~ <html>
#~ <head>
#~ <title>
#~ Fruit Selection Confirmation
#~ </title>
#~ </head>
#~ <body>
#~ <p>
#~ <p>
#~ Your favorite fruit is {{fruit}}
#~ </body>
#~ </html>