from PIL import Image


# Programme Principal

imageFond = Image.open("vacances-montagne-ete-lac.jpg") #Ouverture de l'image initiale.

imageFond.show() #Affichage de cette image.

dimx = imageFond.size[0]  #Récupération de ses dimensions.
dimy = imageFond.size[1]

imageIncrust = Image.open("Sans_titre.png") #Ouverture de l'image à incruster.

imageIncrust.show() #Affichage de cette image.

dimxI = imageIncrust.size[0]  #Récupération de ses dimensions.
dimyI = imageIncrust.size[1]


def vert(r,v,b): # fonction qui détecte les pixels "verts"
    return r<200 and v>200 and b<200

for i in range(0,dimxI,1):
    for j in range(0,dimyI,1):
        r,v,b=imageIncrust.getpixel((i,j))
        if not vert(r,v,b):
            imageFond.putpixel((i,j),(r,v,b))

imageFond.save("fake.bmp", "bmp") # On enregistre l'image finale

imageFond.show()

imageFond.close() #fermeture de toutes les images

imageIncrust.close()

