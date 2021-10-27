import datetime

def getNewPayment(_numar_apartament: int, _suma: int, _data: datetime, _tip: str):
    payment = [_numar_apartament, _suma, _data, _tip]
    return payment

def get_numar_apartament(cheltuiala):
    return cheltuiala[0]

def get_suma(cheltuiala):
    return cheltuiala[1]

def get_data(cheltuiala):
    return cheltuiala[2]

def get_tip(cheltuiala):
    return cheltuiala[3]

def get_payment_string(cheltuiala):
    return f'Propietarul apartamentului {get_numar_apartament(cheltuiala)} a efectuat plata in valoare de {get_suma(cheltuiala)} lei, pentru {get_tip(cheltuiala)} in data de {get_data(cheltuiala)}.'