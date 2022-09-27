from PIL import Image
import momentos
import pandas as pd

figuras = Image.open("./img/vocales.jpg")
figuras = figuras.convert("L")

vocales = { "a": [], "e": [], "i": [], "o": [], "u": [] }

"""
Obtener una región para cada una de las vocales.
El método crop de PIL me permite recortar una región y recibe como argumento una tupla de
4 elementos, dónde:
* El primer elemento corresponde a la cantidad de píxeles a desplazar desde la izquierda.
* El segundo elemento corresponde a la cantidad de píxeles a desplazar hacia arriba.
* El tercer elemento corresponde a la cantidad de píxeles a desplazar hacia la derecha.
* El cuarto elemento corresponde a la cantidad de píxeles a desplazar hacia abajo.

Adicionalmente, se utiliza el método resize para redimensionar las regiones extraídas a una
imagen de 120 de alto x 120 de ancho. Se almacena en la clave correspondiente.
"""
vocales["a"].append(figuras.crop((0,0,90,90)).resize((120,120)))
vocales["a"].append(figuras.crop((0,90,90,180)).resize((120,120)))
vocales["a"].append(figuras.crop((0,180,90,250)).resize((120,120)))
vocales["a"].append(figuras.crop((0,250,90,340)).resize((120,120)))
vocales["a"].append(figuras.crop((0,330,90,420)).resize((120,120)))
vocales["a"].append(figuras.crop((0,410,90,510)).resize((120,120)))
vocales["e"].append(figuras.crop((90,0,160,90)).resize((120,120)))
vocales["e"].append(figuras.crop((90,90,160,180)).resize((120,120)))
vocales["e"].append(figuras.crop((90,180,160,250)).resize((120,120)))
vocales["e"].append(figuras.crop((90,250,160,340)).resize((120,120)))
vocales["e"].append(figuras.crop((90,330,160,420)).resize((120,120)))
vocales["e"].append(figuras.crop((90,410,160,510)).resize((120,120)))
vocales["i"].append(figuras.crop((160,0,230,90)).resize((120,120)))
vocales["i"].append(figuras.crop((160,90,230,160)).resize((120,120)))
vocales["i"].append(figuras.crop((160,160,230,250)).resize((120,120)))
vocales["i"].append(figuras.crop((160,240,230,320)).resize((120,120)))
vocales["i"].append(figuras.crop((160,320,230,410)).resize((120,120)))
vocales["i"].append(figuras.crop((160,410,250,490)).resize((120,120)))
vocales["o"].append(figuras.crop((220,0,295,100)).resize((120,120)))
vocales["o"].append(figuras.crop((225,90,295,180)).resize((120,120)))
vocales["o"].append(figuras.crop((225,180,295,250)).resize((120,120)))
vocales["o"].append(figuras.crop((230,250,295,330)).resize((120,120)))
vocales["o"].append(figuras.crop((220,330,295,420)).resize((120,120)))
vocales["o"].append(figuras.crop((240,420,320,500)).resize((120,120)))
vocales["u"].append(figuras.crop((290,0,380,100)).resize((120,120)))
vocales["u"].append(figuras.crop((290,90,380,180)).resize((120,120)))
vocales["u"].append(figuras.crop((295,180,380,250)).resize((120,120)))
vocales["u"].append(figuras.crop((295,250,380,330)).resize((120,120)))
vocales["u"].append(figuras.crop((295,330,380,420)).resize((120,120)))
vocales["u"].append(figuras.crop((310,420,400,500)).resize((120,120)))

