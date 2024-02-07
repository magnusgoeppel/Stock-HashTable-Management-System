# Stock HashTable Management System

## Beschreibung

Dieses Programm bietet ein einfaches, aber effektives System zur Verwaltung von Aktieninformationen mit einer Hashtabelle. Es ermöglicht Benutzern, Aktiendaten zu speichern, zu suchen, zu löschen und Kursdaten aus CSV-Dateien zu importieren. Zusätzlich unterstützt das Programm das Plotten der Schlusskurse von Aktien für die letzten 30 Tage in einem ASCII-Diagramm und ermöglicht die Speicherung bzw. das Laden der Hashtabelle in bzw. aus einer Datei.

## Features

- **Hashing-Verfahren:** Unterstützt drei verschiedene Sondierungsmethoden für die Hashtabelle: quadratische Sondierung, lineare Sondierung und Double Hashing.
- **CRUD-Operationen:** Ermöglicht das Hinzufügen, Löschen und Suchen von Aktien in der Hashtabelle.
- **Importieren von Kursdaten:** Unterstützt das Importieren von Aktienkursdaten aus CSV-Dateien.
- **Datenvisualisierung:** Zeigt die Schlusskurse einer Aktie der letzten 30 Tage in einem ASCII-Diagramm an.
- **Persistenz:** Ermöglicht das Speichern der Hashtabelle in einer Datei und das Laden aus einer Datei.

## Anleitung

### Voraussetzungen

- Python 3.4 oder höher
- Bibliotheken:  `csv`, `pckile`, `collections.namedtuple`, `assciichart`


### Verwendung
1. Starten Sie das Programm.
2. Wählen Sie ein Hashing-Verfahren aus den vorgegebenen Optionen.
3. Verwenden Sie die folgenden Befehle für verschiedene Operationen:
   - ADD: Fügt eine neue Aktie hinzu.
   - DEL: Löscht eine vorhandene Aktie.
   - IMPORT: Importiert Kursdaten für eine Aktie aus einer CSV-Datei.
   - SEARCH: Sucht nach einer Aktie und zeigt die neuesten Kursdaten, falls vorhanden.
   - PLOT: Zeigt die Schlusskurse der letzten 30 Tage für eine Aktie im ASCII-Format.
   - SAVE <filename>: Speichert die aktuelle Hashtabelle in einer Datei.
   - LOAD <filename>: Lädt eine Hashtabelle aus einer Datei.
   - QUIT: Beendet das Programm.
