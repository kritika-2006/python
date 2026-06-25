# long way
"""tools = ["nmap","wireshark","sqlmap"]
upper_tools = []

for t in tools:
    upper_tools.append(t.upper())
print(upper_tools)"""

# list comprehension
tools = ["nmap","wireshark","sqlmap"]
upper_tools = [t.upper() for t in tools]
print(upper_tools)