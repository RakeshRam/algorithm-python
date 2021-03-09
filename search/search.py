# Collection Of Search Algorithims. 

def binary_search(lst, to_find):
    """
    Binary Search: O(log n)
                n: Number of elements in the list
    Works only on Sorted array.
    https://en.wikipedia.org/wiki/Binary_search_algorithm
    """
    if to_find > lst[-1]:                             # Check if `to_find` is out of `lst` range
        return False
    if to_find == lst[0] or  to_find == lst[-1]:      # Check if first or last element is == `to_find`
        return True

    middle = (len(lst)-1)//2                          # Find mid-point of list
    mid_num = lst[middle]                             # Get middle element
    if mid_num == to_find:                            # Check if element == `to_find`
        return True
    if to_find > mid_num:                              
        return binary_search(lst[middle:], to_find)   # If `to_find` is greater than mid-point, search right side  `lst`
    else:
        return binary_search(lst[:middle], to_find)   # If `to_find` is lesser than mid-point, search left side of `lst`