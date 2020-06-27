import random
import sys
sys.tracebacklimit = 0
#BARALLA

baralla=['A',2,3,4,5,6,7,8,9,10,'J','Q','K']*4

def mix():
    random.shuffle(baralla)

def show():
    print(baralla)

#JUGADOR

class Jugador():
    def __init__(self):
        self.cartes=[]

    def deal(self):
        for i in range(2):
            carta=baralla.pop(0)
            self.cartes.append(carta)

    def hit(self):
        carta=baralla.pop()
        self.cartes.append(carta)
        if carta=='J' or carta=='Q' or carta=='K':
            self.valor=self.valor+10
        elif carta=='A' and self.valor>10:
            self.valor=self.valor+1
        elif carta=='A' and self.valor<=10:
            self.valor=self.valor+11
        else:
            self.valor=self.valor+carta
        print('Tens:',self.cartes)
        self.check()

    def valor(self):
        if self.cartes[0]=='A':
            self.valor1=11

        elif self.cartes[0]=='J' or self.cartes[0]=='Q' or self.cartes[0]=='K':
            self.valor1=10
        else:
            self.valor1=self.cartes[0]

        if self.cartes[1]=='A':
            self.valor2=11

        elif self.cartes[1]=='J' or self.cartes[1]=='Q' or self.cartes[1]=='K':
            self.valor2=10
        else:
            self.valor2=self.cartes[1]

        self.valor=self.valor1+self.valor2
        return self.valor

    def decision(self):
            decision=input("(H)it o (s)tay? : ")
            if decision=='H':
                self.hit()
            elif decision=='S':
                print('Tens:',self.cartes)
                return self.valor

            else:
                print('Entra una opció valida')
                self.decision()


    def check(self):
        if self.valor<21:
                self.decision()
        elif self.valor==21:
            print('BLACKJACK! Has guanyat, fi de la partida.')
            sys.exit()
        elif self.valor>21:
            print('BUST! Has perdut, fi de la partida.')
            sys.exit()

#DEALER

class Dealer():
    def __init__(self):
        self.cartes=[]

    def deal(self):
        for i in range(2):
            carta=baralla.pop(0)
            self.cartes.append(carta)

    def hit(self):
        carta=baralla.pop()
        self.cartes.append(carta)
        if carta=='J' or carta=='Q' or carta=='K':
            self.valor=self.valor+10
        elif carta=='A' and self.valor>10:
            self.valor=self.valor+1
        elif carta=='A' and self.valor<=10:
            self.valor=self.valor+11
        else:
            self.valor=self.valor+carta
        self.check()

    def valor(self):
        if self.cartes[0]=='A':
            self.valor1=11

        elif self.cartes[0]=='J' or self.cartes[0]=='Q' or self.cartes[0]=='K':
            self.valor1=10
        else:
            self.valor1=self.cartes[0]

        if self.cartes[1]=='A':
            self.valor2=11

        elif self.cartes[1]=='J' or self.cartes[1]=='Q' or self.cartes[1]=='K':
            self.valor2=10
        else:
            self.valor2=self.cartes[1]

        self.valor=self.valor1+self.valor2
        return self.valor

    def decision(self):
            if self.valor<17:
                self.hit()
            else:
                print('El dealer té',self.cartes)

    def check(self):
            if self.valor<21:
                self.decision()
            elif self.valor==21:
                print('BLACKJACK! Has guanyat, fi de la partida.')
                sys.exit()
            elif self.valor>21:
                print('BUST! Has perdut, fi de la partida.')
                sys.exit()


#JOC

def joc():
    mix()
    dealer=Dealer()
    jugador=Jugador()
    dealer.deal()
    dealer.valor()
    jugador.deal()
    jugador.valor()
    print('El dealer té:',dealer.cartes)
    print('Tens:',jugador.cartes)
    jugador.check()
    dealer.check()
    if jugador.valor < dealer.valor:
        print('El dealer guanya. Sort per la propera!')
    elif jugador.valor > dealer.valor:
        print('Guanyes. Ben jugat!')
    else:
        print('Tenim un empat. Ben jugat!')


joc()
