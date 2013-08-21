import bottle

@bottle.route('/')
def home_page():
	return "<html><head><title></title></head><body>Hello World!\n</body></html>"

@bottle.route('/testpage')
def test_page():
	return "<html><head><title></title></head><body>This is a test page.\n</body></html>"
	
bottle.debug(True)
bottle.run(host = 'localhost',  port = 8082)	
#~ http://williams.best.vwh.net/sunrise_sunset_algorithm.htm
#~ http://blade.nagaokaut.ac.jp/cgi-bin/scat.rb/ruby/ruby-talk/264573
	