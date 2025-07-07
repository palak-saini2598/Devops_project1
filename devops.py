from flask import Flask

devops=Flask(__name__)

@devops.route("/info")
def myinfo():
	return "i am Palak Saini"


@devops.route("/phone")
def myphone():
	return "1234567890"

devops.run(host="0.0.0.0")
