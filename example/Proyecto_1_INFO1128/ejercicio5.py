from PIL import Image, ImageOps
import matplotlib.pyplot as plt
import numpy as np
import pygame
import sys
import pathlib

"""
El histograma acumulado es una función creciente con un valor máximo, el cual es el número total de pixeles
en una imagen de ancho (W) y altura (N). Para generar esta función creciente, basta con sumar cada h(j) del histograma
normal con un valor anterior conformado por h(j-1).
"""
def cumulative_histogram(img:Image):
    img = img.copy()
    H = img.histogram()
    for j in range(len(H)):
        H[j] = H[j-1] + H[j]
    return H

# Función para dibujar un botón en pygame
def draw_button(surface:pygame.Surface, button:pygame.Rect, background:tuple, background_hover:tuple, posicion:tuple, txt:str):

    """
    Parámetros
    @surface -> class: pygame.Surface -> Superficie que permite incorporar elementos sobre ella. Ejemplo:
    el display o ventana principal de la aplicación.
    @button -> class: pygame.Rect -> El botón se diseña a partir de los rectángulos de pygame.
    @background -> tuple -> Es el color de fondo para el botón
    @background_hover -> tuple -> Es el color de fondo para el botón cuando se pase el mouse por encima
    @posicion -> tuple -> Posición (x,y) en el superficie o surface.
    @txt -> str -> Texto o valor que contiene el botón.
    """

    # Generar el tipo de letra con su tamaño
    myFont = pygame.font.SysFont("Calibri",30)
    # Validar la posición del mouse dentro del botón
    if button.collidepoint(pygame.mouse.get_pos()):
        # Dibujar un botón redondeando de color definido por el background
        pygame.draw.rect(surface, background, button, border_radius=50)
    else:
        # Dibujar un botón redondeando de color definido por el background_hover
        pygame.draw.rect(surface, background_hover, button, border_radius=50)
    
    # Establecer el texto en color verde
    texto = myFont.render(txt,True, (255,255,255))
    # Establecer el texto dentro de la superficie centrado tanto horizontal como verticalmente con respecto al botón
    surface.blit(texto,(posicion[0]+(button.width-texto.get_width())/2,posicion[1]+(button.height-texto.get_height())/2))

# Función para generar un carrusel de imágenes con pygame
def slider(title:str, size:tuple, btn_next:list,btn_prev:list, figure:list, color_btn:list):
    """
    @title => título de la ventana
    @size => tamaño de la ventana (width, height)
    @btn_next => Recibe las características del botón siguiente en una lista
    [x, y, width, height]
    @btn_prev => Recibe las características del botón anterior en una lista
    [x, y, width, height]
    @figure => listado de imágenes
    @color_btn => lista con los respectivos colores para los botones
    """
    pygame.init()
    pygame.display.set_caption(title)

    # Crear dos rectángulos para simular la creación de los botones
    next = pygame.Rect(btn_next[0],btn_next[1],btn_next[2],btn_next[3])
    prev = pygame.Rect(btn_prev[0],btn_prev[1],btn_prev[2],btn_prev[3])

    """
    pos_figura define la posición de la imagen que está recorriendo e incorporando al display principal
    llamado ventana.
    """
    pos_figure = 0

    # Genera la superficie o ventana principal
    ventana = pygame.display.set_mode(size)
    # Rellena el display principal con un background de color blanco
    ventana.fill(0xffffff)

    # Establecer como superficie la primera imágen de la lista
    ventana.blit(figure[pos_figure],(0,0))

    while True:
        # Para cada evento detectado
        for event in pygame.event.get():
            # Cerrar la aplicación
            if event.type == pygame.QUIT:
                sys.exit()
            # Detectar cuando se hace click izquierdo sobre el botón next
            if event.type == pygame.MOUSEBUTTONDOWN and event.button==1 and next.collidepoint(pygame.mouse.get_pos()):
                """
                Cuando se hace click sobre el botón next, a la posición de la figura se le suma 1, para 
                avanzar a la siguiente imagen
                """
                pos_figure += 1
                """
                Si la posición de la figura es igual al número de elementos, entonces se asigna un 0
                con la finalidad de regresar a la primera imagen, ya que no existen más imágenes, y con la
                finalidad de evitar generar un error.
                """
                if pos_figure > len(figure)-1:
                    pos_figure = 0
                # Cambiar de imagen en la superficie principal
                ventana.blit(figure[pos_figure],(0,0))
            # Detectar cuando se hace click izquierdo sobre el botón prev
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button==1 and prev.collidepoint(pygame.mouse.get_pos()):
                """
                Cuando se hace click sobre el botón prev, a la posición de la figura se le resta 1, para 
                retroceder a la imagen anterior.
                """
                pos_figure -= 1
                """
                Si la posición de la figura es menor a 0, entonces se asigna la posición de la última imagen
                con la finalidad de regresar a esta última.
                """
                if pos_figure < 0: # Regresar a la imagen final
                    pos_figure = len(figure)-1
                # Cambiar de imagen en la superficie principal
                ventana.blit(figure[pos_figure],(0,0))

        # Dibujar los botones
        draw_button(ventana,next,color_btn[0],color_btn[1],(btn_next[0],btn_next[1]),"Siguiente")
        draw_button(ventana,prev,color_btn[0],color_btn[1],(btn_prev[0],btn_prev[1]),"Anterior")

        # Mantener actualizada la interfaz gráfica
        pygame.display.update()


