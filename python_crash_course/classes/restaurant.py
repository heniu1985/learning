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

class IceCreamStand(Restaurant):
    """Pod klasa (klasa dziedzicząca) klasy Restaurant stowrzona by wymodelować budkę z lodami"""

    def __init__(self, restaurant_name, cusisine_type):
        """Przedstawia cechy charakterystyczne budki z lodami"""
        super().__init__(restaurant_name, cusisine_type)
        self.flavors = ["Jagodowy", "Czekoladowy", "Mango", "Nutella"]

    def show_flavors(self):
        """Wyświetla wszystkie dostępne smaki lodów"""
        print("Dostępne smaki lodów:")
        for flavor in self.flavors:
            print(f"- {flavor}")

restaurant1 = Restaurant("la cantina", "kuchnia śródziemnomorska")
restaurant2 = Restaurant("u batmana", "pizzeria")
restaurant3 = Restaurant("pod lipami", "kuchnia polska")
ice_cream_stand1 = IceCreamStand("Lodzio", "Budka z lodami")

ice_cream_stand1.describe_restaurant()
ice_cream_stand1.show_flavors()