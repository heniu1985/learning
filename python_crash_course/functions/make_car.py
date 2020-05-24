def make_car(marka, model, **car_info):
    """Tworzy słownik zawierający informacje o samochodzie"""
    car_info["marka"] = marka
    car_info["model"] = model
    return(car_info)

car = make_car("BWM", "520i", color="Bordowy", hak=True)

print(car)