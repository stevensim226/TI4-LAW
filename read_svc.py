from flask import Flask, request
from database import find_mahasiswa

app = Flask(__name__)

@app.route('/read/<npm>', methods=["GET"])
def read_normal_service(npm):
	print(f"Get mahasiswa of npm {npm}")
	mahasiswa = find_mahasiswa(npm)
	if mahasiswa:
		return {
			"status": "OK",
			"npm": mahasiswa["npm"],
			"nama": mahasiswa["name"]
		}

	return {"status": "NOTOK"}

@app.route('/read/<npm>/<int:trx_id>', methods=["GET"])
def read_cached_service(npm, trx_id):
	print(f"Get mahasiswa of npm {npm} with transaction id {trx_id}")
	mahasiswa = find_mahasiswa(npm)
	if mahasiswa:
		return {
			"status": "OK",
			"npm": mahasiswa["npm"],
			"nama": mahasiswa["name"]
		}

	return {"status": "NOTOK"}

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=9000)