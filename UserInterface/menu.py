import datetime
from Domain.Cheltuiala import getNewPayment, get_data, get_numar_apartament, get_payment_string
from Logic.crud import create, read, update, delete
from Logic.operations import delete_all_payments, add_value_same_date, search_date, maxim_cheltuieli, find_apt_with_max, ordonare_descrescator, handle_undo, handle_redo, handle_new_list, handle_ap_sum




def menu():
    try:
        lst = []
        list_versions = [lst]
        current_version = 0
        while True:
            print('alege optiunea: 1.1 , 1.2 , 1.3 , 1.4 , 1.5 , 1.6 ')
            print('x - Iesire din program.')
            print('a - vizualizare inregistrari.')
            print('u - undo.')
            print('r - redo.')
            optiune = input()
            if optiune == '1.1':
                while True:
                    print('1. Inregistrare noua.')
                    print('2. Cautare inregistrare.')
                    print('3. Modificare inregistrare')
                    print('4. Stergere inregistrare')
                    opt = input()
                    if opt == '1':
                        nr_apt = int(input('Apartament: '))
                        sum = int(input('Suma platita: '))
                        data = datetime.datetime(int(input('Anul: ')), int(input('Luna: ')), int(input('Ziua: ')))
                        paymnt = input('Tipul cheltuielii: ')
                        create(lst, nr_apt, sum, data, paymnt)
                        print('Inregistrarea a fost adaugata. ')
                        list_versions, current_version = handle_new_list(list_versions, current_version, lst)
                        x = input('Doriti sa efectuati o alta actiune? da/nu')
                        while x != 'da' and x != 'nu':
                            print('Optiune Invalida! Introduceti din nou.')
                            x = input()
                        if x == 'nu':
                            break
                    elif opt == '2':
                        search = int(input('Introduce numarul apartamentului pe care vrei sa-l cauti: '))
                        e = read(lst, search)
                        if e is None:
                            print('Nu exista astfel de inregistrari.')
                        else:
                            print(f'Inregistrarile pentru apartamentul {search}: ')
                            print(e)
                        x = input('Doriti sa efectuati o alta actiune? da/nu')
                        while x != 'da' and x != 'nu':
                            print('Optiune Invalida! Introduceti din nou.')
                            x = input()
                        if x == 'nu':
                            break
                    elif opt == '3':
                        print('Alegeti apartamentul si tipul de cheltuiala la care doresti sa faci modificari: ')
                        apt = int(input('Apartament: '))
                        tip = input('Tipul: ')
                        e = read(lst, apt)
                        if e is None:
                            print('Nu exista inregistrarea. ')
                        else:
                            print('Introdu noile date: ')
                            plata = int(input('Suma: '))
                            dat = datetime.datetime(int(input('Anul: ')), int(input('Luna: ')),
                                                    int(input('Ziua: ')))
                            new = getNewPayment(apt, plata, dat, tip)
                            lst = update(lst, new)
                            print('Inregistrarea a fost modificata.')
                            list_versions, current_version = handle_new_list(list_versions, current_version, lst)
                        x = input('Doriti sa efectuati o alta actiune? da/nu')
                        while x != 'da' and x != 'nu':
                            print('Optiune Invalida! Introduceti din nou.')
                            x = input()
                        if x == 'nu':
                            break
                    elif opt == '4':
                        print('Alege nr apartamentului si tipul inregistrarii: ')
                        apt = int(input('Apartament: '))
                        tip = input('Tipul: ')
                        e = read(lst, apt)
                        if e is None:
                            print('Nu exista inregistrarea. ')
                        else:
                            lst = delete(lst, apt, tip)
                            print('Inregistrarea a fost stearsa.')
                            list_versions, current_version = handle_new_list(list_versions, current_version, lst)
                        x = input('Doriti sa efectuati o alta actiune? da/nu')
                        while x != 'da' and x != 'nu':
                            print('Optiune Invalida! Introduceti din nou.')
                            x = input()
                        if x == 'nu':
                            break
                    else:
                        print('Optiune Invalida!')
            elif optiune == '1.2':
                print('Stergere inregistrari pentru un apartament.')
                nr_apt = int(input('Alegeti numarul apartamentului: '))
                e = read(lst, nr_apt)
                if e is None:
                    print('Nu exista inregistrarea. ')
                else:
                    lst = delete_all_payments(lst, nr_apt)
                    print('Inregistrarile au fost sterse. ')
                    list_versions, current_version = handle_new_list(list_versions, current_version, lst)
            elif optiune == '1.3':
                add = int(input('Introduceti valoarea: '))
                print('Introduceti data: ')
                dat = datetime.datetime(int(input()), int(input()), int(input()))
                ok = search_date(lst, dat)
                if ok == 0:
                    print('Nu exista inregistrari cu data introdusa.')
                else:
                    lst = add_value_same_date(lst, dat, add)
                    print('Inregistrarile au fost modificate.')
                    list_versions, current_version = handle_new_list(list_versions, current_version, lst)
            elif optiune == '1.4':
                print(
                    f'valoarea maxima pentru: intretinere - {maxim_cheltuieli(lst, "intretinere")} lei efectuata de apartamentul/apartamentele:')
                find_apt_with_max(lst, 'intretinere')
                print(
                    f'valoarea maxima pentru: canal - {maxim_cheltuieli(lst, "canal")} lei efectuata de apartamentul/apartamentele:')
                find_apt_with_max(lst, 'canal')
                print(
                    f'valoarea maxima pentru: alte cheltuieli - {maxim_cheltuieli(lst, "alte cheltuieli")} lei efectuata de apartamentul/apartamentele:')
                find_apt_with_max(lst, 'alte cheltuieli')
            elif optiune == '1.5':
                lst = ordonare_descrescator(lst)
                print('lista a fost ordonata.')
                list_versions, current_version = handle_new_list(list_versions, current_version, lst)
            elif optiune == '1.6':
                handle_ap_sum(lst)
            elif optiune == 'x':
                break
            elif optiune == 'a':
                print(lst)
            elif optiune == 'u':
                lst, current_version = handle_undo(list_versions, current_version)
            elif optiune == 'r':
                lst, current_version = handle_redo(list_versions, current_version)
            else:
                print('Optiune Invalida!')
    except:
        print('an exception occured')


