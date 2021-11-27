import datetime
from Domain.Cheltuiala import getNewPayment, get_data, get_numar_apartament, get_payment_string
from Logic.crud import create, read, update, delete
from Logic.operations import delete_all_payments, add_value_same_date, search_date, maxim_cheltuieli, find_apt_with_max, ordonare_descrescator, handle_undo, handle_redo, handle_ap_sum, handle_maxpayments


def handle_read(lst, numar_apartament):
    search = int(numar_apartament)
    e = read(lst, search)
    if e is None:
        print('Nu exista astfel de inregistrari.')
    else:
        print(f'Inregistrarile pentru apartamentul {search}: ')
        print(e)


def handle_add(lst, numar_apartament, suma, yyyy, mm, dd, tip):
    nr = int(numar_apartament)
    sum = int(suma)
    year = int(yyyy)
    month = int(mm)
    day = int(dd)
    date = datetime.datetime(year, month, day)
    create(lst, nr, sum, date, tip)


def handle_update(lst, nr_apartament, suma, anul, luna, ziua, tipul):
    nr = int(nr_apartament)
    sum = int(suma)
    yyyy = int(anul)
    mm = int(luna)
    dd = int(ziua)
    data = datetime.datetime(yyyy, mm, dd)
    e = read(lst, nr)
    if e is None:
        print('Nu exista inregistrarea. ')
    else:
        new = getNewPayment(nr, sum, data, tipul)
        lst = update(lst, new)
        print(f'Inregistrarea ({nr}, {tipul}) a fost modificata')
    return lst


def handle_delete(lst, numar_apartament, tip):
    nr = int(numar_apartament)
    e = read(lst, nr)
    if e is None:
        print('Nu exista inregistrarea. ')
    else:
        lst = delete(lst, nr, tip)
        print('Inregistrarea a fost stearsa.')
    return lst


def handle_deleteall(lst, numar_apartament):
    nr = int(numar_apartament)
    e = read(lst, nr)
    if e is None:
        print('Nu exista inregistrarea. ')
    else:
        lst = delete_all_payments(lst, nr)
        print('Inregistrarile au fost sterse. ')
    return lst


def handle_addvalue(lst, anul, luna, ziua, valoarea):
    yyyy = int(anul); mm = int(luna); dd = int(ziua); v = int(valoarea)
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
    print('Introduceti comenzile pe o singura linie separate de cate un ";". parametrii fiecarei comenzi vor fi separati prin ",".')
    print('Comenzi posibile: ')
    print('add,numar_apartament,suma,YYYY,MM,DD,tip')
    print('read,numar_apartament')
    print('modify,numar_apartament,suma,YYYY,MM,DD,tip')
    print('delete,numar_apartament,tip')
    print('deleteall,numar_apartament')
    print('addvalue,YYYY,MM,DD,valoare')
    print('showmaxpayment')
    print('decreasingsort')
    print('showlunarpayments')
    print('undo')
    print('redo')
    print('showall')


def menu():
    try:
        show_menu()
        lst = []
        undo = []
        redo = []
        while True:
            command = input()
            command = command.split(';')
            for i in command:
                i = i.split(',')
                if i[0] == 'add':
                    handle_add(lst, i[1], i[2], i[3], i[4], i[5], i[6])
                    undo.append(lst[:])
                    redo.clear()
                elif i[0] == 'showall':
                    print(lst)
                elif i[0] == 'read':
                    handle_read(lst, i[1])
                elif i[0] == 'modify':
                    lst = handle_update(lst, i[1], i[2], i[3], i[4], i[5], i[6])
                    undo.append(lst[:])
                    redo.clear()
                elif i[0] == 'delete':
                    lst = handle_delete(lst, i[1], i[2])
                    undo.append(lst[:])
                    redo.clear()
                elif i[0] == 'deleteall':
                    lst = handle_deleteall(lst, i[1])
                    undo.append(lst[:])
                    redo.clear()
                elif i[0] == 'addvalue':
                    lst = handle_addvalue(lst, i[1], i[2], i[3], i[4])
                    undo.append(lst[:])
                    redo.clear()
                elif i[0] == 'showmaxpayment':
                    handle_maxpayments(lst)
                elif i[0] == 'decreasingsort':
                    lst = handle_decreasingsort(lst)
                    undo.append(lst[:])
                    redo.clear()
                elif i[0] == 'showlunarpayments':
                    handle_ap_sum(lst)
                elif i[0] == 'undo':
                    lst, undo, redo = handle_undo(lst, undo, redo)
                elif i[0] == 'redo':
                    lst, undo, redo = handle_redo(lst, undo, redo)

            n = len(command)
            if command[n - 1] == 'quit':
                break
    except:
        print('an exception occured')

