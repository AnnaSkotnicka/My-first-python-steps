import pytest
import dzien_roku


@pytest.mark.parametrize("rok, miesiac, dzien, wynik", [(2011, 0, 28, False),  # Test miesiąca
                                          (2011, 13, 28, False),
                                          (2011, 1, 28, True),
                                          (2011, 12, 28, True),
                                          (2011, 1, 0, False),  # Test dnia
                                          (2016, 2, 28, True),
                                          (2016, 2, 29, True),
                                          (2011, 1, 32, False),
                                          (0, 1, 31, False),  # Test roku
                                          (2024, 1, 31, True),
                                           ])
def test_sprawdz_poprawnosc_daty(rok, miesiac, dzien, wynik):
    assert dzien_roku.sprawdz_poprawnosc_daty(rok, miesiac, dzien) == wynik


def test_czy_przestepny():
    assert dzien_roku.czy_przestepny(2016) is True
    assert dzien_roku.czy_przestepny(2020) is True
    assert dzien_roku.czy_przestepny(2017) is False
    assert dzien_roku.czy_przestepny(2015) is False


def test_dni_w_miesiacu():
    with pytest.raises(Exception):
        dzien_roku.dni_w_miesiacu(2023, 0)
        dzien_roku.dni_w_miesiacu(2023, 13)
    assert dzien_roku.dni_w_miesiacu(2020, 2) == 29
    assert dzien_roku.dni_w_miesiacu(2021, 2) == 28
    assert dzien_roku.dni_w_miesiacu(2021, 12) == 31


def test_dzien_w_roku():
    assert dzien_roku.dzien_w_roku(2023, 9, 5) == 248
    # with pytest.raises(Exception):
    #     dzien_roku.dzien_w_roku(2023, 20, 5)

