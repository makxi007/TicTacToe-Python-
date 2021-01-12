from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#CHANGE DATABASE NAME
#app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////db.db" 
#db = SQLAlchemy(app)


@app.route("/")
def main():
	return "<h1>Hello world</h1>"


@app.route("/file_hashes/")
def file_hashes():
	pass

@app.route("/file_hashes/{hash}")
def hash():
	pass


if __name__ == "__main__":
	#REMOVE DEBUG, than work will done
	app.run(host="localhost",port=3000,debug=True)