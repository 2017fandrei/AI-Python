'''
- vom crea un magazin virtual -

- vom crea o lista cu produse si o alta lista cu preturile produselor
- aplicatia va avea un meniu pentru ca user-ul sa poata interactiona cu aceasta

"
Meniu
1. Adauga produsul in cos
2. Vezi cosul de cumparaturi
3. Finalizeaza comanda
4. Iesire
"

- la finalizarea comenzii, se va afisa suma de plata. Daca cosul este gol, comanda nu poate fi finalizata
'''

# produsele disponibile in magazin
produse = ["Laptop", "Telefon", "Casti", "Mouse", "Tastatura"]
preturi = [3500, 2000, 150, 100, 200]

cos_cumparaturi = []

while True:             # bucla principala care va rula pana cand utilizatorul va alege sa iasa
    print("Bun venit in magazin")
    print("Produse disponibile:")
    
    for i in range(len(produse)):        # parcurgem fiecare produs din lista de produse: 0, 1, 2, 3, 4
        # 1. id produs.  produsul - pretul
        print(f'{i + 1}. {produse[i]} - {preturi[i]} RON') # afisam produsul si pretul sau

    print("Meniu utilizator")
    print('1. Adauga produsul in cos')
    print('2. Vezi cosul de cumparaturi')
    print('3. Finalizeaza comanda')
    print('4. Iesire')

    # cere utilizatorului sa aleaga o optiune din meniul aplicatiei
    optiune = input("Alege o optiune: ")
    
    if optiune == "1":
        # scadem din input - 1 pentru la noi in lista primul produs este pe 0. Utilizatorul va alege produsul
        # 1. Daca nu scadem 1, va lua produsul telefon in loc de laptop
        produs_index = int(input("Alege produsul dorit: ")) - 1 
        if 0 <= produs_index < len(produse):
            cos_cumparaturi.append((produse[produs_index], preturi[produs_index]))
            print(f'Numele produsul care a fost adaugat in cos: {produse[produs_index]}.')
        else:
            print("Produsul nu este disponibil.")
    
    # utilizatorul alege sa vada cosul de cumparaturi # 2 - 
    # verifica daca exista produse in cos -
    # afiseaza produsele
    # parcurge fiecare produs din cos
    # afiseaza fiecare produs si pretul
    # afiseaza totalul sumei din cos
    elif optiune == "2":
        if len(cos_cumparaturi) > 0:
            print('*' * 30)
            print("\nProduse in cosul tau:")
            print('*' * 30)
            total = 0 # initilizare total suma
            for produs, pret in cos_cumparaturi:
                print('-' * 30)
                print(f'Produsul este {produs} si are pretul {pret} RON')
                print('-' * 30)
                total += pret
            print(f'Cosul de cumparaturi are valoarea totala {total} RON')
        else:
            print("Nu exista produse in cos")
            
    # utilizatorul doreste sa finalizeze comanda
    # verifica daca sunt produse in cos
    # afisare produse
    # calcul total cos
    # mesaj de confirmare pentru comanda plasata
    # iesire din program
    # daca n are produse, afiseaza mesajul de genul comanda nu poate fi finalizata ca nu s produse in ea
    elif optiune == "3":
        if len(cos_cumparaturi) > 0:
            print("\nFinalizare comanda ...")
            total = 0
            for produs, pret in cos_cumparaturi:
                total += pret
            print(f'Comanda ta a fost plasata! Total de plata {total} RON.')
            break
        else:
            print("Cosul tau este gol, iar comanda nu poate fi finalizata.")
            
    # utilizatorul va alege sa iasa din aplicatie # 4
    # afisam mesaj de "La reverede!"
    # aplicatia se opreste
    
    elif optiune == "4":
        print("La revedere!")
        break
    
    # altfel
    # afisam optiunea introduse nu este valida
    else:
        print('!' * 30)
        print("Optiunea nu se regaseste in meniu.")
        print('!' * 30)
   