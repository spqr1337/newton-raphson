import math

a = int(input("Entre com o grau da função: "))
b = a+1
d = a-1
cons = []
tombo = []
txt = "Entre com a {}a constante: "
txt2 = "Foram necessárias {} iterações."
x = y = fx = fxd = 1
cont = 0

if a==1:
    for i in range(b):
        w = float(input(txt.format(i+1)))
        cons.append(w)
    x = cons[-1]*-1
    y = x/cons[0]
    print("A função possui raiz real em: ", y)
elif a==2:
    for i in range(b):
        w = float(input(txt.format(i+1)))
        cons.append(w)
    delta = (cons[1]**2)-(4*cons[0]*cons[2])
    if delta<0:
        print("A função não possui raiz real.")
    else:
        fx = 2*cons[0]
        x1 = (((-1*cons[1])+math.sqrt(delta))/fx)
        x2 = (((-1*cons[1])-math.sqrt(delta))/fx)
        print("A função possui raiz X1: ", x1)
        print("A função possui raiz X2: ", x2)
else:
    c = float(input("Entre com a tolerância de erro: "))
    for i in range(b):
        w = float(input(txt.format(i+1)))
        cons.append(w)

    for j in range(b):
        s = cons[j]*(a - j)
        tombo.append(s)

    while(fx>c):
        fx = fxd = 0
        for k in range(a):
            fx = fx+(cons[k]*(x**(a-k)))
        fx = fx + cons[-1]

        for l in range(d):
            fxd = fxd+(tombo[l]*(x**(d-l)))
        fxd = fxd + tombo[-1]

        x = x-(fx/fxd)
        fx = abs(fx)
        cont = cont+1
    print("A função possui uma raiz real em: ", x)
    print(txt2.format(cont))
