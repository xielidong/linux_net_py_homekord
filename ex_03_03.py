score=input("Enter score:")

if(score.isalpha()):
	print("Bad score")
else:
	s=(float)(score)
	if(s<0.0 or s>1.0):
		print("Bad score")
	else:
		if(s>=0.9):
			print('A')
		elif(s>=0.8):
			print('B')
		elif(s>=0.7):
			print('C')
		elif(s>=0.6):
			print('D')
		else:
			print('F')