from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home_page():
	return render_template("main_page.html")

@app.route("/contacts")
def contact_page():
	return render_template("main_page_contacts.html")

@app.route("/about")
def about_page():
	return render_template("main_page_about.html")

@app.route("/prog_lang")
def prog_lang():
	return render_template("main_page_proglang.html")

if __name__ == "__main__":
	app.debug = True
	app.env = "Working Hard, Playing Hard"
	app.run()