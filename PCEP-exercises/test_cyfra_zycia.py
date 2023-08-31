import pytest
import cyfra_zycia


@pytest.mark.parametrize("data, wynik", [("10.03.1997", "10031997"),
                                         ("10-03-1997", "10031997"),
                                         ("10,03,1997", "10031997"),
                                         ("10 03 1997", "10031997"),
                                         ("10 03 abcd", "1003abcd"),
                                         ])
def test_formatuj_dane(data, wynik):
    assert cyfra_zycia.formatuj_date(data) == wynik


@pytest.mark.parametrize("data, wynik", [("10031997", True),  # poprawna data
                                         ("1003199", False),  # za krótka o jedną cyfrę
                                         ("100319976", False),  # za długa o jedną cyfrę
                                         ("1003i99", False),  # zawiera literkę
                                         ("35021999", False),  # test dnia w dacie
                                         ("00021999", False),  # test dnia w dacie
                                         ("21161999", False),  # test miesiąca w dacie
                                         ("21001999", False),  # test miesiąca w dacie
                                         ("21052022", False),  # test roku w dacie
                                         ("21051000", False)])  # test roku w dacie
def test_czy_data_jest_poprawna(data, wynik):
    assert cyfra_zycia.czy_data_jest_poprawna(data) == wynik


def test_suma():
    assert cyfra_zycia.suma("10031997") == 30
    assert cyfra_zycia.suma("19081991") == 38


def test_spr_cyfry(capsys):
    cyfra_zycia.spr_cyfry(3)
    out, err = capsys.readouterr()
    assert out == "Twoja szczęśliwa liczba to: 3\n"

    cyfra_zycia.spr_cyfry(21)
    out, err = capsys.readouterr()
    assert out == "Twoja szczęśliwa liczba to: 3\n"

