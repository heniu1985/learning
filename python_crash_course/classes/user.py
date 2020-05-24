class User():
    """Klasa opisująca użytkownika"""

    def __init__(self, first_name, last_name, email, country, city):
        """Inicjalizacja atrybutów opisujących użytkownika"""
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.country = country
        self.city = city
        self.login_attempts = 0

    def describe_user(self):
        """Wyświetla opis użytkownika"""
        print(f"{self.first_name.title()} {self.last_name.title()}")
        print(f"e-mail: {self.email}")
        print(f"{self.city.title()}, {self.country.title()}")

    def greet_user(self):
        """Spersonalizowane powitanie"""
        print(f"Witaj {self.first_name.title()}")

    def increment_login_attempts(self):
        """Zwiększa liczbę prób logowania"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Resetuje próby logowania"""
        self.login_attempts = 0

    def show_login_attempts(self):
        """Wyświetla liczbę prób logowania"""
        print(f"{self.login_attempts} prób logowania.")

user1 = User("Piotr", "Kowalski", "pkowalski@gmail.com", "Polska", "Rzeszów")
user2 = User("Damian", "Hennek", "hennek@gmail.com", "Polska", "Katowice")
user3 = User("John", "Kowalsky", "john.kowalsky@yahoo.com", "usa", "new")

# user1.greet_user()
# user1.describe_user()

# user2.greet_user()
# user2.describe_user()

# user3.greet_user()
# user3.describe_user()

user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.show_login_attempts()
user1.reset_login_attempts()
user1.show_login_attempts()