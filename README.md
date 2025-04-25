# Network Sniffer – DNS Tracker

This is a simple Python script that captures DNS query packets on your network and logs the domain names of visited websites in real time. It's a great lightweight tool for network monitoring and learning about how DNS queries work under the hood.

## 🔍 Features

- Captures DNS query packets (UDP on port 53)
- Displays unique domain names visited
- Avoids printing duplicate domains
- Lightweight and RAM-efficient (doesn't store packets)

## 📦 Requirements

- Python 3.x
- [Scapy](https://scapy.readthedocs.io/en/latest/)

You can install Scapy using pip:

```bash
pip install scapy
