# System Traceability w Branży Farmaceutycznej

Projekt Inżynierski - Piotr Kryziński

## Opis Projektu

System umożliwia pełne śledzenie genealogii partii leków (Traceability) zgodnie ze standardami GMP. Aplikacja pozwala na:

1. Ewidencję surowców i produktów (Materiały).
2. Zarządzanie partiami produkcyjnymi (Batches) i ich statusami.
3. Rejestrację zużycia surowców (Traceability).
4. Generowanie raportów "Wstecz" i "W przód" dla wybranej serii.

## Stos Technologiczny

- **Język:** Python 3.11
- **Framework:** Django 5.2
- **Baza Danych:** SQLite (Plik db.sqlite3 załączony z danymi testowymi)

## Instrukcja Uruchomienia

1. Otwórz terminal w folderze projektu.

2. Stwórz wirtualne środowisko:
   `python -m venv venv`

3. Aktywuj środowisko:

   - Windows: `venv\Scripts\activate`
   - Mac/Linux: `source venv/bin/activate`

4. Zainstaluj wymagane biblioteki (w tym Django i python-docx):
   `pip install -r requirements.txt`

5. Uruchom serwer (Migracje nie są konieczne, jeśli używasz załączonej bazy danych):
   `python manage.py runserver`

6. Otwórz przeglądarkę: http://127.0.0.1:8000/


## Scenariusz Testowy (Sprawdzenie Traceability)

Aby zobaczyć działanie systemu i wygenerować raport genealogiczny:

1. Wejdź na stronę główną: http://127.0.0.1:8000/
2. W wyszukiwarkę wpisz numer serii: **SERIA-TAB-2025**
3. Kliknij **Szukaj**.
