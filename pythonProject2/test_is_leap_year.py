import pytest
from main import isLeapYear


def test_year_divisible_by_4_and_not_by_100_is_leap_year():
    assert isLeapYear(2004) == True
    assert isLeapYear(2008) == True
    assert isLeapYear(2012) == True


def test_year_divisible_by_400_is_leap_year():
    assert isLeapYear(1600) == True
    assert isLeapYear(2000) == True


def test_year_not_divisible_by_4_is_not_leap_year():
    assert isLeapYear(2001) == False
    assert isLeapYear(2002) == False
    assert isLeapYear(2003) == False
    assert isLeapYear(2005) == False


def test_year_divisible_by_100_and_not_by_400_is_not_leap_year():
    assert isLeapYear(1700) == False
    assert isLeapYear(1800) == False
    assert isLeapYear(1900) == False


# Med tanke på at det er år før 0 så burde man også beregne med det. Jeg fant ikke ut om alle samme reglene gjelder
# For år før vår tidsregning. Gikk utifra https://en.wikipedia.org/wiki/Leap_year#
def test_negative_year_divisible_by_4_and_not_by_100_is_leap_year():
    assert isLeapYear(-4) == True  # 4 fvt., som er et skuddår i den kalenderen før år 0.
    assert isLeapYear(-8) == True
    assert isLeapYear(-12) == True
    assert isLeapYear(-16) == True
