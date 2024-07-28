class User:
    def __init__(self, user_id, user_name):
        self.id = int(user_id)
        self.user_name = user_name.capitalize()


name = input("What's your name?: ")
id = input("What's your ID number?: ")

user = User(id, name)

print(f"Hello {user.user_name}, ID:{user.id}  ")
