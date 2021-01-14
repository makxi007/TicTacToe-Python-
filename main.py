from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from flask_sqlalchemy import SQLAlchemy

from werkzeug.utils import secure_filename

from hashes import digest_md5, digest_sha256
import os

UPLOAD_FOLDER = "files"
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg'])

app = Flask(__name__)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db" 
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


class Users(db.Model):
	db_id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.String(100), unique=True, nullable=False)
	file_name = db.Column(db.String(100), nullable=False)
	sha256sum_hash = db.Column(db.Text)
	md5sum_hash = db.Column(db.Text)

	def __repr__(self):
		return "< User: %r - %r >" % (self.db_id, self.user_id) 

#Check if file in allowed extensions
def allowed_file(filename):
	return "." in filename and \
		filename.rsplit(".", 1)[1] in ALLOWED_EXTENSIONS

@app.route("/", methods=["POST", "GET"])
def main():
	if request.method == "POST":
		#Get data from form
		user_title_id = request.form["title_id"]
		file = request.files["file"]
		
		if_user = Users.query.filter_by(user_id=user_title_id).first()

		# If user wrote file and extension of this file in allowed extension variable
		if file and allowed_file(file.filename):
			filename = secure_filename(file.filename)
			file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))

			#Get hash of file
			md5_hash = digest_md5(file.filename, path="files")
			sha256_hash = digest_sha256(file.filename, path="files")

			user_to_add = Users(user_id=user_title_id, file_name=file.filename, sha256sum_hash=sha256_hash, md5sum_hash=md5_hash)

			try:
				db.session.add(user_to_add)
				db.session.commit()
			except Exception as e:
				print(e)

			return redirect(url_for('file_by_hash', sum_hash=sha256_hash))

	return render_template("auth.html")

#Get file by hash
@app.route("/file_hashes/<sum_hash>", methods=["POST", "GET"])
def file_by_hash(sum_hash):
	#Query in database
	sha256 = Users.query.filter_by(sha256sum_hash=sum_hash).first()
	md5 = Users.query.filter_by(md5sum_hash=sum_hash).first()

	# By SHA256 found 
	if sha256 != None:
		return redirect(url_for("uploaded_file", filename=sha256.file_name))

	# By MD5 found
	if md5 != None:	
		return redirect(url_for("uploaded_file", filename=md5.file_name))

	return redirect(url_for('page_not_found'))

@app.route("/upload_files/uploads/<filename>")
def uploaded_file(filename):
	return send_from_directory(app.config["UPLOAD_FOLDER"], filename)


#Get data about all users
@app.route("/all_users")
def get_all_users():
	users = Users.query.all()
	return render_template("all_users.html", all_users=users)

#Error page
@app.route("/page_not_found")
def page_not_found():
	return "<h1>Page not found</h1>"



if __name__ == '__main__':

	app.run(host="localhost",port=3000,debug=True)