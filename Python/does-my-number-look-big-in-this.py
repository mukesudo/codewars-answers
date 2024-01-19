def narcissistic( value ):
    # Code away
    
    initialValue = value
    counter = 0
    sum = 0
    remainder = 0
    digits = []
    
    while(value!=0):
        remainder = value%10
        digits.append(remainder)
        value=int(value/10)
        counter+=1
        
    digitsCubed = [digit**counter for digit in digits]
    
    for digit in digitsCubed:
        sum+=digit
        
    if(sum==initialValue):
        return True
    else:
        return False