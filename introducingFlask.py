from flask import Flask

app = Flask(__name__)

@app.rout('/')
def hello_flask()
	return "Hello Flask!"
