router_logs ={"192.168.1.10","10.0.0.5","172.16.0.1"}
firewalls_logs = {"10.0.0.5","192.168.1.20","172.16.0.1"}

suspect_ips = router_logs & firewalls_logs
print(suspect_ips)

a = router_logs | firewalls_logs
print(a)