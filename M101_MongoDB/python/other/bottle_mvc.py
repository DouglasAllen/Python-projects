import bottle

@bottle.route('/')
def home_page():
	fruits = ['apple', 'orange', 'grape', 'kiwi']
	#return bottle.template('mytemplate', username= "Douglas", things = fruits)
	return bottle.template('mytemplate', {'username': "Douglas", 
	                                                       'things': fruits})
	
bottle.debug(True)
bottle.run(host = 'localhost',  port = 8082)	

#~ <! DOCTYPE html>
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
#~ </body>
#~ </html>