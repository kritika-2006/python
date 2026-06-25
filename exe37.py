scanned_ips = ["192.168.1.1","10.0.0.1","192.168.1.5","10.0.0.22","192.168.1.100"]

local_ips = [p for p in scanned_ips if p.startswith("192.168")]
print(local_ips)