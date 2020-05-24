def send_messages(messages, sent):
    """Wyświetla komunikat z listy i przenosi go na inną listę"""
    message = 0
    while messages:
        msg = messages.pop()
        message += 1
        print(f"Komunikat nr {message}: {msg}")
        sent.append(msg)

messages = ["Uwaga!", "Błąd!", "Dorze Ci idzie!", "Awaria!", "Zamknięcie programu."]
sent_messages = []

send_messages(messages[:], sent_messages)

print(messages)
print(sent_messages)