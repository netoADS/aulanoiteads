n1 = float(input("entre com a nota 1: "))
n2 = float(input("entre com a nota 2: "))
n3 = float(input("entre com a nota 3: "))
me = float(input("entre com a nota Me: "))

ma = (n1 + n2*2 +n3*3+me)/7

if ma >= 9:
    print("Parabens sua nota é: ",ma)
else:
    print("PUTS... precisa melhorar: ",ma)
