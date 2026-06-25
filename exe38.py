device_statuses = ["Active","Malicious","Active","Active","Malicious"]
sanitized_statuses = ["Block" if p=="Malicious" else "Active" for p in device_statuses]
print(sanitized_statuses)