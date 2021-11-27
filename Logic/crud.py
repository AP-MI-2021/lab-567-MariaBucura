import datetime
from Domain.Cheltuiala import getNewPayment, get_numar_apartament, get_tip


def create(lista_cheltuieli: list, _numar_apartament: int, _suma: int, _data: datetime, _tip: str):
    cheltuiala = getNewPayment(_numar_apartament, _suma, _data, _tip)
    lista_cheltuieli.append(cheltuiala)
    return lista_cheltuieli


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


def update(lista_cheltuieli, new_payment):
    result = []
    for i in lista_cheltuieli:
        if get_numar_apartament(i) == get_numar_apartament(new_payment) and get_tip(i) == get_tip(new_payment):
            result.append(new_payment)
        else:
            result.append(i)
    return result


def delete(lista_cheltuieli, numar_apartament, tip):
    result = []
    for i in lista_cheltuieli:
        if get_numar_apartament(i) == numar_apartament and get_tip(i) == tip:
            pass
        else:
            result.append(i)
    return result
