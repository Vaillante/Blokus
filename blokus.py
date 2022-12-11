def placer_piece(plateau,joueur,main):
    piece=afficher_piece(joueur,main)
    rotation_yn=input"tourner la piece?"
        if rotation_yn = False :
            return(0)
        else :
            rotate=input"de combien de quarts de tour dans le sens horaire?"
            rotation(rotate,piece)
    coordx=input("coordonnées x, du centre de la piece")
    coordy=input("coordonnées y, du centre de la piece")
    verif(p,piece,joueur,coord)
    afficher plateau(plateau)
    validation

def afficher_piece(joueur,main):
    print("au tour de",joueur,"/nPièces:",main)
    return(input"Quelle pièce jouer?")

def rotation(rotate,piece):
                # soit la rotation se fait directement lors de la création des pièces soit elle se fait ici où la coordonnées x est comparée avec celle de la pièce centrale, elle est ensuite assignée à la coordonnées y

            #for k in range len(piece):
                #modification de la pièce, carreaux/carreaux#
        return(piece)

def verif(plateau,piece,joueur,coordx,coordy):
    for k in range len(piece()):
        for i in range len(piece[k]):
            if i != "-" :
                verif_carreaux(k,i,plateau,piece)
                if ii

def verif_carreaux(y,x,plateau,piece,coordx,coody,joueur):
# besoin du centre de symmetrie
# peut etre donné dans la definition de la piece ou retrouver à chaque nouvelle piece
    centrex=0
    centrey=0
    yplateau=centrey+coody+y
    xplateau=centrex+coodx+x
    #Savoir si y plateau est sur une case déja prise ou non
    if plateau[yplateau][xplateau]=="-" :
        for u in range (k-1;k+1):
            for j in range (i-1;i):
                if plateau[u][j] ==
    else :
        return False