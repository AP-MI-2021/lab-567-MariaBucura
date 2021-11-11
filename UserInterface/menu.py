import datetime
from Domain.Cheltuiala import getNewPayment, get_data, get_numar_apartament, get_payment_string
from Logic.crud import create, read, update, delete, handle_add, handle_read,handle_update, handle_delete, handle_delete1, handle_update1, handle_read1, handle_add1
from Logic.operations import delete_all_payments, add_value_same_date, search_date, maxim_cheltuieli, find_apt_with_max, ordonare_descrescator, handle_ap_sum, handle_deleteall, handle_addvalue, handle_maxpayments, handle_decreasingsort, handle_addvalue1, handle_deleteall1, handle_undo, handle_redo


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


