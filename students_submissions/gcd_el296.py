def gcd(a: int, b: int) -> int:	
    if(b ==0 ):
		return a
	if(a ==0):
		return b
	return gcd(b,a%b)
