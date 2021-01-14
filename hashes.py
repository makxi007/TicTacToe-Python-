from hashlib import sha256, md5
import os

#MD5 HASH
def digest_md5(file, path=None):
	hash_md5 = md5()
	if path != None:
		with open(os.path.join(path, file), "rb") as file:
			for chunk in iter(lambda: file.read(4096), b""):
				hash_md5.update(chunk)
		return hash_md5.hexdigest()
	else:
		with open(file, "rb") as file:
			for chunk in iter(lambda: file.read(4096), b""):
				hash_md5.update(chunk)
		return hash_md5.hexdigest()

#SHA256 HASH
def digest_sha256(file, path=None):
	hash_sha256 = sha256()
	if path != None:
		with open(os.path.join(path, file), "rb") as file:
			for chunk in iter(lambda: file.read(4096), b""):
				hash_sha256.update(chunk)
		return hash_sha256.hexdigest()
	else:
		with open(file, "rb") as file:
			for chunk in iter(lambda: file.read(4096), b""):
				hash_sha256.update(chunk)
		return hash_sha256.hexdigest()



