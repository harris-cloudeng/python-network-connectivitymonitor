# &#x20;**Python Network Connectivity Monitor**



## &#x20;**Project Overview**

The Python Network Connectivity Monitor is a beginner-friendly network automation project that checks connectivity to multiple servers using ping requests.



It monitors server availability, extracts response latency, calculates packet loss, and stores monitoring results in a log file with timestamps.



#### &#x20;**Features**

\- Monitors multiple targets: `1.1.1.1`, `8.8.8.8`, and `google.com`

\- Checks connectivity using ping requests

\- Displays connection status

\- Extracts response latency

\- Calculates packets sent, received, lost, and packet-loss percentage

\- Records timestamps for monitoring checks

\- Saves results to `network\_log.txt`

\- Repeats monitoring every 60 seconds

\- Handles ping timeouts and log-file write errors



#### &#x20;**Technologies Used**

\- Python

\- Python `subprocess` module

\- Python `datetime` module

\- Python `time` module

\- Basic networking concepts: ICMP ping, latency, and packet loss

\- Git and GitHub for version control



#### &#x20;**Requirements**

\- Python 3 installed

\- Windows operating system

\- An active network connection for external connectivity checks



#### &#x20;**How to Run**

1\. Clone or download this repository.

2\. Open PowerShell in the project folder.

3\. Run:



&#x20;  `python network\_monitor.py`



4\. View the results in the terminal.

5\. Monitoring records are appended to `network\_log.txt`.



Press `Ctrl + C` to stop the monitoring loop.



#### &#x20;**Learning Outcomes**

Through this project, I practised Python scripting, network connectivity testing, error handling, latency extraction, packet-loss calculation, file logging, and basic version control.



#### &#x20;**Future Improvements**

\- Calculate average latency

\- Improve packet-loss measurement

\- Add configurable monitoring intervals

\- Generate monitoring reports

\- Explore cloud-based monitoring and alerting





