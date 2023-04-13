idade = [30,16,40,50,10]
altura = [1.67,1.61,1.70,1.65,1.50]
alturaVazia = []
idadeVazia = []
print (idade)
print (altura)

for i in range (5):
    idadeVazia.append(idade.pop())
    alturaVazia.append(altura.pop())

    print(idadeVazia)
    print(alturaVazia)