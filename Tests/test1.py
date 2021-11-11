import datetime
from Domain.Cheltuiala import getNewPayment
from Logic.crud import create
from Logic.operations import maxim_cheltuieli, handle_undo, handle_redo


def test_create():
    lst = []
    lst1 = []
    c1 = getNewPayment(6, 100, datetime.datetime(2021, 12, 4), 'canal')
    lst.append(c1)
    create(lst1, 6, 100, datetime.datetime(2021, 12, 4), 'canal')
    assert lst == lst1

def test_maxim_cheltuieli():
    c1 = getNewPayment(6, 100, datetime.datetime(2021, 12, 4), 'canal')
    c2 = getNewPayment(23, 150, datetime.datetime(2021, 10, 15), 'canal')
    lst = []; lst.append(c1); lst.append(c2)
    assert maxim_cheltuieli(lst, 'canal') == 150


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
