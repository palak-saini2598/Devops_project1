from flask import Flask

app=Flask(__name__)

@app.route("/info")
def myinfo():
	return "i am Palak Saini"


@app.route("/phone")
def myphone():
	return "1234567890"

app.run(host="0.0.0.0")