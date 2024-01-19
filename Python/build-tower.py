def tower_builder(n_floors):
    # build here
    tower=[]
    star="*"
    space=" "
    for i in range(1,n_floors+1):
        floor=""
        for x in range(n_floors-i):
            floor+=space
        for j in range((2*i)-1):
            floor+=star
        for x in range(n_floors-i):
            floor+=space
        tower.append(floor)
    return tower