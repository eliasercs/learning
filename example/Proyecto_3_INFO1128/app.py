import requests as req, time as ti, random as ra

URL = "http://127.0.0.1:8000/datos"

def Generate():
    dData = {
        '01' : ra.randint(+5,+20),
        '25' : ra.randint(+5,+20),
        '10' : ra.randint(+5,+20),
        'te' : ra.randint(-10,+10)
    }
    return dData

while 1:
    dData = Generate()
    MyCnx = req.post(URL,json=dData)
    ti.sleep(5)
    MyCnx.close()