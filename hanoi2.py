## Projet Hanoi Eliot Poupin-Lebreton
class Pile:
    def __init__(self):
        self.l = []
    def est_vide(self):
        return len(self.l) == 0
    def pop(self):
        return self.l.pop(0)
    def push(self, n):
        self.l = [n] + self.l
################################################################################
################################################################################
class Jeu_Hanoi:
    def __init__(self, nbr_disq = 6):
        self.n = nbr_disq
        self.A = Pile()
        self.B = Pile()
        self.C = Pile()
        # Remplissage initial de la première pile
        for d in range(self.n):
            self.A.push(self.n-d)

    def jouer_ia(self):
        def hanoi(n,A,B,C):
            if n==0 :
                return None # ce return renvoit rien, il a comme unique objectif de stopper la fonction. 
            # l'appel recursif 
            else:
                hanoi(n-1,A,C,B)
                #print ("On deplace le disque de la tour num ",a,"sur la tour num ",c)
                disque = A.pop()
                print ("On déplace le disque",disque)
                C.push(disque)
                print(self.A.l)
                print(self.B.l)
                print(self.C.l)
                hanoi(n-1,B,A,C)

        return hanoi(self.n,self.A,self.B,self.C)

J = Jeu_Hanoi(12) # ne pas mettre au dessus de 20, au risque d'un crash du processeur de votre machine
J.jouer_ia()