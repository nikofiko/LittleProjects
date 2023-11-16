import os
import time 

def quiz(imie):
    print('Witaj,', imie)
    print('Zostanie ci teraz zadane w sumie 10 pytan, sprobuj na nie poprawnie odpowiedziec :)')

    pytania_odpowiedzi = {
        'Ile wierzcholkow ma szescian?': 'A : 6\nB : 8\nC : 12\n',
        'W ktorym roku Miroslaw Handke, owczesny minister edukacji, wprowadzil do systemu gimnazjum?': 'A : 1999\nB : 1998\nC : 1996\n',
        'Jaki ładunek elektryczny ma neutron?': 'A : Dodatni\nB : Neutralny\nC : Ujemny\n',
        'Swiatlo jest fala czy strumieniem czastek?': 'A : Fala\nB : Cząstka\nC : Jest zarowna fala, jak i strumieniem cząstek\n',
        'Czym jest linux?': 'A : Systemem Operacyjnym\nB : Rodzajem komputera\nC : Aplikacja internetowa\n',
        'Prawda czy fałsz W wiedzminie steruje sie tylko geraltem z rivi?': 'A : Prawda\nB : Falsz\n',
        'Kto jest autorem hymnu rozpoczynajecego sie od slow "Smutno mi, Boże?': 'A : Cyprian Kamil Norwid\nB : Juliusz Slowacki\nC : Zygmunt Krasinski\n',
        'W ktorym roku pojawil sie pierwszy Windows?': 'A : 1980\nB : 1990\nC : 1985\n',
        'Ktory z nich nie byl bratem zeusa?': 'A : Posejdon\nB : Hades\nC : Hefajstos\n',
        'Okolo trzy czwarte masy slonca stanowi?': 'A : Tlen\nB : Hel\nC : Wodór\n'
    }
    poprawne_odpowiedzi = ['B', 'A', 'B', 'C', 'A', 'B', 'B' , 'C', 'C', 'C']
    wynik = 0
    licznik_odpowiedzi = 0
    for x, y in pytania_odpowiedzi.items():
        print(x) 
        odpowiedz = input(y)
        while odpowiedz.capitalize() not in 'ABC':
            odpowiedz = input('Podaj poprawna odpowiedz A, B lub C\n')

        if odpowiedz.capitalize() == poprawne_odpowiedzi[licznik_odpowiedzi]:
            print('Dobra odpowiedz')
            wynik += 1
            licznik_odpowiedzi += 1
        elif odpowiedz.capitalize() != poprawne_odpowiedzi[licznik_odpowiedzi]:
            print('Zla odpowiedz poprawna to: B')
            licznik_odpowiedzi += 1
        
        time.sleep(2.2)
        os.system('cls')

    return f'Twoj wynik to {wynik}/10, czyli {wynik * 10}%'

print(quiz('imie'))