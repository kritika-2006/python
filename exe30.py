raw_variable = "  Kritika@gmail.com"
clean_variable = raw_variable.strip().lower()
print(clean_variable)
report_name = "malware_analysis_report.txt"
if (report_name.endswith(".txt")):
    print("Valid text log report")
else:
    print("Invalid format!")

alert = "System status : Unsecure"
print(alert.replace("Unsecure","secure"))

