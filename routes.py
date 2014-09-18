from flask import Flask,redirect, render_template

app = Flask(__name__)

@app.route('/')
def index():
	render_template('home.html')

if __name__ == '__main__':
	app.run(host='0.0.0.0', port='3187')