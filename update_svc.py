from flask import Flask, request
from database import save_mahasiswa

app = Flask(__name__)
app.url_map.strict_slashes = False

@app.route('/update', methods=["POST"])
def update_service():
	json_req = request.get_json()
	save_mahasiswa(json_req["name"], json_req["npm"])
	print(f"Saved mahasiswa of name {json_req['name']} and npm {json_req['npm']}")

	return {"status": "OK"}

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000)