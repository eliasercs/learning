from PIL import Image, ImageOps
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

# Definir la ruta dónde están las imágenes
path = Path("./img")
# Recorrer cada archivo
for e in path.iterdir():
    # Extraer el nombre de la imagen sin su extensión
    name = e.name.split(".")[0]
    print("[PROCESANDO IMAGEN] => {}".format(name))
    # Abrir la imagen actual
    img = Image.open(e)
    # Crear una copia de la imagen
    img_clone = img.copy()
    gray_scale = ImageOps.grayscale(img_clone)
    
    # Extraer cada canal de imagen
    r, g, b = img.split()
    
    # Obtener el contenido de la imagen
    color = img.getdata()
    # Extrar los colores RGB de la imagen
    red = [(red[0],0,0) for red in color]
    green = [(0,green[1],0) for green in color]
    blue = [(0,0,blue[2]) for blue in color]

    # Establecer cada color extraído sobre la imagen y almacenar cada canal en archivos separados
    img_clone.putdata(red)
    img_clone.save("./result/canales/red_{}.jpg".format(name))
    img_clone.putdata(green)
    img_clone.save("./result/canales/green_{}.jpg".format(name))
    img_clone.putdata(blue)
    img_clone.save("./result/canales/blue_{}.jpg".format(name))

    # Generar los 4 gráficos para cada histograma
    plt.figure(0)
    plt.title("Canal Rojo: {}".format(name))
    plt.xlabel("Intensidad")
    plt.ylabel("Píxeles")
    plt.bar(np.arange(len(r.histogram())),r.histogram(),color="red")
    plt.savefig("./result/histogramas/histograma_red_{}.png".format(name))

    plt.figure(1)
    plt.title("Canal Verde: {}".format(name))
    plt.xlabel("Intensidad")
    plt.ylabel("Píxeles")
    plt.bar(np.arange(len(g.histogram())),g.histogram(),color="green")
    plt.savefig("./result/histogramas/histograma_green_{}.png".format(name))

    plt.figure(2)
    plt.title("Canal Azul: {}".format(name))
    plt.xlabel("Intensidad")
    plt.ylabel("Píxeles")
    plt.bar(np.arange(len(b.histogram())),b.histogram(),color="blue")
    plt.savefig("./result/histogramas/histograma_blue_{}.png".format(name))

    plt.figure(3)
    plt.title("Luminosidad: {}".format(name))
    plt.xlabel("Intensidad")
    plt.ylabel("Píxeles")
    plt.bar(np.arange(len(gray_scale.histogram())),gray_scale.histogram(), color="gray")
    plt.savefig("./result/histogramas/luminosidad_{}.png".format(name))