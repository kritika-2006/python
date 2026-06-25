raw_ports = ["port:80","port:443","port:22","port:8080"]

clean_ports = [p[5:] for p in raw_ports]
print(clean_ports)