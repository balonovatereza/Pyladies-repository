import pytest

from piskvorky import tah, vyhodnot
from ai import tah_pocitace


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
    assert vyhodnot("xoxxooxoxxxooxo-xo--xo", "x", "o") == "x"
    assert vyhodnot("xo-ox-oxxxo---ox------", "x", "o") == "x"
    assert vyhodnot("xxxxooxo-xo--xo", "x", "o") == "x"
    assert vyhodnot("xo-ox-oxxxo----", "x", "o") == "x"


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
    assert vyhodnot("xoxoxooxoooxoxx-xoxo", "x", "o") == "o"
    assert vyhodnot("ox-xo-xooox---xo----", "x", "o") == "o"
    assert vyhodnot("xoxoxooxoooxoxx-", "x", "o") == "o"
    assert vyhodnot("ox-xo-xooox---xo", "x", "o") == "o"
    assert vyhodnot("oxoxoxoxo-oxoxoxooox---", "x", "o") == "o"
    assert vyhodnot("---xxooxxoox-ooxxooxooo", "x", "o") == "o"


def test_vyhodnot_remiza():
    """
    Nastala remíza.
    """
    assert vyhodnot("oxoxoxoxoxoxoxoxoxox", "x", "o") == "!"
    assert vyhodnot("xxooxxooxxooxxooxxoo", "x", "o") == "!"
    assert vyhodnot("xoxxoxooxoxxooxoxoox", "x", "o") == "!"
    assert vyhodnot("oxxooxoxoxxooxoxoxxo", "x", "o") == "!"
    assert vyhodnot("xoxxoxooxoxxoo", "x", "o") == "!"
    assert vyhodnot("oxoxxooxoxoxxo", "x", "o") == "!"
    assert vyhodnot("xoxoxxooxoxooxxoxoxooxxo", "x", "o") == "!"
    assert vyhodnot("oxoxooxxoxoxxooxoxoxxoox", "x", "o") == "!"


def test_vyhodnot_hra():
    """
    Hra neskončila.
    """
    assert vyhodnot("--------------------", "x", "o") == "-"
    assert vyhodnot("xx----------------oo", "x", "o") == "-"
    assert vyhodnot("-xoxoxoxoxoxoxoxoxox", "x", "o") == "-"
    assert vyhodnot("-xooxxooxxooxxooxxoo", "x", "o") == "-"
    assert vyhodnot("xoxoxoxoxoxoxoxoxox-", "x", "o") == "-"
    assert vyhodnot("xooxxooxxooxxooxxoo-", "x", "o") == "-"
    assert vyhodnot("oxoxoxoxo-oxoxoxoxox", "x", "o") == "-"
    assert vyhodnot("xxooxxoox-ooxxooxxoo", "x", "o") == "-"
    assert vyhodnot("xo------xox-------ox", "x", "o") == "-"
    assert vyhodnot("ox------oxo-------xo", "x", "o") == "-"


def test_tah_x():
    """
    Pozitivní testy se symbolem "x".
    """
    assert tah("--------------------", 0, "x") == "x-------------------"
    assert tah("--------------------", 10, "x") == "----------x---------"
    assert tah("--------------------", 19, "x") == "-------------------x"
    assert tah("--------------------", 3, "x") == "---x----------------"
    assert tah("--------------------", 16, "x") == "----------------x---"
    # pole = "-" * 20
    # for i in range(len(pole)):
    #     assert tah(pole, i, "x") == "".join((pole[:i], "x", pole[1 + i:]))


def test_tah_o():
    """
    Pozitivní testy se symbolem "o".
    """
    assert tah("--------------------", 0, "o") == "o-------------------"
    assert tah("--------------------", 10, "o") == "----------o---------"
    assert tah("--------------------", 19, "o") == "-------------------o"
    assert tah("--------------------", 3, "o") == "---o----------------"
    assert tah("--------------------", 16, "o") == "----------------o---"
    # pole = "-" * 20
    # for i in range(len(pole)):
    #    assert tah(pole, i, "o") == "".join((pole[:i], "o", pole[1 + i:]))


def test_tah_pocitace_prazdne():
    """
    Hra na prázdné pole.
    """
    pole = "--------------------"
    result = tah_pocitace(pole, "o", "x", 20)
    assert len(result) == 20
    assert result.count("-") == 19
    assert result.count("o") == 1

    pole2 = "------------------------------"
    result = tah_pocitace(pole2, "o", "x", 30)
    assert len(result) == 30
    assert result.count("-") == 29
    assert result.count("o") == 1

    pole3 = "------"
    result = tah_pocitace(pole3, "o", "x", 6)
    assert len(result) == 6
    assert result.count("-") == 5
    assert result.count("o") == 1


def test_tah_pocitace_skoro_plne():
    """
    Hra na skoro plné pole (volno uprostřed).
    """
    pole = "xoxoxoxoxo-xoxoxoxox"
    result = tah_pocitace(pole, "o", "x", 20)
    assert len(result) == 20
    assert result.count("x") == 10
    assert result.count("o") == 10


def test_tah_pocitace_skoro_plne_zacatek():
    """
    Hra na skoro plné pole (volno na začátku).
    """
    pole = "-xoxoxoxoxoxoxoxoxox"
    result = tah_pocitace(pole, "o", "x", 20)
    assert len(result) == 20
    assert result.count("x") == 10
    assert result.count("o") == 10


def test_tah_pocitace_skoro_plne_konec():
    """
    Hra na skoro plné pole (volno na konci).
    """
    pole = "xoxoxoxoxoxoxoxoxox-"
    result = tah_pocitace(pole, "o", "x", 20)
    assert len(result) == 20
    assert result.count("x") == 10
    assert result.count("o") == 10


def test_tah_pocitace_skoro_plne_konec_2():
    """
    Hra na skoro plné pole (2× volno na konci).
    """
    pole = "xooxxooxoxoxoxooxx--"
    result = tah_pocitace(pole, "o", "x", 20)
    assert len(result) == 20
    assert result.count("x") == 9
    assert result.count("o") == 10
    assert result.count("-") == 1


def test_tah_pocitace_pole_ruzne_delky():
    """
    Hra na pole ruzne delky.
    """
    # pole = ""
    # with pytest.raises(ValueError):
    #    tah_pocitace(pole, "o", "x", 0)

    # pole = "-"
    # with pytest.raises(ValueError):
    #     tah_pocitace(pole, "o", "x", 1)

    # pole = "---"
    # with pytest.raises(ValueError):
    #     tah_pocitace(pole, "o", "x", 3)

    for i in range(6):
        pole = i * "-"
        with pytest.raises(ValueError):
            tah_pocitace(pole, "o", "x", i)

    for i in range(6, 50):
        pole = i * "-"
        result = tah_pocitace(pole, "o", "x", i)
        assert len(result) == i
        assert result.count("o") == 1
        assert result.count("-") == i - 1


def test_tah_pocitace_plne_pole():
    """
    Hra na plne pole.
    """
    pole = "xoxoxoxoxoxoxoxoxoxo"
    with pytest.raises(ValueError):
        tah_pocitace(pole, "o", "x", 20)


if __name__ == "__main__":
    pytest.main()
