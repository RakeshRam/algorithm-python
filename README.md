# Algorithm-Python

Collection of Algorithms in Python

## <u>Content</u>

* [Sort.](sorts/README.md)
* [Search.](search/README.md)

---

## <u>Usage</u>

```bash
from sorts.sort_tools import Sorts
from random import shuffle

data = list(range(20000))
shuffle(data)

srt = Sorts(data)
print(srt.lst[:10], "Before")
print(srt.radix_sort()[:10])
print(srt.bubble_sort()[:10])
print(srt.insertion_sort()[:10])
print(srt.selection_sort()[:10])
print(srt.merge_sort()[:10])
```

Output:

```bash
[6067, 17866, 13829, 2137, 11537, 8067, 10738, 2189, 3151, 12717] Before
Total Time(radix_sort): 0.03800058364868164
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
Total Time(bubble_sort): 25.547104120254517
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
Total Time(insertion_sort): 21.524038314819336
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
Total Time(selection_sort): 9.173961162567139
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
Total Time(merge_sort): 0.057138919830322266
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```
