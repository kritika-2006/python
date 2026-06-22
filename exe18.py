## *args store in Tuple
def hacker_tools(*tools):
    for tool in tools:
        print(f" Loaded tool : {tool}")

hacker_tools("Nmap","Wireshark","Metasploit")