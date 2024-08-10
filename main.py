import random
from time import sleep

def glupie_ai(pytanie):
    pytanie = pytanie.lower()

    if "jak" in pytanie:
        odpowiedzi = [
            "Najlepiej, jeśli użyjesz zaczarowanego kompasu i śpiewasz piosenkę o kaczuszkach.",
            "Musisz najpierw znaleźć ukryty klucz pod kamieniem i odwrócić się trzy razy w lewo.",
            "Wypróbuj metodę polegającą na wrzuceniu magicznego proszku do wody i zamieszaj w lewo.",
            "To łatwe, wystarczy tylko, że znajdziesz przyjaznego dinozaura w parku.",
        ]
    elif "dlaczego" in pytanie:
        odpowiedzi = [
            "Bo wszystkie chmury postanowiły się przebrać za jednorożce.",
            "To dlatego, że woda w kranie ma plany na przyszłość.",
            "Bo w kosmosie wszystkie gwiazdy organizują wielką imprezę.",
            "Ponieważ Twoje skarpetki planują ucieczkę na koniec świata.",
        ]
    elif "co" in pytanie:
        odpowiedzi = [
            "To tajemniczy eliksir, który sprawia, że wszystko smakuje jak lody.",
            "Coś, co można znaleźć tylko w magicznych lasach pełnych mchu.",
            "To przedmiot, który zmienia kolor w zależności od tego, jak dobrze się bawi.",
            "To rzecz, która potrafi latać i śpiewać melodie z dzieciństwa.",
        ]
    elif "gdzie" in pytanie:
        odpowiedzi = [
            "W głębokim lesie, gdzie mieszkają bajkowe stworzenia.",
            "Pod dużym, fioletowym kamieniem, który świeci w ciemności.",
            "W miejscu, gdzie wszystkie liście tańczą w rytm muzyki.",
            "Na końcu tęczy, gdzie znajdują się skarby marzeń.",
        ]
    elif "kiedy" in pytanie:
        odpowiedzi = [
            "Kiedy wszystkie dinozaury będą miały swoje wakacje na Marsie.",
            "W momencie, gdy gwiazdy zaczynają tańczyć na niebie.",
            "Gdy zegar na ścianie zaczyna grać melodię z filmu o piratach.",
            "Kiedy kolorowe motyle zaczynają śpiewać kołysanki.",
        ]
    elif "ile" in pytanie:
        odpowiedzi = [
            "Tyle, ile godzin słońce spędza na niebie w letnie dni.",
            "Około 123, ale tylko wtedy, gdy woda w morzu jest spokojna.",
            "Tyle, ile ziarenek piasku jest na plaży w letnie popołudnia.",
            "Dokładnie tyle, ile kropli deszczu pada w czasie burzy.",
        ]
    elif "czemu" in pytanie:
        odpowiedzi = [
            "Bo wszystkie chmurki postanowiły zrobić sobie przerwę na kawę.",
            "To dlatego, że jednorożce mają przerwę na lunch.",
            "Ponieważ Twoja mysz komputerowa zaczęła prowadzić dziennik podróży.",
            "Bo słońce zdecydowało się na chwilę odpocząć.",
        ]
    elif "kto" in pytanie:
        odpowiedzi = [
            "To tajemnicza postać, która mieszka w magicznym lesie z klocków LEGO.",
            "Osoba, która potrafi robić lody w każdej porze roku.",
            "To ktoś, kto zna sekret najlepszej receptury na czekoladę.",
            "Nieznany bohater, który potrafi rozmawiać z roślinami.",
        ]
    elif "czy" in pytanie:
        odpowiedzi = [
            "Tak, ale tylko wtedy, gdy woda w basenie zmienia kolor na różowy.",
            "Nie, ale możesz spróbować zapytać swojego ulubionego robota kuchennego.",
            "Może, ale musisz najpierw przejść przez labirynt z cukierków.",
            "Zdecydowanie, ale tylko jeśli odwiedzisz magiczną krainę na końcu tęczy.",
        ]
    elif "gdzie" in pytanie and "mój" in pytanie:
        odpowiedzi = [
            "Twoje rzeczy są prawdopodobnie w tajemniczym miejscu, gdzie rządzi miś pluszowy.",
            "W skrzyni ukrytej w ogrodzie pełnym kwiatów.",
            "Pod Twoim łóżkiem, gdzie zaginione skarpetki lubią się ukrywać.",
            "Na dnie wielkiego kosza z zabawkami, pełnego niespodzianek.",
        ]
    elif "kiedy" in pytanie and "najlepszy" in pytanie:
        odpowiedzi = [
            "Najlepszy czas to wtedy, gdy słońce zaczyna świecić jak tęcza.",
            "Kiedy wszystkie zwierzęta w ogrodzie zaczynają tańczyć w rytm muzyki.",
            "Gdy gwiazdy zaczynają śpiewać serenady w nocy.",
            "W momencie, gdy kwiaty zaczynają pachnieć świeżymi ciasteczkami.",
        ]
    elif "jak" in pytanie and "sprawić" in pytanie:
        odpowiedzi = [
            "Spraw, by wszystko było magiczne, dodając odrobinę srebrnego pyłu.",
            "Wypróbuj sposób polegający na tańcu wokół ogniska przy świetle księżyca.",
            "Dodaj odrobinę kolorowej farby do każdego przedmiotu i patrz, jak ożywa.",
            "Zrób to, dodając trochę magicznego eliksiru do swojej codziennej herbaty.",
        ]
    else:
        odpowiedzi = [
            "Sprawdź w książce o przygodach magicznych zwierząt.",
            "Zapytaj swojego ulubionego jednorożca, on na pewno wie.",
            "Może warto poszukać odpowiedzi w książce o nieznanych krainach.",
            "Zajrzyj do tajemniczego pudełka, które schowałeś na strychu.",
        ]

    return random.choice(odpowiedzi)

# Przykłady użycia
print('By Jacek,,,,Odpowiada tylko na pytania,,,,,,,,,,,,,,,,,')
while True:
    print('***************************************************')
    pytanie = input('>>')
    print('***************************************************')
    sleep(5)
    print(glupie_ai(pytanie))
