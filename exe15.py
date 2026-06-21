def check_firewall_status(active_firewalls, incoming_attacks):
    if incoming_attacks > 5 :
        return "Danger! Deploy Cloudflare immediately."
    else : 
        return f"System Safe. Firewalls {active_firewalls} are handling it."
my_firewalls = ["UFW","iptables"]

# attack > 5
result1 = check_firewall_status(my_firewalls,8)
print("Test 1:",result1)

result2 = check_firewall_status(my_firewalls,3)
print("Test2:",result2)
