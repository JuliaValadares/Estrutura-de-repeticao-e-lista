
País_A = 80000
País_B = 200000
ano = 0

while País_A <= País_B:
	País_A += País_A * 0.03
	País_B+= País_B * 0.015
	ano += 1

print ( "País A ultrapassa ou iguala a País B em %d anos" % ano )