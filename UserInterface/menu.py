import datetime
from Domain.Cheltuiala2 import getNewPayment, get_data, get_numar_apartament, get_payment_string
from Logic.crud import create, read, update, delete




def menu():
    lst = []
    while True:
        print('alege optiunea: 1.1')
        print('x - Iesire din program.')
        print('a - vizualizare inregistrari.')
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
                    x = input('Doriti sa efectuati o alta actiune? da/nu')
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
                        dat = datetime.datetime(int(input('Anul: ')), int(input('Luna: ')), int(input('Ziua: ')))
                        new = getNewPayment(apt, plata, dat, tip)
                        lst = update(lst, new)
                        print('Inregistrarea a fost modificata.')
                    x = input('Doriti sa efectuati o alta actiune? da/nu')
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
                    x = input('Doriti sa efectuati o alta actiune? da/nu')
                    if x == 'nu':
                        break
                else:
                    print('Optiune Invalida!')
        elif optiune == 'x':
            break
        elif optiune == 'a':
            print(lst)
        else:
            print('Optiune Invalida!')