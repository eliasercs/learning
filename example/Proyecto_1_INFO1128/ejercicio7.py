from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
from ejercicio5 import cumulative_histogram, slider
from pathlib import Path
import pygame

if __name__ == "__main__":
    # Abrir las figuras de interés F1 y F4
    f1 = Image.open("./img/figures/F1.png")
    f2 = Image.open("./img/figures/F4.png")

    # Convertir cada figura en modo CMYK
    img = [f1.convert("CMYK"), f2.convert("CMYK")]

    # Para cada figura
    for i in range(2):

        # Obtener cada uno de sus canales
        c1 = img[i].getchannel("C")
        m1 = img[i].getchannel("M")
        y1 = img[i].getchannel("Y")
        k1 = img[i].getchannel("K")

        # Generar un subplots de 3 filas y 4 columnas
        fig, ax = plt.subplots(3,4)
        # Establecemos una resolución de 15 pulgadas de ancho y 7 pulgadas de alto
        fig.set_size_inches(15,7)
        # Mostrar el canal C con un mapa de colores en escala de grises
        ax[0,0].imshow(c1,"gray")
        # Establecer un título para la figura
        ax[0,0].set_title("Canal C")
        # Ocultar los valores numéricos en los ejes horizontal y vertical
        ax[0,0].set_xticks([]), ax[0,0].set_yticks([])
        # Mostrar el canal M
        ax[0,1].imshow(m1,"gray")
        ax[0,1].set_title("Canal M")
        # Ocultar los valores numéricos en los ejes horizontal y vertical
        ax[0,1].set_xticks([]), ax[0,1].set_yticks([])
        # Mostrar el canal Y
        ax[0,2].imshow(y1,"gray")
        ax[0,2].set_title("Canal Y")
        # Ocultar los valores numéricos en los ejes horizontal y vertical
        ax[0,2].set_xticks([]), ax[0,2].set_yticks([])
        # Mostrar el canal K
        ax[0,3].imshow(k1,"gray")
        ax[0,3].set_title("Canal K")
        # Ocultar los valores numéricos en los ejes horizontal y vertical
        ax[0,3].set_xticks([]), ax[0,3].set_yticks([])
        # Graficar el histograma normal del canal C
        ax[1,0].plot(c1.histogram())
        ax[1,0].set_title("Histograma")
        ax[1,0].set_xlabel("i")
        ax[1,0].set_ylabel("h(i)")
        # Graficar el histograma normal del canal M
        ax[1,1].plot(m1.histogram())
        ax[1,1].set_title("Histograma")
        ax[1,1].set_xlabel("i")
        ax[1,1].set_ylabel("h(i)")
        # Graficar el histograma normal del canal Y
        ax[1,2].plot(y1.histogram())
        ax[1,2].set_title("Histograma")
        ax[1,2].set_xlabel("i")
        ax[1,2].set_ylabel("h(i)")
        # Graficar el histograma normal del canal K
        ax[1,3].plot(k1.histogram())
        ax[1,3].set_title("Histograma")
        ax[1,3].set_xlabel("i")
        ax[1,3].set_ylabel("h(i)")
        # Rellenar por debajo de la recta del histograma acumulado
        ax[2,0].fill_between(np.arange(len(cumulative_histogram(c1))),np.array(cumulative_histogram(c1)),alpha=0.7)
        ax[2,0].set_title("Histograma Acumulado")
        ax[2,0].set_xlabel("i")
        ax[2,0].set_ylabel("H(i)")
        # Rellenar por debajo de la recta del histograma acumulado
        ax[2,1].fill_between(np.arange(len(cumulative_histogram(m1))),np.array(cumulative_histogram(m1)),alpha=0.7)
        ax[2,1].set_title("Histograma Acumulado")
        ax[2,1].set_xlabel("i")
        ax[2,1].set_ylabel("H(i)")
        # Rellenar por debajo de la recta del histograma acumulado
        ax[2,2].fill_between(np.arange(len(cumulative_histogram(y1))),np.array(cumulative_histogram(y1)),alpha=0.7)
        ax[2,2].set_title("Histograma Acumulado")
        ax[2,2].set_xlabel("i")
        ax[2,2].set_ylabel("H(i)")
        # Rellenar por debajo de la recta del histograma acumulado
        ax[2,3].fill_between(np.arange(len(cumulative_histogram(k1))),np.array(cumulative_histogram(k1)),alpha=0.7)
        ax[2,3].set_title("Histograma Acumulado")
        ax[2,3].set_xlabel("i")
        ax[2,3].set_ylabel("H(i)")
        fig.tight_layout()

        # Guardar cada figura
        plt.savefig("./result/ejercicio7/fig_{}.png".format(i+1))

    result = Path("./result/ejercicio7")

    file = []

    # Iterar cada figura obtenida con matplotlib y cargar como una superficie de pygame
    for f in result.iterdir():
        file.append(pygame.image.load(f))

    # Se asume que cada figura de matplotlib contiene el mismo ancho y alto
    width = file[0].get_width()
    height = file[0].get_height()

    # Generar un carrusel de imágenes con la función implementada en el ejercicio 5.
    slider("Ejercicio7",size=(width,height+80),btn_next=[200,720,150,50],btn_prev=[30,720,150,50],
        figure=file, color_btn=[(237,128,19),(70,189,34)])