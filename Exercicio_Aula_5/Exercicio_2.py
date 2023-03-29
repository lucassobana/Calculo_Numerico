def f(x):
    return -x**2+2*x+1
#entrar com valores de [a,b] e precisão
#critério de parada: |f(x)| < erro
a = float(input("Entre com valor de a: "))
b = float(input("Entre com valor de b: "))
e = float(input("Entre com valor do erro: "))
cont=0
print("   a  ","\t"*3,"b  ","\t"*2,"x ","\t"*2,"f(x)")
while(1):
    x = (a+b)/2
    fx = f(x)
    print("%.4f"%a,"\t", "%.4f"%b,"\t", "%.4f"%x,"\t", "%.4f"%fx)
    if(abs(fx) < e):
        break
    elif f(a)*fx<0:
        b = x
    else:
        a = x
print("\n Raiz aproximada: %.4f" %x)
