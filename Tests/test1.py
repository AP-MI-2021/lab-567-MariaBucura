import datetime
from Domain.Cheltuiala import getNewPayment, get_data, get_suma, get_tip, get_payment_string, get_numar_apartament
from Logic.crud import create, update, read, delete
from Logic.operations import maxim_cheltuieli, handle_undo, handle_redo, \
    delete_all_payments, add_value_same_date, ordonare_descrescator


def test_create():
    lst = []
    lst1 = []
    c1 = getNewPayment(6, 100, datetime.datetime(2021, 12, 4), 'canal')
    lst.append(c1)
    create(lst1, 6, 100, datetime.datetime(2021, 12, 4), 'canal')
    assert lst == lst1


def test_update():
    lst1 = []
    create(lst1, 6, 100, datetime.datetime(2021, 12, 4), 'canal')
    c1 = getNewPayment(6, 150, datetime.datetime(2021, 12, 20), 'canal')
    lst1 = update(lst1, c1)
    assert get_suma(lst1[0]) == 150
    assert get_data(lst1[0]) == datetime.datetime(2021, 12, 20)


def test_read():
    lst = []
    create(lst, 6, 100, datetime.datetime(2021, 12, 4), 'canal')
    lst1 = read(lst, 6)
    assert lst == lst1


def test_delete():
    lst = []
    create(lst, 6, 100, datetime.datetime(2021, 12, 4), 'canal')
    create(lst, 7, 200, datetime.datetime(2021, 11, 10), 'intretinere')
    lst = delete(lst, 7, 'intretinere')
    assert read(lst, 7) is None


def test_delete_all():
    lst = []
    create(lst, 6, 100, datetime.datetime(2021, 12, 4), 'canal')
    create(lst, 7, 200, datetime.datetime(2021, 11, 10), 'intretinere')
    create(lst, 6, 200, datetime.datetime(2021, 11, 22), 'alte cheltuieli')
    lst = delete_all_payments(lst, 6)
    assert read(lst, 6) is None


def test_add_value():
    lst = []
    create(lst, 6, 100, datetime.datetime(2021, 12, 4), 'canal')
    create(lst, 7, 200, datetime.datetime(2021, 11, 22), 'intretinere')
    create(lst, 6, 200, datetime.datetime(2021, 11, 22), 'alte cheltuieli')
    date = datetime.datetime(2021, 11, 22)
    value = 20
    lst = add_value_same_date(lst, date, value)
    assert get_suma(lst[1]) == 220
    assert get_suma(lst[2]) == 220


def test_maxim_cheltuieli():
    c1 = getNewPayment(6, 100, datetime.datetime(2021, 12, 4), 'canal')
    c2 = getNewPayment(23, 150, datetime.datetime(2021, 10, 15), 'canal')
    lst = []; lst.append(c1); lst.append(c2)
    assert maxim_cheltuieli(lst, 'canal') == 150

def test_sort():
    lst = []
    create(lst, 6, 100, datetime.datetime(2021, 12, 4), 'canal')
    create(lst, 7, 300, datetime.datetime(2021, 11, 22), 'intretinere')
    create(lst, 6, 200, datetime.datetime(2021, 11, 22), 'alte cheltuieli')
    lst = ordonare_descrescator(lst)
    assert get_suma(lst[0]) == 300
    assert get_suma(lst[1]) == 200
    assert get_suma(lst[2]) == 100

def test_handle_undo():
    lst = [1, 2, 3]
    undo = []
    redo = []
    undo.append(lst[:])
    lst.pop(1)
    undo.append(lst[:])
    lst, undo, redo = handle_undo(lst, undo, redo)
    assert len(lst) == 3
    assert len(undo) == 1
    assert len(redo) == 1
    lst.append(5)
    undo.append(lst[:])
    redo.clear()
    lst, undo, redo = handle_undo(lst, undo, redo)
    assert len(lst) == 3
    assert len(undo) == 1
    assert len(redo) == 1


def test_handle_redo():
    lst = [1, 2, 3]
    undo = []
    redo = []
    undo.append(lst[:])
    lst.pop(1)
    undo.append(lst[:])
    lst, undo, redo = handle_undo(lst, undo, redo)
    lst, undo, redo = handle_redo(lst, undo, redo)
    assert len(lst) == 2
    assert len(undo) == 2
    assert len(redo) == 0





def run_all_tests():
    test_create()
    test_maxim_cheltuieli()
    test_handle_undo()
    test_handle_redo()
    test_update()
    test_read()
    test_delete()
    test_delete_all()
    test_add_value()
    test_sort()

run_all_tests()
