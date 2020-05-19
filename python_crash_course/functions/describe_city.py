def describe_city(city, country="Polsce"):
    """Wyświetla informację w jakim kraju leży dane miasto"""
    print(f"{city} leżą w {country}")

describe_city("Katowice")
describe_city("Polskie Łąki")
describe_city("Amsterdam", "Holandii")