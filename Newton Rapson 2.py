a = int(input("Entre com o grau da função: "))
b = a+1
d = a-1
cons = []
tombo = []
txt = "Entre com a {} constante: "
c = float(input("Entre com a tolerância de erro: "))
x = y = fx = fxd = 1

for i in range(b):
    w = float(input(txt.format(i)))
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

print("A função possui uma raiz real em: ", x)