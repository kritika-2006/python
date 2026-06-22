# **Kwargs store in dictionary
def file(name, **details):
    print(f"User: {name}")
    print(details)
    
file("kritika",role="Explorer",status= "Active")
