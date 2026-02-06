from flask import Flask, request, jsonify
from flask_cors import CORS

from core_engine.nmap_scanner import NmapScanner
from core_engine.owasp_scanner import OWASPScanner

app = Flask(__name__)
CORS(app)

nmap_scanner = NmapScanner()
owasp_scanner = OWASPScanner()


@app.route("/api/scan/network", methods=["POST"])
def network_scan():
    target = request.json.get("target")
    result = nmap_scanner.scan_target(target)
    return jsonify(result)


@app.route("/api/scan/web", methods=["POST"])
def web_scan():
    target = request.json.get("target")

    vulnerabilities = owasp_scanner.run_scan(target)

    return jsonify({
        "target": target,
        "vulnerabilities": vulnerabilities
    })


if __name__ == "__main__":
    app.run(port=5000, debug=True)
