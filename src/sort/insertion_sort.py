

def sort(list):
    list_len = len(list)
    
    i = 1
    while i < list_len:
        k = i
        current_element = list[i]
        for j in range(i - 1, -1, -1):
            j_element = list[j]
            if j_element > current_element:
                list[j], list[k] = list[k], list[j]
                k -= 1
        i += 1


def test():
    list = [20, 10, 11, 2, 5, 44, 18, 56, 100, 33, 87]
    print(list)
    sort(list)
    print(list)        
        
test()