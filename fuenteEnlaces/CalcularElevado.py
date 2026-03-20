a = int(input("Ingrese un numero entero: "))

def Calcular_n_binario():
    global m
    n = int(input("Ingrese un numero entero: "))
    m = []

    while n > 0:
        if n % 2 == 0:
            m.append(0)
        else:
            m.append(1)
        n = n // 2
    m.reverse()

Calcular_n_binario()

p = 1
i = 0
k = len(m)

while i<k-1:
    p = (p * a**m[i])**2
    i += 1
p = p * a**m[(k-1)]
print(p)
input("")