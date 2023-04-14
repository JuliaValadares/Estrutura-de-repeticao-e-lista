País_A= int(input("População A = "))
taxaA = float (input ("Taxa de crescimento da população A = "))
result1 = taxaA * 0.01
País_B = int(input("População B = "))
taxaB = float (input ("Taxa de crescimento da população B = "))
result2 = taxaB * 0.01
ano = 0

while País_A <= País_B:
	País_A+= País_A * result1
	País_B += País_B * result2
	ano += 1

print ( "A ultrapassa ou iguala a B em %d anos" %ano )