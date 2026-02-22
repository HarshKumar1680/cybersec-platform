from flask import Flask, request, jsonify
from flask_cors import CORS
from apscheduler.schedulers.background import BackgroundScheduler

from core_engine.nmap_scanner import NmapScanner
from core_engine.owasp_scanner import OWASPScanner
from core_engine.nikto_scanner import NiktoScanner


app = Flask(__name__)
CORS(app)

# =============================
# Scanner Instances
# =============================
nmap_scanner = NmapScanner()
owasp_scanner = OWASPScanner()
nikto_scanner = NiktoScanner()


# =============================
# API ROUTES
# =============================

@app.route("/api/scan/network", methods=["POST"])
def network_scan():
    target = request.json.get("target")
    print("🌐 Network Scan Requested:", target)
    return jsonify(nmap_scanner.scan_target(target))


@app.route("/api/scan/web", methods=["POST"])
def web_scan():
    target = request.json.get("target")
    print("🕷️ Web Scan Requested:", target)

    vulnerabilities = owasp_scanner.run_scan(target)

    return jsonify({
        "target": target,
        "vulnerabilities": vulnerabilities
    })


@app.route("/api/scan/server", methods=["POST"])
def server_scan():
    target = request.json.get("target")

    print("📡 Server Scan Requested:", target)

    result = nikto_scanner.scan_server(target)

    print("📤 Sending Server Scan Result")

    return jsonify(result)


# =============================
# PHASE 4 — AUTO SCAN ENGINE
# =============================

def auto_security_scan():
    print("\n⏰ AUTO SECURITY SCAN STARTED")

    target = "demo.testfire.net"

    try:
        nikto_result = nikto_scanner.scan_server(target)
        print("✅ Auto Nikto Scan Finished")

    except Exception as e:
        print("❌ Auto Scan Error:", str(e))


# Background Scheduler
scheduler = BackgroundScheduler()
scheduler.add_job(auto_security_scan, "interval", minutes=2)
scheduler.start()


# =============================
# MAIN APP RUN
# =============================

if __name__ == "__main__":
    print("🚀 Cyber Security Platform Running...")
    app.run(port=5000, debug=True)