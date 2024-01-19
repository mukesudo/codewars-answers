def pig_it(text):
    #your code here
    
    my_list = text.split()

    for idx, item in enumerate(my_list):
        if item.isalpha():
            str_list = list(item)
            str_list.append(str_list.pop(0))
            item = ''.join(str_list)+'ay'
            my_list[idx] = item

    return ' '.join(my_list)