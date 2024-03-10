"""
Number of Proper Fractions with Denominator d - 4 Kyu

build a function that computes how many proper fractions you can build with a given denominator n
"""
def proper_fractions(n):
    """
    Calculates totiems of n: number of proper denominaters for n

    Algorithm insufficient for very large numbers
    Time complexity (Approximate): O(nlog(n))
    """
    count = 0
    for b in range(1, n+1):
        a = n
        while b:
            a, b = b, a%b
            if a==1:
                count+=1
    return count

print(proper_fractions(15))
