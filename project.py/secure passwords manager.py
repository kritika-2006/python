class PasswordManager:
    def __init__(self): 
        self.passwords = {}
    
    def add_password(self,account_name,password):
        self.passwords[account_name.lower()] = password
        print("Password saved successfully")
    
    def get_password(self,account_name):
        name = account_name.lower()
        if  name in self.passwords:
            print(self.passwords[account_name])
        else:
            print("Account not found")
    
    def view_accounts(self):
        if not self.passwords:
            print("📭 No accounts saved yet.")
        else:
            print("\n--- Saved Accounts ---")
        for account in self.passwords:
            print("-",account)
obj = PasswordManager()
while True:
    print("\n*** Password Manager Menu ***")
    print("1. Add New Password")
    print("2. Get a Password")
    print("3. View All Accounts")
    print("4. Exit")
    
    choice = input("\nEnter choice (1-4): ")
    
    if choice == "1":
        acc = input("Enter account name (e.g., Instagram): ")
        pwd = input("Enter password: ")
        obj.add_password(acc, pwd)
        
    elif choice == "2":
        acc = input("Enter account name to search: ")
        obj.get_password(acc)
        
    elif choice == "3":
        obj.view_accounts()
        
    elif choice == "4":
        print("Goodbye! Stay Secure. 🔐")
        break
    else:
        print("❌ Invalid choice!")