if __name__ == "__main__":

    """
    Generar una lista para cada vocal, el cual almacena otros arreglos con los momentos de HU de cada
    vocal rotada.
    """
    m_a = []
    m_e = []
    m_i = []
    m_o = []
    m_u = []

    """
    Calcular los momentos de HU para cada vocal de a, generando una lista para cada vocal.
    Para ello, se llaman a las funciones de momentos de HU implementadas en el módulo momentos.
    """
    for a in vocales["a"]:
        data = []
        data.append(momentos.momento_hu1(a))
        data.append(momentos.momento_hu2(a))
        data.append(momentos.momento_hu3(a))
        data.append(momentos.momento_hu4(a))
        data.append(momentos.momento_hu5(a))
        data.append(momentos.momento_hu6(a))
        data.append(momentos.momento_hu7(a))
        m_a.append(data)

    """
    Calcular los momentos de HU para cada vocal de e, generando una lista para cada vocal.
    Para ello, se llaman a las funciones de momentos de HU implementadas en el módulo momentos.
    """
    for e in vocales["e"]:
        data = []
        data.append(momentos.momento_hu1(e))
        data.append(momentos.momento_hu2(e))
        data.append(momentos.momento_hu3(e))
        data.append(momentos.momento_hu4(e))
        data.append(momentos.momento_hu5(e))
        data.append(momentos.momento_hu6(e))
        data.append(momentos.momento_hu7(e))
        m_e.append(data)

    """
    Calcular los momentos de HU para cada vocal de i, generando una lista para cada vocal.
    Para ello, se llaman a las funciones de momentos de HU implementadas en el módulo momentos.
    """
    for i in vocales["i"]:
        data = []
        data.append(momentos.momento_hu1(i))
        data.append(momentos.momento_hu2(i))
        data.append(momentos.momento_hu3(i))
        data.append(momentos.momento_hu4(i))
        data.append(momentos.momento_hu5(i))
        data.append(momentos.momento_hu6(i))
        data.append(momentos.momento_hu7(i))
        m_i.append(data)

    """
    Calcular los momentos de HU para cada vocal de o, generando una lista para cada vocal.
    Para ello, se llaman a las funciones de momentos de HU implementadas en el módulo momentos.
    """
    for o in vocales["o"]:
        data = []
        data.append(momentos.momento_hu1(o))
        data.append(momentos.momento_hu2(o))
        data.append(momentos.momento_hu3(o))
        data.append(momentos.momento_hu4(o))
        data.append(momentos.momento_hu5(o))
        data.append(momentos.momento_hu6(o))
        data.append(momentos.momento_hu7(o))
        m_o.append(data)

    """
    Calcular los momentos de HU para cada vocal de u, generando una lista para cada vocal.
    Para ello, se llaman a las funciones de momentos de HU implementadas en el módulo momentos.
    """
    for u in vocales["u"]:
        data = []
        data.append(momentos.momento_hu1(u))
        data.append(momentos.momento_hu2(u))
        data.append(momentos.momento_hu3(u))
        data.append(momentos.momento_hu4(u))
        data.append(momentos.momento_hu5(u))
        data.append(momentos.momento_hu6(u))
        data.append(momentos.momento_hu7(u))
        m_u.append(data)

    """
    Generar las filas necesarias para crear el dataframe.
    DataFrame = Estructura de filas y columnas para almacenar grandes volúmenes de información.
    """
    data = [m_a[0], m_a[1], m_a[2], m_a[3], m_a[4], m_a[5], 
        m_e[0], m_e[1], m_e[2], m_e[3], m_e[4], m_e[5],
        m_i[0], m_i[1], m_i[2], m_i[3], m_i[4], m_i[5],
        m_o[0], m_o[1], m_o[2], m_o[3], m_o[4], m_o[5],
        m_u[0], m_u[1], m_u[2], m_u[3], m_u[4], m_u[5]]

    # Ajustar los índices de las filas para indicar a qué imagen corresponde
    index = ["a0","a1","a2","a3","a4","a5",
        "e0","e1","e2","e3","e4","e5",
        "i0","i1","i2","i3","i4","i5",
        "o0","o1","o2","o3","o4","o5",
        "u0","u1","u2","u3","u4","u5"]

    # Crear un dataframe (estructura de filas y columnas) para almacenar la información obtenida
    moments = pd.DataFrame(data, columns=["HU1","HU2","HU3","HU4","HU5","HU6","HU7"])
    # Ajustar los índices
    moments.index = index
    print(moments)
    # Almacenar el dataframe en un archivo separado por comas.
    moments.to_csv("./result/ejercicio4/moments.csv",sep=",")