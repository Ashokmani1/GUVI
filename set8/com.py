
def isComposite(n): 

	# Corner cases 
	if (n <= 1): 
		return False
	if (n <= 3): 
		return False

	if (n % 2 == 0 or n % 3 == 0): 
		return True
	i = 5
	while(i * i <= n): 
		
		if (n % i == 0 or n % (i + 2) == 0): 
			return True
		i = i + 6
		
	return False


print("yes") if(isComposite(int(input()))) else print("no") 
