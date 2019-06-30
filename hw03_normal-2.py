def sort_to_max(orgin_list):
    g = 0
    d = 1
    while d < len(orgin_list):
        while g < (len(orgin_list) - 1):
            if orgin_list[g] > orgin_list[g+1]:
                orgin_list[g], orgin_list[g+1] = orgin_list[g+1], orgin_list[g]
            g += 1
        d += 1
        g = 0
 
orgin_list = [2, 10, -12, 2.5, 20, -11, 4, 4, 0]
sort_to_max(orgin_list)
print(orgin_list)