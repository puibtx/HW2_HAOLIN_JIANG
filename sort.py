
def sort_dictionary(dic):
    mylist = []
    for key, value in sorted(dic.items(), key=lambda r: r[1][1]):
        mylist.append((key,value[0]))
    return(mylist)

