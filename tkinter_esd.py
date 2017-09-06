
# -*- coding:Utf8 -*-
from tkinter import * 

# Construction de la fenêtre principale «root»
fen = Tk()
fen.title('ARP Poisonning From Scapy')
weight=15
height=20

'''# Dimensions de la fenetre 
weight=15
height=20'''

# Construction d'un simple bouton
qb = Button(fen, text='Quitter', command=fen.quit)

# Placement du bouton dans «root»
qb.pack()

# Lancement de la «boucle principale»
fen.mainloop()