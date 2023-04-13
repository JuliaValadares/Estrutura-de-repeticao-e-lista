numeros = [1,2,3,4,5]
soma = 0
multi = numeros[0]
print("numeros:", numeros)
for i in numeros:
    soma = soma + numeros [i-1]
    multi = multi * numeros[i-1]
    print("soma:", soma)
    print("multiplicação:" , multi)

