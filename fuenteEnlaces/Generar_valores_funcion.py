import matplotlib.pyplot as plt

listay = []
listax = []
for i in range(-100,100):
    x = i
    listax.append(x)
    f = round(3*x**4+x**3-(x/2)**2+3*x - 1)
    listay.append(f)
plt.plot(listax,listay)
plt.show()