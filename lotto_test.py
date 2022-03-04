"""
pytest unit tests for lotto.py
"""
from lotto import Lotto_game, Lotto_stats


def test_checkhits():
    testgame1 = Lotto_game()
    testgame1.drawn_numbers = [1, 2, 3, 4, 5, 6]
    testgame1.mark_drawn()
    picks = [44, 12, 8, 3, 2, 1]
    assert testgame1.check_hits(picks) == 3


def test_checkhits2():
    testgame2 = Lotto_game()
    testgame2.drawn_numbers = [1, 2, 3, 4, 5, 6]
    testgame2.mark_drawn()
    picks = [3, 2, 1, 4, 5, 6]
    assert testgame2.check_hits(picks) == 6


def test_redraw():
    testgame3 = Lotto_game()
    draw1 = testgame3.drawn_numbers[:]
    testgame3.draw_again()
    draw2 = testgame3.drawn_numbers[:]
    assert draw1 != draw2


def test_noredraw():
    testgame4 = Lotto_game()
    noredraw1 = testgame4.drawn_numbers[:]
    noredraw2 = testgame4.drawn_numbers[:]
    assert noredraw1 == noredraw2
