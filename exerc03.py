exerc03 = [10,9.5,7.0,6.0]
media = 0
for i in range(0,len(exerc03)):
    print("notas",i+1,":",exerc03[i])
    media = media + exerc03[i]
media = media / len(exerc03)
print("media:",media)