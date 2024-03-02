"""
Josephus Survivor - 5 kyu
In this kata you have to correctly return who is the "survivor", 
ie: the last element of a Josephus permutation.
Basically you have to assume that n people are put into a circle 
and that they are eliminated in steps of k elements
e.g.
n=7, k=3 => means 7 people in a circle
one every 3 is eliminated until one remains
[1,2,3,4,5,6,7] - initial sequence
[1,2,4,5,6,7] => 3 is counted out
[1,2,4,5,7] => 6 is counted out
[1,4,5,7] => 2 is counted out
[1,4,5] => 7 is counted out
[1,4] => 5 is counted out
[4] => 1 counted out, 4 is the last element - the survivor!
"""
def josephus_survivor(n,k):
    #your code here
    arr=[i for i in range(1,n+1)]
    position = 0
    while len(arr)>1:
        if position+k<len(arr):
            position+=k-1
        else:
            position+=k-1
            position%=len(arr)
        del arr[position]

    return arr.pop()
