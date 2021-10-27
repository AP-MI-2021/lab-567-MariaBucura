import datetime

def getNewPayment(_numar_apartament: int, _suma: int, _data: datetime, _tip: str):
    payment = {
        'numar_apartament': _numar_apartament,
        'suma': _suma,
        'data': _data,
        'tip': _tip
    }
    return payment

def get_numar_apartament(cheltuiala):
    return cheltuiala['numar_apartament']

def get_suma(cheltuiala):
    return cheltuiala['suma']

def get_data(cheltuiala):
    return cheltuiala['data']

def get_tip(cheltuiala):
    return cheltuiala['tip']

def get_payment_string(cheltuiala):
    return f'Propietarul apartamentului {get_numar_apartament(cheltuiala)} a efectuat plata in valoare de {get_suma(cheltuiala)} lei, pentru {get_tip(cheltuiala)} in data de {get_data(cheltuiala)}.'