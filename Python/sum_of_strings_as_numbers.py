"""
Sum Strings as numbers - 4 Kyu

Given the string representations of two integers, 
return the string representation of the sum of those integers.

For example:
sumStrings('1','2') // => '3'

"""
def sum_strings(x,y):
    """Sum Strings as numbers. x: first number as string, y: second number as string
        return: sum of numbers as string
    """
    if len(x) > len(y):
        x,y=y,x
    sum_str = ""
    n1 = len(x)
    n2 = len(y)
    x = x[::-1]
    y = y[::-1]

    carry = 0
    for i in range(n1):
        sum_of_numbers = int(x[i]) + int(y[i]) + carry
        sum_str += str(sum_of_numbers % 10)
        carry = int(sum_of_numbers / 10)
    for i in range(n1, n2):
        sum_of_numbers = int(y[i]) + carry
        sum_str += str(sum_of_numbers % 10)
        carry = (int)(sum_of_numbers / 10)
    if carry:
        sum_str += str(carry)
    sum_str = sum_str[::-1].lstrip('0') or '0'

    return sum_str