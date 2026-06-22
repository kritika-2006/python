def grant_lab_access(username,access_level= "student"):
    return f"Access granted to {username}. Role: {access_level}"

a = grant_lab_access("kritika")
print(a)

b = grant_lab_access("manvi","Admin")
print(b)
