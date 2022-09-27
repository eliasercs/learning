import cv2
from ejercicio4 import vocales
import numpy as np

if __name__ == "__main__":
    for a in range(len(vocales["a"])):
        print("Vocal a{}".format(a))
        img = np.array(vocales["a"][a])
        M = cv2.moments(img)
        print(cv2.HuMoments(M))

    for e in range(len(vocales["e"])):
        print("Vocal e{}".format(e))
        img = np.array(vocales["e"][e])
        M = cv2.moments(img)
        print(cv2.HuMoments(M))

    for i in range(len(vocales["i"])):
        print("Vocal i{}".format(i))
        img = np.array(vocales["i"][i])
        M = cv2.moments(img)
        print(cv2.HuMoments(M))

    for o in range(len(vocales["o"])):
        print("Vocal o{}".format(o))
        img = np.array(vocales["o"][o])
        M = cv2.moments(img)
        print(cv2.HuMoments(M))

    for u in range(len(vocales["u"])):
        print("Vocal u{}".format(u))
        img = np.array(vocales["u"][u])
        M = cv2.moments(img)
        print(cv2.HuMoments(M))