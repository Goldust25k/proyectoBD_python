#Proyecto 1 Echo por:Joaquin Limaco y Nicolas Riquelme
import os

def recupera_nombres(ruta='train'):
    return [nombre for nombre in os.listdir(ruta) if os.path.isdir(os.path.join(ruta, nombre))]

def obtener_imagnes_por_persona(ruta='train'):
    personas = recupera_nombres(ruta)
    todas_las_imagene = []
    for persona in personas:
        capeta_persona = os.path.join(ruta, persona)
        imagenes = os.listdir(capeta_persona)
        todas_las_imagene.append(imagenes)
    return todas_las_imagene


if __name__ == "__main__":
    print(recupera_nombres('train'))
    print(obtener_imagnes_por_persona('train'))
