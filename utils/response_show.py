import json

from pygments import highlight, lexers, formatters


class ResponseShow:

    @staticmethod
    def show_r(r):
        # Console colors:
        c_green = '\033[92m'
        c_end = '\033[0m'
        # Status code:
        print(f"{c_green}\nStatus: {r.status_code}")
        # Time:
        print(f"Time: {r.elapsed.total_seconds()}")
        # Size:
        print(f"Size: {len(r.content)}{c_end}")
        # Response JSON:
        formatted_json = json.dumps(r.json(), ensure_ascii=False, indent=4)
        colorful_json = highlight(formatted_json, lexers.JsonLexer(), formatters.TerminalFormatter())
        print(colorful_json)

    @staticmethod
    def show_optional(r):
        # Console colors:
        c_purple = '\033[35m'
        c_end = '\033[0m'
        # Request url:
        print(f"{c_purple}Request URL: {r.url}")
        # Headers:
        print(f"Request headers:\n{json.dumps(dict(r.headers), indent=4)}")
        # Cookies:
        print(f"Request cookies: {r.cookies}{c_end}")

    @staticmethod
    def show_bad_json(r):
        print(r.text)


"""
NOTES: --------------------------------------------------------------------------------------------------------------

____________________________________________________________
WYŚWIETLANIE ELEMENTÓW:

print(r) - kod odpowiedzi requesta w takiej formie: <Response>[200]
print(r.status_code) - sam kod odpowiedzi requesta
print(r.elapsed.total_seconds()) - czas odpowiedzi requesta
print(len(r.content)) - rozmiar samej odpowiedzi. Nie pokazuje wagi całości, łącznie z nagłówkami jak to robi Postman.

print(r.url) - adres requesta
print(r.headers) - nagłówki requesta
print(r.cookies) - ciasteczka requesta

____________________________________________________________
WYŚWIETLANIE I FORMATOWANIE JSONA ODPOWIEDZI:

Dla czytelniejszego wyświetlania response'a oraz jego headers warto sformatować wyświetlany JSON.
Służy do tego metoda:
json.dumps(obiektJSON, indent=4)
indent=4 - to ilość spacji używana do układania elementów

Wyświetlanie dla body response'a:
print(json.dumps(r.json(), indent=4))
Dla 'r' trzeba zawsze określić czy chcemy mieć go wyświetlany jako string (r.text) lub JSON (r.json())

ensure_ascii=False
Wyświetla polskie znaki

Wyświetlanie dla nagłówków requesta:
print(json.dumps(dict(r.headers), indent=4))
Headersy są tutaj zwracane jako CaseInsensitiveDict.
json.dumps takich obiektów nie przyjmuje i dlatego tutaj zamieniamy go na zwykłe dictionary.

Kolorowanie JSONA body:
Jeżeli chcemy mieć wyświetlany JSON bardziej przyjazny dla oka to możemy mu nadać kolory.
Potrzebne jest do tego zainstalowanie: Pygments (pip install Pygments)
Strona z dokumentacją:
https://pygments.org/

Tak wyglądałby domyślny zapis pokolorowanego JSON'a odpowiedzi:

formatted_json = json.dumps(r.json(), indent=4)
colorful_json = highlight(formatted_json, lexers.JsonLexer(), formatters.TerminalFormatter())
print(colorful_json)

____________________________________________________________
KOLOROWANIE KONSOLI:

Źródło: https://stackoverflow.com/questions/287871/how-to-print-colored-text-to-the-terminal

Definiujemy najpierw kolor startowy i końcowy. Chociaż od różnych miejsc można używać innych.
c_green = '\033[92m'
c_end = '\033[0m'

Następnie wstawiamy je w printach:

        # Status code:
        print(f"{c_green}\nStatus: {r.status_code}")
        # Time:
        print(f"Time: {r.elapsed.total_seconds()}")
        # Size:
        print(f"Size: {len(r.content)}{c_end}")

"""
