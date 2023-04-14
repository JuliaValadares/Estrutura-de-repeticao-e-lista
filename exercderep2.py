print("faça já seu cadastro:")
usuario=(input("usuário--> "))
senha=(input("senha-->"))
while usuario==senha:
	print("ERRO: o usuário não pode ser igual a senha, tente novamente")
	usuario=(input("usuário--> "))
	senha=(input("senha-->"))
else:
	print("cadastrado efetuado com sucesso")