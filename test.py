from flask import Flask, jsonify
import chatterbot

app = Flask(__name__)

@app.route('/')
def samplefunction():
	
	
    #access your DB get your results here
	
	return "hello"

if __name__ == '__main__':
	
	
	app.run(host='0.0.0.0', debug=True, port=3134)
