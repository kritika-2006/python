def register_device(device_id,**specs):
    for key, value in specs.items():
        print(f" {key} = {value}")

register_device("DB-server",IP = "192.168.1.1",OS = "Linux", Status = "Secure")
