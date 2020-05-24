class Restaurant():
    """Klasa restauracji"""

    def __init__(self, restaurant_name, cusisine_type):
        """Inicjalizacja prezentacji restauracji"""
        self.name = restaurant_name
        self.type = cusisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Wyświetla rodzaj i nazwę restauracji"""
        print(f"{self.type.title()}: {self.name.title()}")

    def open_restaurant(self):
        """Wyświetla godziny otwarcia restauracji"""
        print("Poniedziałek: 12 - 20")
        print("Wtorek: 12 - 20")
        print("Środa: 12 - 20")
        print("Czwartek: 12 - 20")
        print("Piątek: 12 - 2")
        print("Sobota: 12 - 2")
        print("Niedziela: nieczynne")

    def set_number_served(self, served):
        """Umożliwia zmianę liczby obsłużonych gości"""
        self.number_served = served

    def increment_number_served(self, add_served):
        """Zwiększa liczbę obsłużonych klientów o podaną wartość"""
        self.number_served += add_served

    def show_number_served(self):
        """Wyświetla liczbę obsłużonych klientów"""
        print(f'W restauracji "{self.name.title()}" zostało obsłużonych {self.number_served} klientów.')

la_cantina = Restaurant("la cantina", "kuchnia śródziemnomorska")
batman = Restaurant("u batmana", "pizzeria")
pod_lipami = Restaurant("pod lipami", "kuchnia polska")

# la_cantina.describe_restaurant()
# batman.describe_restaurant()
# pod_lipami.describe_restaurant()

# batman.set_number_served(23)
# batman.show_number_served()

batman.show_number_served()
batman.increment_number_served(2)
batman.show_number_served()
batman.increment_number_served(4)
batman.increment_number_served(5)
batman.increment_number_served(9)
batman.show_number_served()