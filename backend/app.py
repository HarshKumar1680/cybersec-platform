from flask import Flask, request, jsonify
from flask_cors import CORS
from core_engine.nmap_scanner import NmapScanner

app = Flask(__name__)
CORS(app)

scanner = NmapScanner()

@app.route("/api/scan/network", methods=["POST"])
def network_scan():

    target = request.json.get("target")

    result = scanner.scan_target(target)

    return jsonify(result)


if __name__ == "__main__":
    app.run(port=5000, debug=True)
