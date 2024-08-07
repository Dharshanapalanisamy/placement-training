st=str(input("Enter the string")
lower=0
upper=0
for i in st:
	if(i.islower()):
			lower+=1
	else:
			upper+=1
print("lowercase characters is:",lower)
print("uppercase characters is:",upper)
