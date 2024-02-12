# Password manager

## Opis

Aplikacja konsolowa napisana w języku python, pozwalająca użytkownikowi na manipulowanie swoimi danymi do logowania. 

Program można uruchomić przy użyciu konsoli systemowej, gdzie znajdziemy do wyboru kilka możliwych opcji, takich jak ustanowienie nowego hasła, zmiana hasła na inne czy wylistowanie wszystkich zapisanych elementów.

Dzięki temu programowi użytkownik może z łatwością zarządzać swoimi hasłami bez konieczności ręcznego wprowadzania zmian do pliku, co w przypadku dużego zbioru danych byłoby trudnym zadaniem.

## Analiza wymagań

W celu zapewnienia przejrzystości kodu i możliwości jego skalowania, utworzona została klasa o nazwie Manager, zawierająca wszystkie potrzebne metody do  optymalnego funkcjonowania programu w jego obecnej formie.

Do zapewnienia prawidłowego funkcjonowania niektórych metod, użyte zostały dekoratory, które wstępnie sprawdzają poprawność danych przed wywołaniem funkcji.

Do przechowywania danych stron i haseł, użyłem  pliku JSON. Przy użyciu metody "json.load", dane pobierane są z pliku i konwertowane na postać słownika, dzięki któremu możemy odczytywać i zmieniać wartości ze złożonością obliczeniową O(1). Po przeprowadzonych transformacjach, dane są z powrotem zapisywane metodą "json.dumps"

W celu uchronienia się przed ewentualnymi błędami, niektóre znaki są zabronione podczas ustalania hasła. Są one zawarte w samej klasie Manager i użytkownik nie może ich zmienić.

Główne działanie programu zachodzi w pliku index.py, gdzie przy użyciu pętli while wysyłamy użytkownikowi zapytania, a także udzielamy mu niezbędnych informacji. W pliku tym importujemy klasę Manager, znajdującą się w osobnym pliku manager.py. Pętla ta jest wykonywana aż do momentu, w którym użytkownik zadecyduje o zatrzymaniu programu, wciskając odpowiadający temu przycisk (opcja ta jest widoczna w konsoli).

W celu zabezpieczenia się przed niespodziewanymi błędami, wdrożone zostały także testy jednostkowe, dostępne przy użyciu komendy "python -m unittest test.py".