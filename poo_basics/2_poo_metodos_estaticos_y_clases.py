class User:
    tota_users = 100
    
    def __init__(self, name, second, age, sex):
        self.name = name
        self.second = second
        self.age = age
        self.sex = sex
        self.premium = False
        
    def __repr__(self):
        return f"{self.name}, {self.second}, {self.age}, {self.sex}, {self.premium}"
    
    def __del__(self):
        print("Objeto borrado")
    
    def convert_to_premium(self):
        self.premium = True
        
    def watch_movies(self):
        if self.premium:
            print("Movie acces")
        else:
            print("Access decline")
            
    @staticmethod
    def user_adult(age):
        return age >= 18
    
    @classmethod
    def total_users_number(cls):
        return cls.tota_users
    
    
        
user = User("Benito", "Avila", 36, "M")
print(user)
print(user.premium)
user.watch_movies()
user.convert_to_premium()
print(user)
print(user.premium)
user.watch_movies()
del user

adult = User.user_adult(18)

print(adult)

print(User.total_users_number())