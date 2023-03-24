def f(x):
    return x**3-2*x**2-3*x+1
#define f'(x)
def f2(x):
    return 3*x**2-4*x-3
# critério de parada: |f(x)| < erro
x = float(input("Entre com aproximação inicial: "))
e = float(input("Entre com valor do erro: "))
print("x","\t"*3,"f(x)","\t"*2,"f'(x)")
while(1):
    print("%.4f"%x,"\t"*2, "%.4f"%f(x),"\t", "%.4f"%f2(x))
    if(abs(f(x)) < e):
        break
    else:
        x = x - f(x) / f2(x)
print("\n Raiz aproximada: ", "%.4f"%x)


