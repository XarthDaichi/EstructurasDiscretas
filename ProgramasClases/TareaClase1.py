from operator import truediv


def binary_search(list, searching_variable):
    found = False
    search = len(list)//2
    while(not found and search != 1):
        print(search)
        if list[search] < searching_variable:
            search = search + search // 2
        elif list[search] > searching_variable:
            search = search // 2
        else:
            found = True
    return search
            
list_variables = [1, 2, 3, 4, 5, 6, 7]
print(list_variables[binary_search(list_variables, 3)])
