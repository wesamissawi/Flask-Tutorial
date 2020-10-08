from flask import Flask

app = Flask(__name__) 


# We define url by routing with @ decorator... its called
# base url is /   just domain with nothing after
# decorator is like an if statement

@app.route('/')
# @app.route('/home')  # in case we want to add hello() to both routes / and home... add decorator to add add more stuff
@app.route('/home')
def hello():
	return "Hello Home"



# getting stuff from url into our code  
@app.route('/intro/<string:name>')
def hello2(name):
	return "Hello "+ name

@app.route('/image/<int:image_id>')
def hello3(image_id):
	pass  # do some image stuff here

# 
if __name__ == "__main__":  # if running direct from terminal...
	app.run(debug=True)

	# we want to turn on developer mode allows show errors and update server on the fly without stopping and starting server. 