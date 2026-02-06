from flask import Flask, request, jsonify
from flask_cors import CORS

from core_engine.nmap_scanner import NmapScanner
from core_engine.owasp_scanner import OWASPScanner
from core_engine.nikto_scanner import NiktoScanner

app = Flask(__name__)
CORS(app)

nmap_scanner = NmapScanner()
owasp_scanner = OWASPScanner()
nikto_scanner = NiktoScanner()


@app.route("/api/scan/network", methods=["POST"])
def network_scan():
    target = request.json.get("target")
    return jsonify(nmap_scanner.scan_target(target))


@app.route("/api/scan/web", methods=["POST"])
def web_scan():
    target = request.json.get("target")
    vulnerabilities = owasp_scanner.run_scan(target)
    return jsonify({
        "target": target,
        "vulnerabilities": vulnerabilities
    })


@app.route("/api/scan/server", methods=["POST"])
def server_scan():
    target = request.json.get("target")
    result = nikto_scanner.scan_server(target)
    return jsonify(result)


if __name__ == "__main__":
    app.run(port=5000, debug=True)
