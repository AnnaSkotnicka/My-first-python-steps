import anagramy2
import pytest


@pytest.mark.parametrize("slowo, result", [("123", False),
                                           ("krab", True),
                                           ("   krab", True),
                                           ("krab   ", True),
                                           ("krab123", False),
                                           ("krab@", False)
                                           ])
def test_tylko_litery(slowo, result):
    assert anagramy2.tylko_litery(slowo) == result
