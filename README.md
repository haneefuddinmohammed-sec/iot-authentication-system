# 🔐 IoT Device Authentication & Threat Detection System

## 🚀 Overview
This project simulates a real-world IoT security system that authenticates devices and detects suspicious access attempts.

It demonstrates how unauthorized devices can be identified and flagged using behavioral monitoring.

---

## 🧠 Features
- Device authentication using ID and key  
- Detection of unauthorized access attempts  
- Alert system for repeated failed logins  
- Continuous simulation of device connections  

---

## 💻 Technologies Used
- Python  
- JSON  

---

## ⚙️ How It Works
1. Devices attempt to connect using ID and key  
2. System validates credentials from stored device list  
3. Failed attempts are tracked  
4. After multiple failures → alert is triggered  

---

## ▶️ How to Run
```bash
python main.py
