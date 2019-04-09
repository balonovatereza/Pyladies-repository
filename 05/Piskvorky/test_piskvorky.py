import pytest

from piskvorky import tah, tah_pocitace, vyhodnot


def test_vyhodnot_vyhra_x():
    """
    Křížky vyhrály.
    """
    assert vyhodnot("xxx-----------------", "x", "o") == "x"
    assert vyhodnot("--------xxx---------", "x", "o") == "x"
    assert vyhodnot("-----------------xxx", "x", "o") == "x"
    assert vyhodnot("-xoxoxxxoxoxoxoxoxox", "x", "o") == "x"
    assert vyhodnot("-xooxxooxxooxxoxxxoo", "x", "o") == "x"
    assert vyhodnot("xxxoxoxoxoxoxoxoxox-", "x", "o") == "x"
    assert vyhodnot("oxxxoxoxxooxxooxxoo-", "x", "o") == "x"
    assert vyhodnot("oxoxoxoxo-oxoxoxoxxx", "x", "o") == "x"
    assert vyhodnot("xxooxxoox-ooxxooxxxo", "x", "o") == "x"


def test_vyhodnot_vyhra_o():
    """
    Kolečka vyhrála.
    """
    assert vyhodnot("ooo-----------------", "x", "o") == "o"
    assert vyhodnot("--------ooo---------", "x", "o") == "o"
    assert vyhodnot("-----------------ooo", "x", "o") == "o"
    assert vyhodnot("-xoxoxoxoooxoxoxoxox", "x", "o") == "o"
    assert vyhodnot("-xoooxooxxooxxooxxoo", "x", "o") == "o"
    assert vyhodnot("xoooxoxoxoxoxoxoxox-", "x", "o") == "o"
    assert vyhodnot("oooxxooxxooxxooxxoo-", "x", "o") == "o"
    assert vyhodnot("oxoxoxoxo-oxoxoxooox", "x", "o") == "o"
    assert vyhodnot("xxooxxoox-ooxxooxooo", "x", "o") == "o"


def test_vyhodnot_remiza():
    """
    Nastala remíza.
    """
    assert vyhodnot("oxoxoxoxoxoxoxoxoxox", "x", "o") == "!"
    assert vyhodnot("xxooxxooxxooxxooxxoo", "x", "o") == "!"


def test_vyhodnot_hra():
    """
    Hra neskončila.
    """
    assert vyhodnot("--------------------") == "-"
    assert vyhodnot("xx----------------oo") == "-"
    assert vyhodnot("-xoxoxoxoxoxoxoxoxox") == "-"
    assert vyhodnot("-xooxxooxxooxxooxxoo") == "-"
    assert vyhodnot("xoxoxoxoxoxoxoxoxox-") == "-"
    assert vyhodnot("xooxxooxxooxxooxxoo-") == "-"
    assert vyhodnot("oxoxoxoxo-oxoxoxoxox") == "-"
    assert vyhodnot("xxooxxoox-ooxxooxxoo") == "-"


def test_tah_x():
    """
    Pozitivní testy se symbolem "x".
    """
    assert tah("--------------------", 0, "x") == "x-------------------"
    assert tah("--------------------", 10, "x") == "----------x---------"
    assert tah("--------------------", 19, "x") == "-------------------x"


def test_tah_o():
    """
    Pozitivní testy se symbolem "o".
    """
    assert tah("--------------------", 0, "o") == "o-------------------"
    assert tah("--------------------", 10, "o") == "----------o---------"
    assert tah("--------------------", 19, "o") == "-------------------o"


def test_tah_pocitace_prazdne():
    """
    Hra na prázdné pole.
    """
    pole = "--------------------"
    result = tah_pocitace(pole)
    assert len(result) == 20
    assert result.count("-") == 19
    assert result.count("o") == 1


def test_tah_pocitace_skoro_plne():
    """
    Hra na skoro plné pole (volno uprostřed).
    """
    pole = "xoxoxoxoxo-xoxoxoxox"
    result = tah_pocitace(pole)
    assert len(result) == 20
    assert result.count("x") == 10
    assert result.count("o") == 10


def test_tah_pocitace_skoro_plne_zacatek():
    """
    Hra na skoro plné pole (volno na začátku).
    """
    pole = "-xoxoxoxoxoxoxoxoxox"
    result = tah_pocitace(pole)
    assert len(result) == 20
    assert result.count("x") == 10
    assert result.count("o") == 10


def test_tah_pocitace_skoro_plne_konec():
    """
    Hra na skoro plné pole (volno na konci).
    """
    pole = "xoxoxoxoxoxoxoxoxox-"
    result = tah_pocitace(pole)
    assert len(result) == 20
    assert result.count("x") == 10
    assert result.count("o") == 10


def test_tah_pocitace_skoro_plne_konec_2():
    """
    Hra na skoro plné pole (2× volno na konci).
    """
    pole = "xooxxooxoxoxoxooxx--"
    result = tah_pocitace(pole)
    assert len(result) == 20
    assert result.count("x") == 9
    assert result.count("o") == 10
    assert result.count("-") == 1


if __name__ == "__main__":
    pytest.main()
