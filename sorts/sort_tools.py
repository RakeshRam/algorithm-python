# Collection Of Sorting Algorithims. 
# https://en.wikipedia.org/wiki/Sorting_algorithm

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

    def __get_max(self):
        return max(self.lst)

    def __get_len(self):
        return len(self.lst)

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
        for n in range(len(n_digits)):                                   # Iterate each digit
            temp = [[] for _ in range(10)]                               # Create Bucket 
            for item in self.lst:
                num = item //10 ** (n) % 10                              # Formula to get each digit in number
                temp[num].append(item)
            self.lst = chain.from_iterable(temp)                         # Flatten List
        return list(self.lst)

    def count_sort(self):
        """
        Count Sort: 
        https://en.wikipedia.org/wiki/Counting_sort
        """
        pass

    def merge_sort(self):
        """
        Merge Sort: O(n log n)
        https://en.wikipedia.org/wiki/Merge_sort
        """
        pass

    def quick_sort(self):
        """
        Quick Sort: O(n log n) 
        https://en.wikipedia.org/wiki/Quicksort
        """
        pass

    def heap_sort(self):
        """
        Heap Sort: O(n log n) 
        https://en.wikipedia.org/wiki/Heapsort
        """
        pass

    def bubble_sort(self):
        """
        Bubble Sort: О(n2)
                  n: Number of elements in the list.
        https://en.wikipedia.org/wiki/Bubble_sort
        """
        length = self.__get_len() - 1
        for i in range(0, length):
            for j in range(0,  length-i):
                if self.lst[j] > self.lst[j + 1]:                                 # Compare each element until all values are sorted
                    self.lst[j], self.lst[j+1] = self.lst[j+1], self.lst[j]       # Swap
        return self.lst 

    def insertion_sort(self):
        """
        Insertion Sort: О(n2)
                     n: Number of elements in the list.
        https://en.wikipedia.org/wiki/Insertion_sort
        """
        for i in range(1, self.__get_len()):
            j = i-1                                                               # Select element
            while self.lst[j] > self.lst[j+1] and j >= 0:                         # Check until the first value is in correct place & also make sure the index does not got to negative.
                self.lst[j], self.lst[j+1] = self.lst[j+1], self.lst[j]           # Swap         
                j -= 1                                                            # Decrement the index
        return self.lst

    def selection_sort(self):
        """
        Selection Sort:  O(n2)
                     n: Number of elements in the list.
        https://en.wikipedia.org/wiki/Selection_sort 
        """
        for i in range(0, self.__get_len()-1):             # Start from first element
            min_index = i
            for j in range(i+1, self.__get_len()):         # Check from second element
                if self.lst[j] < self.lst[min_index]:      # Compare which is minimum
                    min_index = j

            if min_index != i:                             # Only swap if the index are different
                self.lst[i], self.lst[min_index] = self.lst[min_index], self.lst[i]    # Swap
        return self.lst


