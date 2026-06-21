compromised_devices = {
    "Lab-PC-01":"Trojan Infected",
    "Server-Alpha":"Ransomware",
    "Director-Laptop":"Spyware"
}

print(compromised_devices.get("Guest wifi","Device is clean"))
 
compromised_devices.update({"Router-main":"DDOS Target"})

removed_device = compromised_devices.pop("Director-Laptop")
print(f"Successfully removed Director-Laptop which had {removed_device}")

for key,value in compromised_devices.items():
    print(f"{key} value : {value}")