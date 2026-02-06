import requests
from bs4 import BeautifulSoup

class OWASPScanner:

    def get_forms(self, url):
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        return soup.find_all("form")

    def detect_sqli(self, url):
        payload = "' OR '1'='1"
        test_url = url + payload

        response = requests.get(test_url)

        errors = ["sql", "syntax", "mysql", "error", "database"]

        for error in errors:
            if error in response.text.lower():
                return True

        return False

    def detect_xss(self, url):
        payload = "<script>alert('xss')</script>"
        test_url = url + payload

        response = requests.get(test_url)

        if payload in response.text:
            return True

        return False

    def run_scan(self, url):

        vulnerabilities = []

        if self.detect_sqli(url):
            vulnerabilities.append("SQL Injection Detected")

        if self.detect_xss(url):
            vulnerabilities.append("XSS Detected")

        return vulnerabilities
