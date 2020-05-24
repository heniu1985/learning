def sandwich(*ingredients):
    """Funkcja wyświetla informację o kanapce z podanymi składnikami"""
    
    print("Na kanapce znajdują się następujące składniki:")
    for ingredient in ingredients:
        print(f"- {ingredient}")

sandwich("szynka", "ser", "pomidor")
sandwich("jajko", "majonez",)
sandwich("ser", "szynka", "pomidor", "jajko", "majonez")