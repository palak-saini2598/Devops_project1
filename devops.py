from flask import Flask

devops = Flask(__name__)

@devops.route("/info")
def myinfo():
    return "i am Palak Saini"

@devops.route("/phone")
def myphone():
    return "1234567890"

print("This is my LOCAL version")
print("This is the REMOTE version on GitHub")

devops.run(host="0.0.0.0")