if __name__ == "__main__":
    img = [] # Imágenes en escala de grises
    h = [] # Histogramas
    c = [] # Histogramas acumulados

    path = pathlib.Path("./img/figures")

    for i in path.iterdir():
        img.append(ImageOps.grayscale(Image.open(i)))

    for i in img:
        h.append(i.histogram())
        c.append(cumulative_histogram(i))

    # Generar una figura de matplotlib para cada una de las imágenes en escala de grises.
    for i in range(len(img)):
        # Generar una figura de 8 pulgadas de ancho x 6 pulgadas de alto
        fig = plt.figure(0,figsize=(8,6))
        # Establecer un subtitulo a la figura para hacer referencia a la imagen que se está trabajando
        fig.suptitle("Figura {}".format(i+1))
        # Generar un subplot para la imagen en escala de grises
        ax_1 = fig.add_subplot(121)
        # Insertar la imagen en escala de grises
        ax_1.imshow(img[i],"gray")
        # Establecer título
        ax_1.set_title("Imagen")
        # Dejar los ejes vertical y horizontal sin valores numéricos
        plt.xticks([]), plt.yticks([])
        # Generar otro subplot para graficar el histograma normal
        ax_2 = fig.add_subplot(222)
        ax_2.set_title("Histograma")
        ax_2.set_ylabel("h(i)")
        ax_2.set_xlabel("i")
        # Graficar el histograma normal
        ax_2.plot(h[i])
        # Generar un subplot para el histograma acumulado
        ax_3 = fig.add_subplot(224)
        ax_3.set_title("Histograma Acumulado")
        ax_3.set_ylabel("H(i)")
        ax_3.set_xlabel("i")
        # Generar el relleno a partir de la función de histograma acumulado
        ax_3.fill_between(np.arange(len(c[i])),np.array(c[i]),alpha=0.7)
        fig.tight_layout()
        # Guardar la figura de matplotlib para mostrarla
        # en una interfaz generada con pygame
        fig.savefig("./result/ejercicio5/F{}.png".format(i+1))
        # Cerrar la figura
        plt.close(0)

    figure = []

    result = pathlib.Path("./result/ejercicio5")

    # Recorrer cada figura generada con matplotlib y cargarla a PyGame como una superficie.
    for e in result.iterdir():
        file = pygame.image.load(e)
        figure.append(file)

    # Se asume que cada figura de matplotlib contiene el mismo ancho y alto
    width = figure[0].get_width()
    height = figure[0].get_height()

    # Generar un carrusel de imágenes, junto con los eventos en su interfaz.
    slider("Ejercicio5",size=(width,height),btn_next=[200,550,150,50],btn_prev=[30,550,150,50],
        figure=figure,color_btn=[(237,128,19),(70,189,34)])