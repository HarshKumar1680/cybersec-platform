import requests
from bs4 import BeautifulSoup


class OWASPScanner:

    # ==============================
    # Get Forms from Page (future use)
    # ==============================
    def get_forms(self, url):
        try:
            response = requests.get(url, timeout=10)
            soup = BeautifulSoup(response.text, "html.parser")
            return soup.find_all("form")
        except:
            return []

    # ==============================
    # SQL Injection Detection
    # ==============================
    def detect_sqli(self, url):

        payload = "' OR '1'='1"

        test_url = url.rstrip("/") + "/?id=" + payload

        try:
            response = requests.get(test_url, timeout=10)
        except:
            return False

        errors = ["sql", "syntax", "mysql", "error", "database"]

        for error in errors:
            if error in response.text.lower():
                return True

        return False

    # ==============================
    # XSS Detection
    # ==============================
    def detect_xss(self, url):

        payload = "<script>alert('xss')</script>"

        test_url = url.rstrip("/") + "/?q=" + payload

        try:
            response = requests.get(test_url, timeout=10)
        except:
            return False

        if payload.lower() in response.text.lower():
            return True

        return False

    # ==============================
    # MAIN SCAN FUNCTION
    # ==============================
    def run_scan(self, url):

        # 🔥 Ensure URL has http/https
        if not url.startswith("http://") and not url.startswith("https://"):
            url = "https://" + url

        vulnerabilities = []

        if self.detect_sqli(url):
            vulnerabilities.append("SQL Injection Detected")

        if self.detect_xss(url):
            vulnerabilities.append("XSS Detected")

        return vulnerabilities