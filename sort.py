
# def sort_dictionary(dic):
#     mylist = []
#     for key, value in sorted(dic.items(), key=lambda r: r[1][1]):
#         mylist.append((key,value[0]))
#     return(mylist)

def sort_dictionary(dict1):
    list_dic = list(dict1.items())
    size = (len(list_dic))
    
    for index in range(size):
        min_index = index
 
        for j in range(index + 1, size):
            # select the minimum element in every iteration
            if list_dic[j][1][1] < list_dic[min_index][1][1]:
                min_index = j
         # swapping the elements to sort the array
        list_dic[index], list_dic[min_index] = list_dic[min_index], list_dic[index]
    
    list1 = []
    for i in range(len(list_dic)):
         list1.append((list_dic[i][0],list_dic[i][1][0]))
    
    
    return list1

