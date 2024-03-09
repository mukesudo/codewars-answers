
"""
Snail Sort - 4 Kyu
Given an n x n array, return the array elements arranged from outermost elements
 to the middle element, traveling clockwise.
"""
def snail(snail_map):

    k, l = len(snail_map[0])-1, len(snail_map)-1
    i, j = 0, 0
    cycle = 0
    items_in_snail_size = 0
    snail = []

    for item in snail_map:
        items_in_snail_size += len(item)
    print(f"Items size in snail_map: {items_in_snail_size}")

    while len(snail) < items_in_snail_size:
        print("To left ---->")
        while j <= k:
            print(f"Item added: snail_map[{i}][{j}] = {snail_map[i][j]}")
            snail.append(snail_map[i][j])
            j += 1

        print(f"Snail: {snail}")

        j -= 1
        k -= 1
        i += 1

        print("Downwards")
        print("|")
        print("|")
        print("|")
        print("*")

        while i <= l:
            print(f"Item added: snail_map[{i}][{j}] = {snail_map[i][j]}")
            snail.append(snail_map[i][j])
            i += 1

        print(f"Snail: {snail}")
        i -= 1
        l -= 1
        j -= 1
        

        print(" <---- To Right")
        while j >= cycle:
            print(f"Item added: snail_map[{i}][{j}] = {snail_map[i][j]}")
            snail.append(snail_map[i][j])
            j -=1
        j += 1

        i -= 1

        print(f"Snail: {snail}")

        print("Upwards")
        print("*")
        print("|")
        print("|")
        print("|")
        while i > cycle:
            print(f"Item added: snail_map[{i}][{j}] = {snail_map[i][j]}")
            snail.append(snail_map[i][j])
            i -=1

        i += 1
        j += 1
        cycle += 1

        print(f"Snail: {snail}")

    return snail


array = [[1,2,3],
         [4,5,6],
         [7,8,9]]

snail(array)
        