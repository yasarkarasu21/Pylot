import numpy as np
import matplotlib.pyplot as plt
import json
konumlarx=[]
konumlary=[]
rnd = np.random
rnd.seed(4)
myjsonfile=open("konum.json","r",encoding='utf-8')
jsondata = myjsonfile.read()
obj= json.loads(jsondata)

n = len(obj) # bir firma bir gün içerisinde yalnızca 43 noktaya sipariş götürebilir.
plt.plot(37.746804865934564, 29.106838840302437, c='r', marker='s') # aracın ilk başlayacağı rota 0 noktası, depo

for i in range(1, len(obj)):
    konumlarx.append(obj[i]['x'])
    konumlary.append(obj[i]['y'])
plt.scatter(konumlarx[0:], konumlary[0:], c='b') # sistemde kayıtlı müşterilerin işaretlendiği nokta
plt.show()