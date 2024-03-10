"""
Number of Proper Fractions with Denominator d - 4 Kyu

build a function that computes how many proper fractions you can build with a given denominator n
"""
def proper_fractions(n):
    """
    Calculates totiems of n: number of proper denominaters for n

    Better algorithm with Time complexity of O(N)
    Time complexity (Approximate): O(N)
    """
    if n == 1:
        return 0
    count = n
    i = 2
    while i*i <= n:
        if n % i == 0:
            while n % i ==0:
                n //= i
            count -= count // i
        i += 1
    if n > 1:
        count -= count // n
    return count

print(proper_fractions(15))
