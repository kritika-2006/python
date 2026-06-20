server_security = {"status":"safe","active_firewalls":["UFW","iptables"],"logs":0}

while True:
    print("1. check server status.")
    print("2.simulate cyber attack.")
    print("3.shutdown and exit.")

    choice = 3
    choice = int(input("Enter our choice(1-3):"))
    if choice == 1:
        print(server_security)
    elif choice == 2:
        server_security["logs"] = ++1
        server_security["status"] = "UNDER ATTACK!"
        server_security["active_firewalls"].append("Cloudflare")
        print(server_security)
    elif choice == 3:
        print("Shutdown and Exit")
        break