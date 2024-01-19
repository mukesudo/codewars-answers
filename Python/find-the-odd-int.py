def find_it(seq):
    
    seq_set = set(seq)
    for item in seq_set:
        if seq.count(item)%2 != 0:
            return item