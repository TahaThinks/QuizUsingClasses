class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0


user_1 = User("001", "angela")
user_2 = User("002", "taha")

print(user_1.username)
print(user_2.username)