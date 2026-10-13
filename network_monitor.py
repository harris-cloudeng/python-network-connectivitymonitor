
import subprocess
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

        # Send four ping requests with error handling
        try:
            result = subprocess.run(
                ["ping", "-n", "4", "-w", "2000", server],
                capture_output=True,
                text=True,
                timeout=10
            )

            output = result.stdout + result.stderr

        except subprocess.TimeoutExpired:
            output = ""

        # Initialize packet statistics
        packets_sent = 4
        packets_received = 0

        # Count successful ping replies
        for line in output.splitlines():
            if "Reply from" in line and "bytes=" in line:
                packets_received += 1

        # Calculate packet loss percentage
        packets_lost = packets_sent - packets_received
        packet_loss = (packets_lost / packets_sent) * 100

        # Check connection status and extract latency
        if packets_received > 0:
            status = "CONNECTION OK"
            latency = "Not available"

            for line in output.splitlines():
                if "Reply from" in line and "bytes=" in line:
                    parts = line.split()

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

        # Display the results
        print("Status:", status)
        print("Latency:", latency)
        print("Packets Sent:", packets_sent)
        print("Packets Received:", packets_received)
        print("Packets Lost:", packets_lost)
        print("Packet Loss:", f"{packet_loss:.0f}%")

        # Save the results to the log file
        try:
            with open("network_log.txt", "a") as file:
                file.write(
                    f"{check_time} | {server} | {status} | "
                    f"Latency: {latency} | "
                    f"Sent: {packets_sent} | "
                    f"Received: {packets_received} | "
                    f"Lost: {packets_lost} | "
                    f"Packet Loss: {packet_loss:.0f}%\n"
                )
        except OSError as error:
            print("Could not write to log file:", error)

    # Wait 60 seconds before the next check
    print("\nNetwork check complete. Waiting 60 seconds...")
    time.sleep(60)
