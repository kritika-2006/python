# global variable
system_status = 10
def fire_alert():
# local variable
    local_ip= "10.0.0.5"
    print(f"inside function : system is {system_status} on ip {local_ip}")

fire_alert()

# global variable call on outside
print(system_status)
 # local variable does not call on outside
 # print(local_ip) 