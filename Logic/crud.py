import datetime
from Domain.Cheltuiala import getNewPayment, get_numar_apartament, get_tip


def create(lista_cheltuieli: list, _numar_apartament: int, _suma: int, _data: datetime, _tip: str):
    cheltuiala = getNewPayment(_numar_apartament, _suma, _data, _tip)
    lista_cheltuieli.append(cheltuiala)
    return lista_cheltuieli

def handle_add(lst, numar_apartament, suma, yyyy, mm, dd, tip):
    nr = int(numar_apartament)
    sum = int(suma)
    year = int(yyyy)
    month = int(mm)
    day = int(dd)
    date = datetime.datetime(year, month, day)
    create(lst, nr, sum, date, tip)

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

def read(lista_cheltuieli: list, numar_apartament: int = None):
    if numar_apartament is None:
        return lista_cheltuieli

    lista_cheltuieli_gasite = []

    for i in lista_cheltuieli:
        if get_numar_apartament(i) == numar_apartament:
            cheltuiala_gasita = i
            lista_cheltuieli_gasite.append(cheltuiala_gasita)

    if lista_cheltuieli_gasite == []:
        return None

    return lista_cheltuieli_gasite

def handle_read(lst, numar_apartament):
    search = int(numar_apartament)
    e = read(lst, search)
    if e is None:
        print('Nu exista astfel de inregistrari.')
    else:
        print(f'Inregistrarile pentru apartamentul {search}: ')
        print(e)

def handle_read1(lst):
    search = int(input('numar apartament: '))
    e = read(lst, search)
    if e is None:
        print('Nu exista astfel de inregistrari.')
    else:
        print(f'Inregistrarile pentru apartamentul {search}: ')
        print(e)

def update(lista_cheltuieli, new_payment):
    result = []
    for i in lista_cheltuieli:
        if get_numar_apartament(i) == get_numar_apartament(new_payment) and get_tip(i) == get_tip(new_payment):
            result.append(new_payment)
        else:
            result.append(i)
    return result

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

def delete(lista_cheltuieli, numar_apartament, tip):
    result = []
    for i in lista_cheltuieli:
        if get_numar_apartament(i) == numar_apartament and get_tip(i) == tip:
            pass
        else:
            result.append(i)
    return result

def handle_delete(lst, numar_apartament, tip):
    nr = int(numar_apartament)
    e = read(lst, nr)
    if e is None:
        print('Nu exista inregistrarea. ')
    else:
        lst = delete(lst, nr, tip)
        print('Inregistrarea a fost stearsa.')
    return lst

def handle_delete1(lst):
    nr = int(input('numar apartament: '))
    tip = input('tipul: ')
    lst = delete(lst, nr, tip)
    print('Inregistrarea a fost stearsa.')
    return lst



