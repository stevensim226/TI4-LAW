import json

DB_FILENAME = "database.json"
DATABASE = json.loads(open(DB_FILENAME).read())


def save_mahasiswa(name, npm):
	DATABASE.append({"name":name, "npm":npm})
	print(json.dumps(DATABASE), file=open(DB_FILENAME, "w"))
	print(DATABASE)

def find_mahasiswa(npm):
	for mahasiswa in DATABASE:
		if mahasiswa["npm"] == npm:
			return mahasiswa
	
	return None