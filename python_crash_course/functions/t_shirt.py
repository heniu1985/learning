def make_shirt(size="XXL", text="Uwielbiam Pythona"):
    """Wyświetla informację o rozmiarze i nadruku na koszulce"""
    print(f"Zamówiono koszulkę w rozmiarze {size}, z następującym nadrukiem: {text}.")

make_shirt()
make_shirt("M")
make_shirt("S", "Piwo to moje paliwo")