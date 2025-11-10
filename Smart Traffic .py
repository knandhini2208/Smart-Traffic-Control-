# =======================================================
# SMART TRAFFIC CONTROL SYSTEM USING AI AND IoT (PYTHON)
# =======================================================

import random
import time
from datetime import datetime

# -----------------------------
# Simulated Real-time Data Feed
# -----------------------------
vehicles = [
    {"number": "TN10AB1234", "helmet": True,  "speed": 45,  "signal": "green"},
    {"number": "TN22CD5678", "helmet": False, "speed": 92,  "signal": "red"},
    {"number": "TN18EF2468", "helmet": True,  "speed": 65,  "signal": "red"},
    {"number": "TN09GH1357", "helmet": True,  "speed": 130, "signal": "green"},
    {"number": "TN11JK2468", "helmet": False, "speed": 110, "signal": "green"},
]

# Randomly simulate ambulance detection
ambulance_detected = random.choice([True, False])

# Daily violation storage (can be replaced with CSV/Database)
violation_log = []


# ---------------------------------------------------
# Function: Classify speed levels
# ---------------------------------------------------
def classify_speed(speed):
    if speed <= 50:
        return "Normal"
    elif 51 <= speed <= 80:
        return "Medium"
    elif 81 <= speed <= 100:
        return "High"
    else:
        return "Very High"


# ---------------------------------------------------
# Function: Check for violations
# ---------------------------------------------------
def check_violations(vehicle):
    violations = []

    # Red light violation
    if vehicle["signal"] == "red":
        violations.append("Red Light Violation")

    # Helmet violation
    if not vehicle["helmet"]:
        violations.append("Helmet Not Worn")

    # Speed violation
    speed_type = classify_speed(vehicle["speed"])
    if speed_type in ["High", "Very High"]:
        violations.append(f"Over Speed ({speed_type})")

    return violations


# ---------------------------------------------------
# Function: Send emergency alert
# ---------------------------------------------------
def send_emergency_alert():
    print("\n🚨 EMERGENCY ALERT! 🚨")
    print("Ambulance detected — Sending signal to control center...")
    print("→ Switching all signals to GREEN for ambulance route.\n")
    time.sleep(1)


# ---------------------------------------------------
# Function: Log Violations
# ---------------------------------------------------
def log_violation(vehicle, violations):
    if not violations:
        return

    entry = {
        "number": vehicle["number"],
        "violations": violations,
        "speed": vehicle["speed"],
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    violation_log.append(entry)


# ---------------------------------------------------
# Function: Run Traffic Monitoring Cycle
# ---------------------------------------------------
def run_traffic_cycle():
    print("\n🧠 SMART TRAFFIC CONTROL SYSTEM (AI + IoT)")
    print("==========================================\n")
    time.sleep(1)

    # Step 1: Check for ambulance
    if ambulance_detected:
        send_emergency_alert()

    # Step 2: Analyze vehicles
    print("Analyzing vehicles in the traffic lane...\n")
    for v in vehicles:
        print(f"Vehicle: {v['number']}")
        print(f"  Helmet: {'Yes' if v['helmet'] else 'No'}")
        print(f"  Speed: {v['speed']} km/h ({classify_speed(v['speed'])})")
        print(f"  Signal: {v['signal'].upper()}")

        violations = check_violations(v)
        if violations:
            print(f"  ⚠️ Violations detected: {', '.join(violations)}")
        else:
            print("  ✅ No violations.")
        
        log_violation(v, violations)
        print("-" * 40)
        time.sleep(0.5)

    # Step 3: Daily Report Summary
    print("\n📋 DAILY VIOLATION REPORT")
    print("==========================================")
    if not violation_log:
        print("No violations recorded today.")
    else:
        for entry in violation_log:
            print(f"Vehicle: {entry['number']}")
            print(f"  Violations: {', '.join(entry['violations'])}")
            print(f"  Speed: {entry['speed']} km/h")
            print(f"  Time: {entry['time']}")
            print("-" * 40)

    print("\n✅ Report saved successfully.")
    print("System ready for next cycle...\n")


# ---------------------------------------------------
# Main Execution (Run Once)
# ---------------------------------------------------
if __name__ == "__main__":
    run_traffic_cycle()
