import datetime
from Domain.Cheltuiala import getNewPayment, get_data, get_numar_apartament, get_payment_string
from Logic.crud import create, read, update, delete, handle_add, handle_read,handle_update, handle_delete
from Logic.operations import delete_all_payments, add_value_same_date, search_date, maxim_cheltuieli, find_apt_with_max, ordonare_descrescator, handle_undo, handle_redo, handle_new_list, handle_ap_sum, handle_deleteall, handle_addvalue, handle_maxpayments, handle_decreasingsort



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
        list_versions = [lst]
        current_version = 0
        while True:
            command = input()
            command = command.split(';')
            for i in command:
                i = i.split(',')
                if i[0] == 'add':
                    handle_add(lst, i[1], i[2], i[3], i[4], i[5], i[6])
                    list_versions, current_version = handle_new_list(list_versions, current_version, lst)
                elif i[0] == 'showall':
                    print(lst)
                elif i[0] == 'read':
                    handle_read(lst, i[1])
                elif i[0] == 'modify':
                    lst = handle_update(lst, i[1], i[2], i[3], i[4], i[5], i[6])
                    list_versions, current_version = handle_new_list(list_versions, current_version, lst)
                elif i[0] == 'delete':
                    lst = handle_delete(lst, i[1], i[2])
                    list_versions, current_version = handle_new_list(list_versions, current_version, lst)
                elif i[0] == 'deleteall':
                    lst = handle_deleteall(lst, i[1])
                    list_versions, current_version = handle_new_list(list_versions, current_version, lst)
                elif i[0] == 'addvalue':
                    lst = handle_addvalue(lst, i[1], i[2], i[3], i[4])
                    list_versions, current_version = handle_new_list(list_versions, current_version, lst)
                elif i[0] == 'showmaxpayment':
                    handle_maxpayments(lst)
                elif i[0] == 'decreasingsort':
                    lst = handle_decreasingsort(lst)
                    list_versions, current_version = handle_new_list(list_versions, current_version, lst)
                elif i[0] == 'showlunarpayments':
                    handle_ap_sum(lst)
                elif i[0] == 'undo':
                    lst, current_version = handle_undo(list_versions, current_version)
                elif i[0] == 'redo':
                    lst, current_version = handle_redo(list_versions, current_version)

            n = len(command)
            if command[n - 1] == 'quit':
                break
    except:
        print('an exception occured')

menu()