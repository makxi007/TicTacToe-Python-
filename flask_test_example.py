from flask import Flask, render_template, request, redirect, url_for
from flask_httpauth import HTTPBasicAuth
from flask_sqlalchemy import SQLAlchemy

from werkzeug.utils import secure_filename
from flask import send_from_directory

import os

UPLOAD_FOLDER = "files"
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg'])


app = Flask(__name__)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db" 
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

#this is files folder where files will be appload

class Users(db.Model):
	db_id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.String(100), unique=True, nullable=False)
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
		return "< Data: %r - %r >" % (self.db_id, self.user_id) 

#If user in db -> Just authorize user
#If user not in db -> just register user and remember
@app.route("/", methods=["POST", "GET"])
def main():
	if request.method == "POST":
		user_title_id = request.form["title_id"]
		
		if_user = Users.query.filter_by(user_id=user_title_id).first()

		if if_user != None:
			if if_user.user_id == user_title_id:
				return redirect(url_for("file_hashes"))
		if if_user == None:
			user_to_add = Users(user_id=user_title_id)
			try:
				db.session.add(user_to_add)
				db.session.commit()
			except Exception as e:
				print(e)

			return redirect(url_for("file_hashes"))

	return render_template("flask_test_example.html")

#Get data about all users
@app.route("/all_users")
def get_all_users():
	users = Users.query.all()
	return render_template("all_users.html", all_users=users)

def allowed_file(filename):
	return "." in filename and \
		filename.rsplit(".", 1)[1] in ALLOWED_EXTENSIONS

@app.route("/upload_files", methods=["GET", "POST"])
def upload_files():
	if request.method == "POST":
		file = request.files["file"]
		if file and allowed_file(file.filename):
			filename = secure_filename(file.filename)
			file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
			return redirect(url_for('upload_files', filename=filename))
	return render_template("upload_files.html")

@app.route("/upload_files/uploads/<filename>")
def uploaded_file(filename):
	return send_from_directory(app.config["UPLOAD_FOLDER"], filename)


@app.route("/file_hashes/", methods=["POST", "GET"])
def file_hashes():
	return "<p>You was authorized/register!</p><br><h1>Hashes page</h1>"

@app.route("/file_hashes/<int:hash>", methods=["POST", "GET"])
def file_by_hash(hash):
	return render_template("file_by_hash.html")



if __name__ == '__main__':
	app.run(debug=True)
	#app.run(host="localhost",port=3000,debug=True)