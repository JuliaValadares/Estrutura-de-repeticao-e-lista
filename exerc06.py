aluno1 =[7,4,6,2]
aluno2 =[4,9,5,6]
aluno3 =[9,9,3,4]
aluno4 =[8,2,5,7]
aluno5 =[9,9,8,7]
aluno6 =[4,3,6,2]
aluno7 =[7,7,6,5]
aluno8 =[6,7,9,9]
aluno9 =[7,9,8,8]
aluno10 =[6,4,7,8]
alunos = [aluno1,aluno2,aluno3,aluno4,aluno5,aluno6,aluno7,aluno8,aluno9,aluno10]

contagem = 0
final = ""
media = 0

for i in alunos:
    for nota in alunos[contagem]:
        media = media + nota
        media = media / len(alunos[contagem])
        if media >= 7:
            final =f"{final} Aluno {contagem +1} (Aprovado) - {media} |" 
            contagem +=1
            media = 0
            print("media",final)