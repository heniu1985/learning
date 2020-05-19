def city_country(city, country):
    """Wyświetla miasto i państwo"""
    msg = f"{city}, {country}"
    return msg

info = city_country("Katowice", "Polska")
print(info)

info = city_country("Sztokholm", "Szwecja")
print(info)

info = city_country("Budapeszt", "Węgry")
print(info)