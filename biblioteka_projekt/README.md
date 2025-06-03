System zarządzania cyfrową biblioteką

1. Opis projektu

Aplikacja internetowa pozwalająca na zarządzanie książkami w cyfrowej bibliotece. Projekt został wykonany w Django z wykorzystaniem wzorca architektonicznego MVC. Umożliwia dodawanie, edytowanie, usuwanie oraz wyświetlanie książek.

2. Funkcjonalności

- Dodawanie książek (tytuł, autor, rok wydania)
- Edycja istniejących książek
- Usuwanie książek
- Walidacja danych:
  - Imię i nazwisko autora nie mogą zawierać cyfr
  - Rok wydania musi być 4-cyfrowy, bez liter, nie może przekraczać bieżącego roku

3. Instalacja i uruchomienie

3.1. Sklonuj repozytorium:
bash
git clone https://github.com/twoj-uzytkownik/nazwa-repo.git
cd nazwa-repo


3.2. Utwórz i aktywuj wirtualne środowisko:bash
python -m venv venv
venv\Scripts\activate    # Windows
lub
source venv/bin/activate # Linux/Mac


3.3. Zainstaluj zależności:
bash
pip install django


3.4. Wykonaj migracje:
bash
python manage.py makemigrations
python manage.py migrate


3.5. Utwórz konto administratora:
bash
python manage.py createsuperuser


3.6. Uruchom aplikację:
bash
python manage.py runserver


3.7. Otwórz przeglądarkę i wejdź na:

http://127.0.0.1:8000/


4. Wymagania

- Python 3.8+
- Django 4.x

5. Autor
Projekt wykonany przez: Rafał Gad
Numer indeksu: 51294