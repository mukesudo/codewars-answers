def delete_nth(order,max_e):
    # code here
    
    list_with_n_occurence=[]
    for i in order:
        if order.count(i)<=max_e:
            list_with_n_occurence.append(i)
        elif list_with_n_occurence.count(i)<max_e:
            list_with_n_occurence.append(i)
    return list_with_n_occurence