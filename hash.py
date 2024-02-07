import csv
import pickle
from collections import namedtuple
import asciichartpy


# Speichern der Hashtabelle in einer Datei
def save_table(hash_table, filename):
    with open(filename, "wb") as file:
        data = {
            'table': hash_table.table,
            'probing_method': hash_table.probing_method
        }
        pickle.dump(data, file)


# Laden der Hashtabelle
def load_table(filename):
    with open(filename, "rb") as file:
        data = pickle.load(file)
        loaded_table = HashTable(len(data['table']), data['probing_method'])
        loaded_table.table = data['table']
        return loaded_table


# Aktienkurse für die letzten 30 Tage
def plot_stock(stock):
    # Daten für die letzten 30 Tage extrahieren
    dates = [price_data.date for price_data in stock.history[-30:]]
    closing_prices = [float(price_data.close) for price_data in stock.history[-30:]]

    # Plotten mit asciichart
    chart = asciichartpy.plot(closing_prices, {"height": 10})
    print(f"Closing Prices of {stock.name} in the Last 30 Days:")
    print(chart)


# NamedTuples für Aktien und Kursdaten
Stock = namedtuple("Stock", ["name", "wkn", "symbol", "history"])
PriceData = namedtuple("PriceData", ["date", "open", "high", "low", "close", "volume", "adj_close"])


class HashTable:
    def __init__(self, size, probing_method):
        self.size = size
        self.table = [None] * size
        self.probing_method = probing_method

    # Hashfunktion, die einen String (Aktienkürzel) in einen Index umwandelt
    def hash_function(self, key):
        return sum(ord(c) for c in key) % self.size

    # Sondierungsmethoden für die Hashtabelle
    def quadratic_probing(self, key, i):
        return (self.hash_function(key) + i ** 2) % self.size

    def linear_probing(self, key, i):
        return (self.hash_function(key) + i) % self.size

    def double_hashing(self, key, i):
        return (self.hash_function(key) + i * (1 + (self.hash_function(key) % (self.size - 1)))) % self.size

    # Auswählen der Sondierungsmethode basierend auf der gewählten Methode
    def probing_method_selector(self, key, i):
        methods = {
            'quadratic_probing': self.quadratic_probing,
            'linear_probing': self.linear_probing,
            'double_hashing': self.double_hashing
        }
        return methods[self.probing_method](key, i)

    def insert(self, stock):
        for i in range(self.size):
            index = self.probing_method_selector(stock.symbol, i)
            if self.table[index] is None:
                self.table[index] = stock
                return True
        return False

    def delete(self, symbol):
        for i in range(self.size):
            index = self.probing_method_selector(symbol, i)
            if self.table[index] is not None and self.table[index].symbol == symbol:
                self.table[index] = "DELETED"
                return True
        return False

    def search(self, symbol):
        for i in range(self.size):
            index = self.probing_method_selector(symbol, i)
            if self.table[index] is None:
                return None
            if self.table[index] != "DELETED" and self.table[index].symbol == symbol:
                return self.table[index]
        return None


def import_stock_data(stock, filename):
    with open(filename, "r") as file:
        reader = csv.reader(file)
        next(reader)  # Überspringe die Header-Zeile
        stock.history.extend([PriceData(*row) for row in reader])


def main():
    print("Bitte wählen Sie ein Hashing-Verfahren:")
    print("1) Quadratische Sondierung")
    print("2) Lineare Sondierung")
    print("3) Double Hashing")
    choice = input("Geben Sie die Nummer der gewünschten Methode ein: ")

    probing_methods = {
        '1': 'quadratic_probing',
        '2': 'linear_probing',
        '3': 'double_hashing'
    }

    if choice in probing_methods:
        probing_method = probing_methods[choice]
    else:
        print("Ungültige Eingabe. Verwende lineare Sondierung als Standardmethode.")
        probing_method = 'linear_probing'

    # Initialisieren Sie die Hashtabelle mit einer geeigneten Größe (z.B. 2000)
    hash_table = HashTable(2000, probing_method)

    while True:
        command = input("Bitte geben Sie einen Befehl ein (ADD, DEL, IMPORT, SEARCH, PLOT, SAVE, LOAD, QUIT): ")

        if command == "ADD":
            name = input("Geben Sie den Namen der Aktie ein: ")
            wkn = input("Geben Sie die WKN der Aktie ein: ")
            symbol = input("Geben Sie das Kürzel der Aktie ein: ")
            stock = Stock(name, wkn, symbol, [])
            if hash_table.insert(stock):
                print("Aktie erfolgreich hinzugefügt.")
            else:
                print("Fehler beim Hinzufügen der Aktie.")

        elif command == "DEL":
            symbol = input("Geben Sie das Kürzel der Aktie ein, die gelöscht werden soll: ")
            if hash_table.delete(symbol):
                print("Aktie erfolgreich gelöscht.")
            else:
                print("Fehler beim Löschen der Aktie.")

        elif command == "IMPORT":
            symbol = input("Geben Sie das Kürzel der Aktie ein, für die Sie Kursdaten importieren möchten: ")
            stock = hash_table.search(symbol)
            if stock is not None:
                filename = input(
                    "Geben Sie den Namen der CSV-Datei ein, aus der die Kursdaten importiert werden sollen: ")
                import_stock_data(stock, filename)
                print("Kursdaten erfolgreich importiert.")
            else:
                print("Aktie nicht gefunden.")

        elif command == "SEARCH":
            symbol = input("Geben Sie das Kürzel der Aktie ein, die Sie suchen möchten: ")
            stock = hash_table.search(symbol)
            if stock is not None:
                print("Aktie gefunden:")
                latest_data = stock.history[-1] if stock.history else None
                if latest_data is not None:
                    print(f"Aktuellster Kurseintrag für {stock.name}: {latest_data}")
                else:
                    print("Keine Kursdaten vorhanden.")
            else:
                print("Aktie nicht gefunden.")


        elif command == "PLOT":
            symbol = input(
                "Geben Sie das Kürzel der Aktie ein, für die Sie die Schlusskurse der letzten 30 Tage anzeigen möchten: ")
            stock = hash_table.search(symbol)
            if stock is not None:
                plot_stock(stock)
            else:
                print("Aktie nicht gefunden.")

        elif command.startswith("SAVE"):
            _, filename = command.split()
            save_table(hash_table, filename)
            print(f"Hashtabelle erfolgreich in {filename} gespeichert.")

        elif command.startswith("LOAD"):
            try:
                _, filename = command.split()
            except ValueError:
                filename = input("Geben Sie den Dateinamen zum Laden ein: ")
            hash_table = load_table(filename)
            print(f"Hashtabelle erfolgreich aus {filename} geladen.")

        elif command == "QUIT":
            break
        else:
            print("Ungültiger Befehl. Bitte geben Sie einen gültigen Befehl ein.")


if __name__ == "__main__":
    main()
