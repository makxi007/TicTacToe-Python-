from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///articles.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

class Articles(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(100), nullable=False)
	intro = db.Column(db.String(300), nullable=False)
	text = db.Column(db.Text, nullable=False)
	date = db.Column(db.DateTime, default=datetime.utcnow)

	def __repr__(self):
		return "<Article %r>" % self.id

@app.route("/")
def main_page():
	articles = Articles.query.order_by(Articles.date.desc())

	page = request.args.get("page")
	if page:
		page = int(page)
	else:
		page = 1

	pages = articles.paginate(page=page,per_page=1)
	return render_template("main_page.html", articles=articles, pages=pages)
'''
@app.route("/articles")
def articles():

	page = request.args.get("page")
	if page and page.isdigit():
		page = int(page)
	else:
		page = 1

	articles = Articles.query.order_by(Articles.date.desc())#.all()

	pages = articles.paginate(page=page, per_page=2)

	return render_template("articles_page.html", articles=articles, pages=pages)
'''
@app.route("/create_article", methods=["POST", "GET"])
def create_article():
	if request.method == "POST":
		title = request.form['title']
		intro = request.form['intro']
		text = request.form['text']

		article = Articles(title=title, intro=intro, text=text)

		try:
			db.session.add(article)
			db.session.commit()
			return redirect(url_for("main_page"))
		except:
			return redirect(url_for("error_page"))

	else:
		return render_template("create_article.html")

@app.route("/articles/<int:id>")
def article_details(id):
	article = Articles.query.get(id)
	return render_template("articles_details_page.html", article=article)

@app.route("/articles/<int:id>/delete")
def articles_delete(id):
	article = Articles.query.get_or_404(id)

	try:
		db.session.delete(article)
		db.session.commit()
		return redirect(url_for("main_page"))
	except:
		return redirect(url_for("error_page"))

@app.route("/articles/<int:id>/update", methods=["POST", "GET"])
def article_update(id):
	article = Articles.query.get(id)
	if request.method == "POST":
		article.title = request.form['title']
		article.intro = request.form['intro']
		article.text = request.form['text']
		try:
			db.session.commit()
			return redirect(url_for("main_page"))
		except:
			return redirect(url_for("error_page"))
	else:
		return render_template("article_update_page.html", article=article)


@app.route("/error")
def error_page():
	return render_template("error_page.html")


if __name__ == "__main__":
	app.env = "HARD WORK!!!"
	app.debug = True
	app.run()