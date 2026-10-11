

import os
import time
from datetime import datetime

servers = ["1.1.1.1", "8.8.8.8", "google.com"]

while True:
    print("\nStarting network check...")

    for server in servers:
        print("\nChecking server:", server)

        check_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print("Check time:", check_time)

        output = os.popen(f"ping -n 1 {server}").read()

        if "Reply from" in output:
            status = "CONNECTION OK"
            latency = "Not available"

            for line in output.split("\n"):
                if "Reply from" in line:
                    parts = line.split()

                    for part in parts:
                        if part.startswith("time=") or part.startswith("time<"):
                            latency = part.replace("time=", "").replace("time<", "<")
                            break

                    break

        else:
            status = "CONNECTION DOWN"
            latency = "Not available"

        print("Status:", status)
        print("Latency:", latency)

        with open("network_log.txt", "a") as file:
            file.write(
                f"{check_time} | {server} | {status} | Latency: {latency}\n"
            )

    print("\nNetwork check complete. Waiting 60 seconds...")
    time.sleep(60)
