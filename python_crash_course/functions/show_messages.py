def show_messages(komunikaty):
    """Wyświetla komunikat z listy"""
    for message in messages:
        msg = f"Komunikat: {message}"
        print(msg)

messages = ["Uwaga!", "Błąd!", "Dorze Ci idzie!", "Awaria!", "Zamknięcie programu."]

show_messages(messages)