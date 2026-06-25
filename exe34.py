ports = [80,443,22,80]
#  agar p== 80  to web print karo , otherwise not 
port_labels = ["web" if p==80 else "other" for p in ports]
print(port_labels)