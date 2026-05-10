def login(username, password):
    if password == "admin123":
        return f"{username} authenticated"
    return "Invalid credentials"