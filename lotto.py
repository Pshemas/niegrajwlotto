""" szybka rozgrzewka zaproponowana przez tworcow pycamp-u"""
import random


class Losowanie_lotto:
    """
    Tworzy kupon lotto jako listę długości 49
    i zaznacza w nim 6 losowych liczb.
    """

    def __init__(self):
        self.losowanie = [0] * 49
        self.wylosowane = random.sample(range(1, 50), 6)
        self.oznacz_wylosowane()

    def oznacz_wylosowane(self):
        """
        wstawia 1 w liscie losowanie w miejsca wyznaczone przez wylosowane liczby
        """
        for liczba in self.wylosowane:
            self.losowanie[liczba - 1] = 1

    def ile_trafionych(self, skreslone: list) -> int:
        """
        sprawdza ilosc trafionych liczb.
        """
        trafienia = 0
        for liczba in skreslone:
            trafienia += self.losowanie[liczba - 1]
        return trafienia


def losuj_szostke(skreslone: list):
    """
    przeprowadza losowanie tak dlugo, az trafi szostke.
    Przyjmuje listę z 6 wybranymi liczbami jako argument.
    Zwraca ilosc losowan (int) i podsumowaniem trafien{dict).
    """

    proby = 1
    wyniki = {3: 0, 4: 0, 5: 0, 6: 0}

    while True:
        losowanie = Losowanie_lotto()
        losowanie.oznacz_wylosowane()
        trafione = losowanie.ile_trafionych(skreslone)
        if trafione > 2:
            wyniki[trafione] += 1

        if trafione == 6:
            break

        proby += 1

    return proby, wyniki


def policz_koszt_kuponow(ilosckuponow: int) -> float:
    """
    Liczy ile kosztowały kupony lotto
    """
    cena_kuponu = 3.0
    return cena_kuponu * ilosckuponow


def main():
    mojeliczby = [2, 8, 9, 10, 12, 45]
    iledoszostki = losuj_szostke(mojeliczby)
    wydano = policz_koszt_kuponow(iledoszostki[0])
    print(
        f"Szóstka trafiona za {iledoszostki[0]} podejściem. \n Wydano na kupony {wydano} PLN."
    )
    print(
        f"Przed szostką było {iledoszostki[1][3]} trójek, {iledoszostki[1][4]} czwórek, {iledoszostki[1][5]} piątek."
    )
    bilans = (
        wydano
        - iledoszostki[1][5] * 5300
        - iledoszostki[1][4] * 100
        - iledoszostki[1][3] * 24
    )
    print(f"Biorąc pod uwagę wypłacane średnie wydałeś {bilans}.")


if __name__ == "__main__":
    main()
