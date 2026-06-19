print("--- Welcome to the Python Shopping Game! ---")

mall_items = ["Laptop", "Phone", "Headphones", "Watch"]
my_cart = []

while True:
    print("\n1. View Mall Items")
    print("2. Add Item to Cart")
    print("3. Remove Item from Cart")
    print("4. Checkout & Exit")
    
    choice = int(input("\nEnter your choice (1-4): "))
    
    if choice == 1:
        print("\nAvailable items in Mall:")
        
    elif choice == 2:
        item = input("Kaun sa item add karna hai? ")
        
    elif choice == 3:
        item = input("Kaun sa item remove karna hai? ")
         
        
    elif choice == 4:
        print("\nShopping Complete! Aapka final cart:", my_cart)
        print("Total items bought:", len(my_cart)) 
        break