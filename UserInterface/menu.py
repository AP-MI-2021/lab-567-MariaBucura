import datetime
from Domain.Cheltuiala import getNewPayment, get_data, get_numar_apartament, get_payment_string
from Logic.crud import create, read, update, delete
from Logic.operations import delete_all_payments, add_value_same_date, search_date, maxim_cheltuieli, find_apt_with_max, ordonare_descrescator, handle_ap_sum, handle_maxpayments, handle_undo, handle_redo


def handle_read1(lst):
    search = int(input('numar apartament: '))
    e = read(lst, search)
    if e is None:
        print('Nu exista astfel de inregistrari.')
    else:
        print(f'Inregistrarile pentru apartamentul {search}: ')
        print(e)


def handle_add1(lst):
    nr = int(input('numar apartament: '))
    sum = int(input('suma: '))
    year = int(input('anul: '))
    month = int(input('luna: '))
    day = int(input('ziua: '))
    tip = input('tipul: ')
    date = datetime.datetime(year, month, day)
    create(lst, nr, sum, date, tip)
    print('Inregistrarea a fost adaugata.')
    return lst


def handle_update1(lst):
    print('Introduceti numarul si tipul: ')
    nr = int(input('nr apartament: '))
    tip = input('tipul: ')
    print('Introduceti noile date: ')
    sum = int(input('suma: '))
    yyyy = int(input('anul: '))
    mm = int(input('luna: '))
    dd = int(input('ziua: '))
    data = datetime.datetime(yyyy, mm, dd)
    new = getNewPayment(nr, sum, data, tip)
    lst = update(lst, new)
    print(f'Inregistrarea ({nr}, {tip}) a fost modificata')
    return lst


def handle_delete1(lst):
    nr = int(input('numar apartament: '))
    tip = input('tipul: ')
    lst = delete(lst, nr, tip)
    print('Inregistrarea a fost stearsa.')
    return lst


def handle_deleteall1(lst):
    nr = int(input('Apartamentul: '))
    e = read(lst, nr)
    if e is None:
        print('Nu exista inregistrarea. ')
    else:
        lst = delete_all_payments(lst, nr)
        print('Inregistrarile au fost sterse. ')
    return lst


def handle_addvalue1(lst):
    yyyy = int(input('anul: ')); mm = int(input('luna: ')); dd = int(input('ziua: ')); v = int(input('valoarea: '))
    data = datetime.datetime(yyyy, mm, dd)
    ok = search_date(lst, data)
    if ok == 0:
        print('Nu exista inregistrari cu data introdusa.')
    else:
        lst = add_value_same_date(lst, data, v)
        print('Inregistrarile au fost modificate.')
    return lst


def handle_decreasingsort(lst):
    lst = ordonare_descrescator(lst)
    print('lista a fost ordonata.')
    return lst


def show_menu():
    print('alege optiunea: ')
    print('1 - adaugare inregistrari.')
    print('2 - cautare inregistrare.')
    print('3 - modificare inregistrare.')
    print('4 - stergere inregistrare.')
    print('5 - Ștergerea tuturor cheltuielilor pentru un apartament dat.')
    print('6 - Adunarea unei valori la toate cheltuielile dintr-o dată citită.')
    print('7 - Determinarea celei mai mari cheltuieli pentru fiecare tip de cheltuială.')
    print('8 - Ordonarea cheltuielilor descrescător după sumă.')
    print('9 - Afișarea sumelor lunare pentru fiecare apartament.')
    print('x - Iesire din program.')
    print('a - vizualizare inregistrari.')
    print('u - undo.')
    print('r - redo.')

def menu():
    show_menu()
    try:
        lst = []
        undo = []
        redo = []
        while True:
            optiune = input()
            if optiune == '1':
                lst = handle_add1(lst)
                undo.append(lst[:])
                redo.clear()
            elif optiune == '2':
                handle_read1(lst)
            elif optiune == '3':
                lst = handle_update1(lst)
                undo.append(lst[:])
                redo.clear()
            elif optiune == '4':
                lst = handle_delete1(lst)
                undo.append(lst[:])
                redo.clear()
            elif optiune == '5':
                lst = handle_deleteall1(lst)
                undo.append(lst[:])
                redo.clear()
            elif optiune == '6':
                lst = handle_addvalue1(lst)
                undo.append(lst[:])
                redo.clear()
            elif optiune == '7':
                handle_maxpayments(lst)
            elif optiune == '8':
                lst = handle_decreasingsort(lst)
                undo.append(lst[:])
                redo.clear()
            elif optiune == '9':
                handle_ap_sum(lst)
            elif optiune == 'x':
                break
            elif optiune == 'a':
                print(lst)
            elif optiune == 'u':
                lst, undo, redo = handle_undo(lst, undo, redo)
            elif optiune == 'r':
                lst, undo, redo = handle_redo(lst, undo, redo)
            else:
                print('Optiune Invalida!')
    except:
        print('an exception occured')


