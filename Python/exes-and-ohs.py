def xo(s):

    x,y =['x','o']

    s = s.lower()
    
    if x in s and y in s:
        if s.count(x) == s.count(y):
            return True
        else:
            return False
    else:
        return True