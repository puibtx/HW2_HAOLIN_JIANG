def reverse_list(a):
    b = []
    length = len(a)-1
    while length >=0:
        b.append(a[length])
        length -= 1 
    return(b)
