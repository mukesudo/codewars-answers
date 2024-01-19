def validate_pin(pin):
    #return true or false
    
    return pin.isdigit() and (len(pin)==6 or len(pin)==4)