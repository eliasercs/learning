from PIL import Image
import math

"""
El momento espacial o M se define como la sumatoria del polinomio x**p * y**q * I(x,y), dónde
(x, y) son posiciones del pixel de la imagen a recorrer.
(p, q) son valores que hacen referencia a un momento en específico.
I(x, y) como un píxel de una imagen.
"""
def momento_espacial(img:Image,p:int,q:int):
    sumatoria = 0
    for y in range(img.height):
        for x in range(img.width):
            sumatoria += math.pow(x,p) * math.pow(y,q) * img.getpixel((x,y))
    return sumatoria

"""
El centroide devuelve x e y, los cuales son coordenadas de dónde se ubica el centroide, obteniéndose como:
area = M00 (Momento 0 0)
x = M10 / area
y = M01 / area
"""
def centroide(img:Image):
    area = momento_espacial(img,0,0)
    x = momento_espacial(img,1,0) / area
    y = momento_espacial(img,0,1) / area
    return x,y

"""
El momento central está definida como la sumatoria del polinomio (x - xp)**p * (y - yp)**q * I(x,y), dónde:
(x, y) son coordenadas de la imagen a recorrer,
(xp, yp) son coordenadas del centroide,
(p, q) son valores que hacen referencia a un momento en específico.
I(x, y) como un píxel de una imagen.
"""
def momento_central(img:Image,p:int,q:int):
    xp,yp = centroide(img)
    sumatoria = 0
    for y in range(img.height):
        for x in range(img.width):
            sumatoria += math.pow((x-xp),p) * math.pow((y-yp),q) * img.getpixel((x,y))
    return sumatoria
"""
Los momentos normales (MNpq) se define como:
La división entre los momentos centrales de pq y por una potencia adecuada del momento de orden 0.
Donde p+q >= 2
"""
def momento_normal(img:Image,p:int,q:int):
    return momento_central(img,p,q) / math.pow(momento_central(img,0,0),1+((p+q)/2))
    
def momento_hu1(img:Image):
    return momento_normal(img,2,0) + momento_normal(img,0,2)

def momento_hu2(img:Image):
    return (math.pow((momento_normal(img,2,0)-momento_normal(img,0,2)),2) + 4*math.pow(momento_normal(img,1,1),2))

def momento_hu3(img:Image):
    a = math.pow((momento_normal(img,3,0)-3*momento_normal(img,1,2)),2)
    b = math.pow((3*momento_normal(img,2,1)-momento_normal(img,0,3)),2)
    return a + b

def momento_hu4(img:Image):
    a = math.pow((momento_normal(img,3,0)+momento_normal(img,1,2)),2)
    b = math.pow((momento_normal(img,2,1)+momento_normal(img,0,3)),2)
    return a + b

def momento_hu5(img:Image):
    #Momentos normales
    mn_30 = momento_normal(img,3,0)
    mn_12 = momento_normal(img,1,2)
    mn_21 = momento_normal(img,2,1)
    mn_03 = momento_normal(img,0,3)

    #Operaciones comunes
    o1 = (mn_30 + mn_12)
    o2 = (mn_21 + mn_03)

    # Operación Final
    a = (mn_30-3*mn_12)*o1*(math.pow(o1,2)-3*math.pow(o2,2))
    b = (3*mn_21-mn_03)*o2*(3*math.pow(o1,2)-math.pow(o2,2))
    return a + b

def momento_hu6(img:Image):
    #Momentos normales
    mn_30 = momento_normal(img,3,0)
    mn_12 = momento_normal(img,1,2)
    mn_21 = momento_normal(img,2,1)
    mn_03 = momento_normal(img,0,3)
    mn_20 = momento_normal(img,2,0)
    mn_02 = momento_normal(img,0,2)
    mn_11 = momento_normal(img,1,1)

    # Operaciones comunes
    o1 = (mn_30 + mn_12)
    o2 = (mn_21 + mn_03)

    # Operación o expresión final
    a = (mn_20-mn_02)*(math.pow(o1,2)-math.pow(o2,2))
    b = 4*mn_11*o1*o2
    return a + b

def momento_hu7(img:Image):
    # Momentos normales
    mn_30 = momento_normal(img,3,0)
    mn_12 = momento_normal(img,1,2)
    mn_21 = momento_normal(img,2,1)
    mn_03 = momento_normal(img,0,3)

    # Operaciones comunes
    o1 = (mn_30 + mn_12)
    o2 = (mn_21 + mn_03)

    # Operación o expresión final
    a = (3*mn_21-mn_03)*o1*(math.pow(o1,2)-3*math.pow(o2,2))
    b = (mn_30-3*mn_12)*o2*(3*math.pow(o1,2)-math.pow(o2,2))

    return a - b