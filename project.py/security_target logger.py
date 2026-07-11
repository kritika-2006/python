import os
import requests
class TargetScanner:
    def __init__(self,target_url,folder_name):
        self.target_url = target_url
        self.folder_name = folder_name
        self.status_result  = ""
    
    def setup_lab(self):
        self.folder_name = input("put the name of the first folder:")
        if not os.path.exists(self.folder_name):
            os.mkdir(self.folder_name)
            print("📁 folder ban gya!")
        else:
            print("⚠️ Folder already exists!")
    def scan_target(self):
      
     try:
       self.target_url = "https://google.com"
       response = requests.get(self.target_url)
       if response.status_code == 200:
        print("Target is UP and Active")
       else:
        print("There is an error")
     except:
      print("Target is DOWN or Unreachable")
    
    def save_report(self):
       path = self.folder_name + "report.txt"
       with open(path,"w") as file:
          pass

obj = TargetScanner("https://api.github.com", "Github_Report_Lab")
obj.setup_lab()
obj.scan_target()
obj.save_report()


    

    