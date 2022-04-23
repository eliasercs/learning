def CODE(cKey:chr,nKey:int) -> int:
    nXOR = ord(cKey) ^ nKey
    nLSB = nXOR & 0x0F
    nMSB = nXOR >>0x04
    return (nLSB << 0x04) | nMSB

def DECODE(cKey:int,nKey:int) -> chr:
    nLSB = cKey & 0x0F
    nMSB = cKey >> 0x04
    aux = (nLSB << 0x04) | nMSB
    return chr(aux^nKey)

if __name__ == "__main__":
    aMsg = [116,103,215,71,199,51,7,39,51,119,103,51,54,103,54,167,215,199]
    aKey = [7,13,19,21]

    message = ""
    for key in aKey:
        for cKey in aMsg:
            message += DECODE(cKey,key)
        print("Probando con la clave {} => {}".format(key,message))
        message = ""