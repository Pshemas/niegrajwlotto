""" a short warmup task proposed by Pycamp organizers"""
import random


class Lotto_game:
    """
    Creates empty coupon and draws 6 random numbers.
    Provides methods to mark those on the coupon and count hits.
    """

    def __init__(self):
        self.playslip = [0] * 49
        self.drawn_numbers = random.sample(range(1, 50), 6)
        self.mark_drawn()

    def mark_drawn(self):
        """
        puts 1 in self.playslip cells pointed by drawn_numbers.
        """
        for liczba in self.drawn_numbers:
            self.playslip[liczba - 1] = 1

    def check_hits(self, chosen_numbers: list) -> int:
        """
        calculates number of hits returned as int.
        """
        hits = 0
        for liczba in chosen_numbers:
            hits += self.playslip[liczba - 1]
        return hits

    def draw_again(self):
        """
        Clears playslip and redraws the numbers.
        """
        self.__init__()


class Lotto_stats:
    """
    Used to record attempts, hits and calculate prize / spent balance
    """

    def __init__(self) -> None:
        self.attempts = 0
        self.summary = {3: 0, 4: 0, 5: 0, 6: 0}
        self.singlecoupon_cost = 3
        self.prize3 = 24
        self.prize4 = 100
        self.prize5 = 24
        self.prize6 = 2000000

    def calculate_balance(self) -> int:
        """
        Used to calculate how much has been spent / won.
        Returns result as int
        """
        total_spent = self.attempts * self.singlecoupon_cost
        prizes = (
            self.summary[3] * self.prize3
            + self.summary[4] * self.prize4
            + self.summary[5] * self.prize5
            + self.summary[6] * self.prize6
        )
        balance = total_spent - prizes
        return balance


def main():
    mypicks = [2, 8, 9, 10, 12, 45]
    mystats = Lotto_stats()
    game = Lotto_game()

    while mystats.summary[6] == 0:
        mystats.attempts += 1
        hits = game.check_hits(mypicks)
        if hits > 2:
            mystats.summary[hits] += 1
        game.draw_again()

    spent = mystats.calculate_balance()
    print(f"There were {mystats.attempts} attempts before 6 hits were scored")
    print(f"You've spent {spent} PLN to get there.")


if __name__ == "__main__":
    main()
