""" szybka rozgrzewka zaproponowana przez tworcow pycamp-u"""
import random


class Losowanie_lotto:
    def __init__(self):
        self.losowanie = [0] * 49
        self.wylosowane = random.sample(range(1, 50), 6)
        self.oznacz_wylosowane()

    def oznacz_wylosowane(self):
        """wstawia 1 w liscie losowanie w miejsca wyznaczone przez wylosowane liczby"""
        for liczba in self.wylosowane:
            self.losowanie[liczba - 1] = 1

    def ile_trafionych(self, skreslone: list) -> int:
        """sprawdza ilosc trafionych liczb"""
        trafienia = 0
        for liczba in skreslone:
            trafienia += self.losowanie[liczba - 1]
        return trafienia


def main():
    skreslone = [2, 8, 9, 10, 12, 45]
    proby = 0
    while True:
        losowanie = Losowanie_lotto()
        losowanie.oznacz_wylosowane()
        print(losowanie.wylosowane)
        trafione = losowanie.ile_trafionych(skreslone)
        if trafione == 6:
            break
        print(f"Ilość trafień: {trafione}")
        proby += 1
        print(f"to proba nr {proby}")
    print(f"Probowales {proby} zanim trafiles 6tke.")


if __name__ == "__main__":
    main()
