all_ports = [80,443,22,23,3389]
web_ports = [p for p in all_ports if p>100]
print(web_ports)