class User():
    """Klasa opisująca użytkownika"""

    def __init__(self, first_name, last_name, email, country, city):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.country = country
        self.city = city

    def describe_user(self):
        print(f"{self.first_name.title()} {self.last_name.title()}")
        print(f"e-mail: {self.email}")
        print(f"{self.city.title()}, {self.country.title()}")

    def greet_user(self):
        print(f"Witaj {self.first_name.title()}")

user1 = User("Piotr", "Kowalski", "pkowalski@gmail.com", "Polska", "Rzeszów")
user2 = User("Damian", "Hennek", "hennek@gmail.com", "Polska", "Katowice")
user3 = User("John", "Kowalsky", "john.kowalsky@yahoo.com", "usa", "new york")

user1.greet_user()
user1.describe_user()

user2.greet_user()
user2.describe_user()

user3.greet_user()
user3.describe_user()