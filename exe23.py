threat_level = "Low" # global variable

def trigger_breach():
    global threat_level
    threat_level = "critical"
    # local variable
    breach_zone = "Server Room"
    print(f"Alert! Breach detected in {breach_zone}")

trigger_breach()
print(f"Current global Threat : {threat_level}")