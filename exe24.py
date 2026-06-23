db_credentials = ("admin","SuperSecretPass123","MySQL")
# a = db_credentials.update(1,"HackPass")
print(db_credentials)

db_user, db_password, db_type = db_credentials
print(f"Connecting to {db_type} database using username: {db_user}")