def swap_list(a):
    size = len(a)-1
    mid = size//2
    a[size], a[mid] = a[mid], a[size]
    return a
