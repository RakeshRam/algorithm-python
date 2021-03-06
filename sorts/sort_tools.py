# Collection Of Sorting Algorithims. 
# https://en.wikipedia.org/wiki/Sorting_algorithm

import time
from itertools import chain


class Sorts:
    """
    Collection of Sorting Algorithims.
    Attributes:
    -----------
            lst : list object
    Methods:
    --------
            1. radix_sort()
            2. count_sort()
            3. merge_sort()
            4. quick_sort()
            5. heap_sort()
            6. bubble_sort()
            7. insertion_sort()
            8. selection_sort()sssss
    To Use:
    -------
            s = Sorts([1,3,2,0,8,9,6,7,3,5,666,2,6,9,2,777,3,7,8,1,0,0,0,3,3,5,7])
            print(s.radix_sort())
            ...
    """
    def __init__(self, lst):
        self.lst = lst

    def __lst_cpy(self):
        return self.lst.copy()

    def __get_max(self):
        return max(self.lst)

    def __get_len(self):
        return len(self.lst)

    def __timediff(f):
        def time_calc(self):
            start = time.time()
            rv = f(self)
            print(f"Total Time({f.__name__}): {time.time() - start}")
            return rv
        return time_calc

    @__timediff
    def radix_sort(self):
        """
        Radix Sort: T(n) = O(d*(n+b))
                 d: Number of digits in the given list.
                 n: Number of elements in the list.
                 b: Bucket size used.
        https://en.wikipedia.org/wiki/Radix_sort

        Formula Desc: item //10 ** (n) % 10
        >>> item = 123
        >>> n = 0
        >>> item //10 ** (n) % 10  ==> 3
        >>> n = 1
        >>> item //10 ** (n) % 10  ==> 2
        >>> n = 2                 
        >>> item //10 ** (n) % 10
        """
        n_digits = str(self.__get_max())                                 # Get max number
        lst_cpy = self.__lst_cpy()                                       # Sort on copy of list
        for n in range(len(n_digits)):                                   # Iterate each digit
            temp = [[] for _ in range(10)]                               # Create Bucket 
            for item in lst_cpy:
                num = item //10 ** (n) % 10                              # Formula to get each digit in number
                temp[num].append(item)
            lst_cpy = chain.from_iterable(temp)                          # Flatten List
        return list(lst_cpy)

    @__timediff
    def count_sort(self):
        """
        Count Sort: 
        https://en.wikipedia.org/wiki/Counting_sort
        """
        pass

    def __merge_sort(self, data, first, last):
        if first < last:                                  # Check to confirm multiple elements in list
            middle = (first+last)//2                      # Get middle element in list
            self.__merge_sort(data, first, middle)        # Sort Left side
            self.__merge_sort(data, middle+1, last)       # Sort Right side
            self.__merge(data, first, middle, last)       # Merge list

    def __merge(self, data, first, middle, last):
        L = data[first: middle+1]
        R = data[middle+1: last+1]

        R.append(99999999)                                  # WIll be ignored because not in original list
        L.append(99999999)                                  # WIll be ignored because not in original list
        i = j = 0
        for k in range(first, last+1):
            if L[i] <= R[j]:
                # Left List
                data[k] = L[i]
                i += 1
            else:
                # Right List
                data[k] = R[j]
                j += 1

    @__timediff
    def merge_sort(self):
        """
        Merge Sort: O(n log n)
        https://en.wikipedia.org/wiki/Merge_sort
        """
        lst_cpy = self.__lst_cpy()
        self.__merge_sort(lst_cpy, 0, self.__get_len()-1)
        return lst_cpy

    @__timediff
    def quick_sort(self):
        """
        Quick Sort: O(n log n) 
        https://en.wikipedia.org/wiki/Quicksort
        """
        pass

    @__timediff
    def heap_sort(self):
        """
        Heap Sort: O(n log n) 
        https://en.wikipedia.org/wiki/Heapsort
        """
        pass

    @__timediff
    def bubble_sort(self):
        """
        Bubble Sort: ??(n2)
                  n: Number of elements in the list.
        https://en.wikipedia.org/wiki/Bubble_sort
        """
        length = self.__get_len() - 1
        lst_cpy = self.__lst_cpy()
        for i in range(0, length):
            for j in range(0,  length-i):
                if lst_cpy[j] > lst_cpy[j + 1]:                                 # Compare each element until all values are sorted
                    lst_cpy[j], lst_cpy[j+1] = lst_cpy[j+1], lst_cpy[j]       # Swap
        return lst_cpy 

    @__timediff
    def insertion_sort(self):
        """
        Insertion Sort: ??(n2)
                     n: Number of elements in the list.
        https://en.wikipedia.org/wiki/Insertion_sort
        """
        lst_cpy = self.__lst_cpy()
        for i in range(1, self.__get_len()):
            j = i-1                                                               # Select element
            while lst_cpy[j] > lst_cpy[j+1] and j >= 0:                         # Check until the first value is in correct place & also make sure the index does not got to negative.
                lst_cpy[j], lst_cpy[j+1] = lst_cpy[j+1], lst_cpy[j]           # Swap         
                j -= 1                                                            # Decrement the index
        return lst_cpy

    @__timediff
    def selection_sort(self):
        """
        Selection Sort:  O(n2)
                     n: Number of elements in the list.
        https://en.wikipedia.org/wiki/Selection_sort 
        """
        lst_cpy = self.__lst_cpy()
        for i in range(0, self.__get_len()-1):             # Start from first element
            min_index = i
            for j in range(i+1, self.__get_len()):         # Check from second element
                if lst_cpy[j] < lst_cpy[min_index]:      # Compare which is minimum
                    min_index = j

            if min_index != i:                             # Only swap if the index are different
                lst_cpy[i], lst_cpy[min_index] = lst_cpy[min_index], lst_cpy[i]    # Swap
        return lst_cpy


