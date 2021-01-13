from hashlib import sha256, md5
import os

def digest_message(message):
	try:
		#SHA256
		message_sha256 = sha256()
		message_sha256.update(message)
		print("Message '{0}'".format(message))
		print("*" * 10)
		print("SHA256")
		print("Simple digest: ")
		print(message_sha256.digest())
		print("HexDigest: ")
		print(message_sha256.hexdigest())
		print("*" * 10)
		#MD5
		print("MD5")
		message_md5 = md5()
		message_md5.update(message)
		print("Simple digest: ")
		print(message_md5.digest())
		print("HexDigest: ")
		print(message_md5.hexdigest())
	except Exception as e:
		print(e)

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

def digest_file():
	file = "text.txt"
	print(f"File:\n{file}")
	md5_digest = digest_md5(file)
	sha256_digest = digest_sha256(file)

	print("MD5:")
	print(md5_digest)
	print("SHA256:")
	print(sha256_digest)

