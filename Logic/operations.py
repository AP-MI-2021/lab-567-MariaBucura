from Domain.Cheltuiala import get_numar_apartament, get_data, get_suma, get_tip, getNewPayment


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
    print(lista_cheltuieli)
