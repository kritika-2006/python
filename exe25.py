# In set 
# no duplicate allowed
# it is unordered
scanned_ports = {80, 443 ,80, 22, 8080}
print(scanned_ports)
# methods
scanned_ports.add(45)
scanned_ports.remove(22)
print(scanned_ports)