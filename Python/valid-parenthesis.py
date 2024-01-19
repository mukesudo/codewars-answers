def valid_parentheses(string):
    #your code here
    stack=[]
    for character in string:
        if character == '(':
            stack.append(character)
        elif character ==')':
            if not stack:
                return False
            stack.pop()

    return not stack