import pygame
from PIL import Image
import sys

figures = Image.open("./img/figuras.png")
"""
A partir de la imagen anterior, procedo a realizar 4 recortes para obtener las regiones de interés relacionadas a cada
figura encontrada en la imagen, para ello, utilizo el método crop de PIL, el cual recibe una tupla con la cantidad de pixeles
a recortar hacia la izquierda, arriba, derecha y abajo. Junto con el método resize redimensiono la región obtenida
a una imagen de 116 x 116. Y finalmente se convierte a una imagen en canal RGBA, con la finalidad de trabajar con
fondos transparentes a la hora de rotar las imágenes. Y posteriormente se almacenan en el directorio recortes, dentro de img.
Para posteriormente, cargarlos desde pygame y rotarlos desde este mismo.
"""
img1 = figures.crop((3,5,220,220)).resize((116,116))
img1.convert("RGBA").save("./img/recortes/img1.png")
img2 = figures.crop((245,5,484,205)).resize((116,116))
img2.convert("RGBA").save("./img/recortes/img2.png")
img3 = figures.crop((505,23,720,198)).resize((116,116))
img3.convert("RGBA").save("./img/recortes/img3.png")
img4 = figures.crop((733,19,980,202)).resize((120,120))
img4.convert("RGBA").save("./img/recortes/img4.png")

pygame.init()

# Establecer un título a la ventana
pygame.display.set_caption("Ejercicio 2")

"""
Cargar cada uno de los recortes y rotarlos a un ángulo que coincida con lo solicitado
en las posiciones asignadas en plantilla.png
"""

# Cargar el primer recorte y rotarlo a un ángulo de -11 grados
img1 = pygame.image.load("./img/recortes/img1.png")
img1 = pygame.transform.rotate(img1,-11)

# Cargar el segundo recorte y rotarlo a un ángulo de 9 grados
img2 = pygame.image.load("./img/recortes/img2.png")
img2 = pygame.transform.rotate(img2, 9)

# Cargar el tercer recorte y rotarlo a un ángulo de -38.6 grados
img3 = pygame.image.load("./img/recortes/img3.png")
img3 = pygame.transform.rotate(img3,-38.6)

# Cargar el cuarto recorte y rotarlo a un ángulo de 20.5 grados
img4 = pygame.image.load("./img/recortes/img4.png")
img4 = pygame.transform.rotate(img4,20.5)

"""
Cargar la plantilla como una superficie de pygame. Con la finadlidad de dibujar cada recorte sobre ella.
"""
template = pygame.image.load("./img/plantilla.png")
template.blit(img1,(10,19))
template.blit(img2,(201,22))
template.blit(img3,(378,11))
template.blit(img4,(600,11))

"""
Generar una ventana a partir del ancho y alto de la plantilla.
"""
window = pygame.display.set_mode((template.get_width(),template.get_height()))

# Dibujar la plantilla con los recortes sobre la superficie principal de la aplicación.
window.blit(template, (0,0))

while True:
    # Detectar eventos
    for e in pygame.event.get():
        # Validar eventos de cierre
        if e.type == pygame.QUIT:
            sys.exit()

    # Mantener actualizada la aplicación
    pygame.display.update()