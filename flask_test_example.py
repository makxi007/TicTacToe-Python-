from flask import Flask, render_template, request
from flask_httpauth import HTTPBasicAuth
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db" 
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

#this is files folder where files will be appload
files_folder = "files"


class Users(db.Model):
	db_id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.String(100), nullable=False)
	# file_name = db.Column(db.String(100), nullable=False)
	# sha256sum_hash = db.Column(db.Text)
	# md5sum_hash = db.Column(db.Text)

	def __repr__(self):
		# db_data = {
		# "database_id":self.db_id,
		# "user_id":self.user_id,
		# # "file_name":self.file_name,
		# # "sha256sum_hash":self.sha256sum_hash,
		# # "md5sum_hash":self.md5sum_hash
		# }
		return "Data:\n %r " % self.db_id 

#If user in db -> Just authorize user
#If user not in db -> just register user and remember
@app.route("/", methods=["POST", "GET"])
def main():
	if request.method == "POST":
		user_title_id = request.form["title_id"]
		if user_title_id.strip() == user_id.strip():
			return "<h1>Success</h1>"
		else:
			return "<h1>Unknown id</h1>"

	return render_template("flask_test_example.html")

if __name__ == '__main__':
	app.run(debug=True)