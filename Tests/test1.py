import datetime
from Domain.Cheltuiala2 import getNewPayment
from Logic.crud import create


def test_create():
    lst = []
    lst1 = []
    c1 = getNewPayment(6, 100, datetime.datetime(2021, 12, 4), 'canal')
    lst.append(c1)
    create(lst1, 6, 100, datetime.datetime(2021, 12, 4), 'canal')
    assert lst == lst1


