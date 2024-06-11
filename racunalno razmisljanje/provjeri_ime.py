# Napišite funkciju koja provjerava da li je
# zadano ime osobe muško ili žensko.

# Za provjeru koristimo jednostavnu provjeru koja se
# temelji na zadnjem slovu imena.
# Ako je zadnje slovo imena 'a', kažemo da je ime žensko.
# Ako zadnje slovo imena nije 'a', kažemo da je ime muško.
# Ali imamo i neke iznimke: Matija, Vanja, Saša.
# Za te iznimke kažemo da ne znamo.
# (naravno, postoji još imena koja su u tom skupu, ali za potrebe
# zadatka ih nećemo koristiti)

# Funkcija se mora zvati `provjeri_ime`.
# Funkcija prima ime osobe kao argument koji mora biti tipa string (str).
# Funkcija vraća 'Musko ime', 'Zensko ime' ili 'Ne znam' (str).
# Ako ulazni parametar nije tipa str, funkcija mora vratiti 'Ne znam'.
# Glavna funkcija (main) ispituje ispravnost rada funkcije,
# taj dio programskog koda ne treba mijenjati.


def provjeri_imea(ime):
    # TODO implementirajte funkciju
    pass

def provjeri_ime(ime):
    # Provjeravamo je li ulazni parametar tipa string
    if not isinstance(ime, str) or ime == '':
        return 'Ne znam'
    
    # Iznimke
    iznimke = {'Matija', 'Vanja', 'Saša'}
    
    # Provjeravamo je li ime u iznimkama
    if ime in iznimke:
        return 'Ne znam'
    
    # Provjeravamo zadnje slovo imena
    if ime[-1] == 'a':
        return 'Zensko ime'
    
    return 'Musko ime'

def main():
    assert provjeri_ime('Dino') == 'Musko ime'
    assert provjeri_ime('Marta') == 'Zensko ime'
    assert provjeri_ime('Ana') == 'Zensko ime'
    assert provjeri_ime('Igor') == 'Musko ime'
    assert provjeri_ime('Matija') == 'Ne znam'
    assert provjeri_ime('Vanja') == 'Ne znam'
    assert provjeri_ime('Saša') == 'Ne znam'
    assert provjeri_ime('') == 'Ne znam'
    assert provjeri_ime(10) == 'Ne znam'
    print("Implementacija je tocna!")


if __name__ == '__main__':
    main()
