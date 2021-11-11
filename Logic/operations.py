from Domain.Cheltuiala import get_numar_apartament, get_data, get_suma, get_tip, getNewPayment
from Logic.crud import read
import datetime


def delete_all_payments(lista_cheltuieli, numar_apartament):
    '''
    stergerea tuturor inregistrarilor pentru un apartament dat
    :param lista_cheltuieli:
    :param numar_apartament:
    :return: lista rezultata dupa stergeri
    '''
    result = []
    for i in lista_cheltuieli:
        if get_numar_apartament(i) != numar_apartament:
            result.append(i)
    return result

def handle_deleteall(lst, numar_apartament):
    nr = int(numar_apartament)
    e = read(lst, nr)
    if e is None:
        print('Nu exista inregistrarea. ')
    else:
        lst = delete_all_payments(lst, nr)
        print('Inregistrarile au fost sterse. ')
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

def search_date(lista_cheltuieli, data):
    '''
    determinare daca exista cel putin o inregistrare cu data introdusa
    :param lista_cheltuieli:
    :param data:
    :return:
    '''
    ok = 0
    for i in lista_cheltuieli:
        if get_data(i) == data:
            ok = 1
    return ok

def add_value_same_date(lista_cheltuieli, data, add):
    '''
    adunarea unei valori pentru o data citita
    :param lista_cheltuieli:
    :param data:
    :param add:
    :return: lista rezultata dupa modificari
    '''
    result = []
    for i in lista_cheltuieli:
        if get_data(i) == data:
            new = get_suma(i) + add
            apt = get_numar_apartament(i)
            tip = get_tip(i)
            new_payment = getNewPayment(apt, new, data, tip)
            result.append(new_payment)
        else:
            result.append(i)
    return result

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

def maxim_cheltuieli(lista_cheltuieli, tip):
    '''
    returneaza valoarea maxima pentru un tip de cheltuiala
    :param lista_cheltuieli:
    :param tip:
    :return: maximul
    '''
    max = 0
    for i in lista_cheltuieli:
        if get_tip(i) == tip and get_suma(i) > max:
            max = get_suma(i)
    return max

def find_apt_with_max(lista_cheltuieli, tip):
    for i in lista_cheltuieli:
        if maxim_cheltuieli(lista_cheltuieli, tip) == get_suma(i):
            print(get_numar_apartament(i))

def handle_maxpayments(lst):
    print(
        f'valoarea maxima pentru: intretinere - {maxim_cheltuieli(lst, "intretinere")} lei efectuata de apartamentul/apartamentele:')
    find_apt_with_max(lst, 'intretinere')
    print(
        f'valoarea maxima pentru: canal - {maxim_cheltuieli(lst, "canal")} lei efectuata de apartamentul/apartamentele:')
    find_apt_with_max(lst, 'canal')
    print(
        f'valoarea maxima pentru: alte cheltuieli - {maxim_cheltuieli(lst, "alte cheltuieli")} lei efectuata de apartamentul/apartamentele:')
    find_apt_with_max(lst, 'alte cheltuieli')

def ordonare_descrescator(lista_cheltuieli):
    '''
    ordonare descrescator a elementelor din lista dupa suma
    :param lista_cheltuieli:
    :return: lista sortata
    '''
    n = len(lista_cheltuieli)
    for i in range(0, n-1):
        for j in range(i+1, n):
            if get_suma(lista_cheltuieli[i]) < get_suma(lista_cheltuieli[j]):
                aux = lista_cheltuieli[i]
                lista_cheltuieli[i] = lista_cheltuieli[j]
                lista_cheltuieli[j] = aux
    return lista_cheltuieli

def handle_decreasingsort(lst):
    lst = ordonare_descrescator(lst)
    print('lista a fost ordonata.')
    return lst

def handle_sum(nr_ap, lst):
    month = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in lst:
        if get_numar_apartament(i) == nr_ap:
            m = get_data(i)
            month[m.month] = month[m.month] + get_suma(i)
    return month

def get_ap_list(lst):
    aux = []; aux = lst
    result = []
    while aux != []:
        n = get_numar_apartament(aux[0])
        result.append(n)
        aux = delete_all_payments(aux, n)
    return result


def handle_ap_sum(lst):
    s = get_ap_list(lst)
    print('Cheltuielile totale efectuate lunar de fiecare apartament: ')
    for i in s:
        m = handle_sum(i,lst)
        print(f'apartamentul {i} in urmatoarele luni: ')
        for j in m:
            if j != 0:
                print(f'{m.index(j)}: {j}')



'''
def handle_new_list(list_versions, current_version, lst):
    while current_version < len(list_versions) - 1:
        list_versions.pop()
    list_versions.append(lst[:])
    current_version += 1
    return list_versions, current_version

def handle_undo(list_versions, current_version):
    if current_version < 1:
        print("Nu se mai poate face undo.")
        return [], 0
    current_version -= 1
    return list_versions[current_version], current_version

def handle_redo(list_versions, current_version):
    if current_version == len(list_versions) - 1:
        print("Nu se mai poate face redo.")
        return list_versions[current_version], current_version
    current_version += 1
    return list_versions[current_version], current_version
'''

def handle_undo(lst, undo, redo):
    if len(undo) == 1:
        redo.append(undo[0][:])
        undo.clear()
        lst.clear()
    elif undo == []:
        print('nu se mai poate face undo.')
    else:
        n = len(undo)
        redo.append(undo[n - 1][:])
        undo.pop(n - 1)
        n = len(undo)
        lst = undo[n - 1][:]
    return lst, undo, redo

def handle_redo(lst, undo, redo):
    if redo == []:
        print('nu se mai poate face redo.')
    elif len(redo) == 1:
        lst = redo[0][:]
        redo.clear()
        undo.append(lst[:])
    else:
        n = len(redo)
        lst = redo[n - 1][:]
        undo.append(lst[:])
        redo.pop(n - 1)
    return lst, undo, redo






