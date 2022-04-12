def swap(array:list,i:int,e:int) -> None:
    temp = array[i]
    array[i] = array[e]
    array[e] = temp

def bubbleSort(array:list) -> list:
    """
    Recorre repetidamente a través de una lista. Si el elemento actual es mayor al siguiente,
    se intercambian.
    """
    for i in range(1,len(array)):
        for j in range(0,len(array)-1):
            if array[j]>array[j+1]:
                swap(array,j,j+1)
    return array

def selectionSort(array:list) -> list:
    """
    Consiste en buscar el elemento más pequeño de la lista, e intercambiarlo con el primero.
    Buscar el segundo elemento más pequeño de la lista, e intercambiarlo con el segundo.
    Y así sucesivamente.
    """
    for i in range(0,len(array)):
        min = i
        for j in range(i+1,len(array)):
            if array[j] < array[min]:
                min = j
        swap(array,i,min)
    return array