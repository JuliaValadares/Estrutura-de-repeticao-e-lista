nome=str(input("digite um nome "))
while ( len(nome) <=  3 ):
	nome=str(input("Nome invalido.Digite o nome novamente"))

idade=int(input("digite a idade"))
while ( idade > 150 or idade < 0 ):
	idade=int(input("Idade inválida.digite novamente "))

salario=float(input("digite um salário invalido.Digite novamente "))
while ( salario < 0 ):
	salario=float(input("Salário--> "))
	
sexo=str(input("digite a inicial do seu sexo"))
while   sexo !="F" and sexo !="M" :
	sexo=str(input("digite a inicial do seu sexo"))
	

estado_civil=str(input("digite a inicial do seu estado civil"))
while ( estado_civil != "s" and estado_civil != "c" and estado_civil != "v" and estado_civil != "d"  ):
	estado_civil=str(input("digite a inicial do seu estado civil"))
