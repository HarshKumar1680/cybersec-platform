import subprocess

class NiktoScanner:

    def scan_server(self, target):

        command = [
            "perl",
            "C:/nikto-master/program/nikto.pl",
            "-h",
            target
        ]

        try:
            output = subprocess.check_output(
                command,
                stderr=subprocess.STDOUT,
                text=True
            )

            return {
                "status": "success",
                "data": output
            }

        except Exception as e:
            return {
                "status": "error",
                "data": str(e)
            }
