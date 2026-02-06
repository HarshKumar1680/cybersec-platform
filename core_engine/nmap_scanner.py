import subprocess

class NmapScanner:

    def scan_target(self, target):
        command = ["nmap", "-sV", "-T4", target]

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
