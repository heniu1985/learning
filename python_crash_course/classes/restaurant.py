class Restaurant():
    """Klasa restauracji"""

    def __init__(self, restaurant_name, cusisine_type):
        """Inicjalizacja prezentacji restauracji"""
        self.name = restaurant_name
        self.type = cusisine_type

    def describe_restaurant(self):
        print(f"{self.type.title()}: {self.name.title()}")

    def open_restaurant(self):
        print("Poniedziałek: 12 - 20")
        print("Wtorek: 12 - 20")
        print("Środa: 12 - 20")
        print("Czwartek: 12 - 20")
        print("Piątek: 12 - 2")
        print("Sobota: 12 - 2")
        print("Niedziela: nieczynne")

la_cantina = Restaurant("la cantina", "kuchnia śródziemnomorska")
batman = Restaurant("u batmana", "pizzeria")
pod_lipami = Restaurant("pod lipami", "kuchnia polska")

la_cantina.describe_restaurant()
batman.describe_restaurant()
pod_lipami.describe_restaurant()