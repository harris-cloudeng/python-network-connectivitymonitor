
import os
import time
from datetime import datetime

# List of servers to monitor
servers = ["1.1.1.1", "8.8.8.8", "google.com"]

# Run the network monitor continuously
while True:
    print("\nStarting network check...")

    # Check each server
    for server in servers:
        print("\nChecking server:", server)

        # Get the current date and time
        check_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print("Check time:", check_time)

        # Send one ping request to the server
        output = os.popen(f"ping -n 1 {server}").read()

        # Check whether the ping was successful
        if "bytes=" in output and "TTL=" in output:
            status = "CONNECTION OK"
            latency = "Not available"

            # Find the successful reply line
            for line in output.splitlines():
                if "Reply from" in line and "bytes=" in line:
                    parts = line.split()

                    # Extract the latency
                    for part in parts:
                        if part.startswith("time="):
                            latency = part.replace("time=", "")
                            break
                        elif part.startswith("time<"):
                            latency = part.replace("time", "")
                            break

                    break

        else:
            status = "CONNECTION DOWN"
            latency = "Not available"

        # Display the result
        print("Status:", status)
        print("Latency:", latency)

        # Save the result to the log file
        with open("network_log.txt", "a") as file:
            file.write(
                f"{check_time} | {server} | {status} | Latency: {latency}\n"
            )

    # Wait 60 seconds before the next check
    print("\nNetwork check complete. Waiting 60 seconds...")
    time.sleep(5)
