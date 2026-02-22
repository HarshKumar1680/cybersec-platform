import subprocess

class NiktoScanner:

    def scan_server(self, target):

        print("🔍 Starting Nikto quick scan...")

        command = [
     "perl",
    "C:/nikto-master/program/nikto.pl",
    "-h",
    f"https://{target}",  
    "-ssl",
    "-nointeractive",
    "-Tuning",
    "1,2,3,4,5",
    "-maxtime",
    "60"
]

        try:
            process = subprocess.Popen(
                command,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )

            stdout, stderr = process.communicate()

            print("✅ Nikto scan completed")

            if stdout:
                return {"status": "success", "data": stdout}
            else:
                return {"status": "success", "data": stderr}

        except Exception as e:
            return {"status": "error", "data": str(e)}