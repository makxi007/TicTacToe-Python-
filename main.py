from flask import Flask
from flask_sqlalchemy import SQLAlchemy




app = Flask(__name__)
#CHANGE DATABASE NAME
#app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////db.db" 
#db = SQLAlchemy(app)


@app.route("/")
def main():
	return "<h1>Hello world</h1>"


if __name__ == "__main__":
	app.run(host="localhost",port=3000,debug=True)