def is_isogram(string):
    #your code here
    
    sum=0
    
    counts = [string.lower().count(x) for x in string.lower()]
    
    for ele in counts:
        sum+= ele
    
    returnValue = True if sum==len(counts) else False

    return returnValue