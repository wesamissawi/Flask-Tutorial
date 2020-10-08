'''from flask import Flask

app = Flask(__name__) 


# We define url by routing with @ decorator... its called
# base url is /   just domain with nothing after
# deorator is like an if statement

@app.route('/')
def hello():
	return "Hello World"


# 
if __name__ == "__main__":  # if running direct from terminal...
	app.run(debug==True)

	# we want to turn on developer mode allows show errors and update server on the fly without stopping and starting server. '''