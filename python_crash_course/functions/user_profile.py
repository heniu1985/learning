def build_profile(first, last, **user_info):
    """Budowa słownika zawierającego wszystkie informacje o użytkowniku."""
    user_info["first_name"] = first
    user_info["last_name"] = last
    return user_info

user_profile = build_profile("Damian", "Hennek", city="Katowice", country="Polska", lang="Python")

print(user_profile)