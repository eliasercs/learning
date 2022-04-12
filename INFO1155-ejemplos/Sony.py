"""
Un receptor IR Sony recibe una trama. Obtener el dispositivo y botón presionado.
"""
class IR_Sony:
    def __binary_to_decimal(self, trama:list) -> int:
        decimal = 0
        for i in range(0,len(trama)):
            if trama[i] == 1:
                decimal += 2**i
        return decimal

    def __init__(self, trama:list) -> None:
        for pulso in range(0,12):
            pulsoActual = trama[pulso]
            if pulsoActual >= 90:
                trama[pulso] = 1
            else:
                trama[pulso] = 0
        self.__button = self.__binary_to_decimal(trama) & 127
        self.__device = (self.__binary_to_decimal(trama) >> 7) & 31

    def get_button(self) -> int:
        return self.__button

    def get_device(self) -> int:
        return self.__device

if __name__ == "__main__":
    trama = [67,70,120,69,110,69,75,79,120,70,110,105]
    Sony = IR_Sony(trama)
    print("Botón: "+str(Sony.get_button()))
    print("Dispositivo: "+str(Sony.get_device()))