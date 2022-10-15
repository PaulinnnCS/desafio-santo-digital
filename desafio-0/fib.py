n = 255

def fib (n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

nFib = str(fib(n))
tam = len(nFib)

if tam > 1:
    result = f"{nFib[tam - 2] if nFib[tam - 2] != '0' else ''}{nFib[tam - 1]}"
else:
    result = f"{nFib[tam - 1]}"

print(nFib)
print(result)   

