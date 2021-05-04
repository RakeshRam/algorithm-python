# Rabin-Karp Algorithm
# makes use of hash functions and the rolling hash technique


class RabinKarp:
    def __init__(self, text, pattern):
        self.text = text
        self.pattern = pattern
        self.size = len(pattern)
        self.total_alpha = 62   # Base62 [A-Za-z0-9]

        self.text_hash = self.__hash(text)
        self.pattern_hash = self.__hash(pattern)

        self.count = 0
        self.window_start = 0
        self.window_end = len(pattern)
        self.positions = []              # Pattern Position in Text

    # Validate Text is not empty
    @property
    def text(self):
        return self._text

    # Validate Text is not empty
    @text.setter
    def text(self, text):
        if text == "":
            raise ValueError("Text cannot be empty")
        self._text = text

    # Validate Pattern is not empty
    @property
    def pattern(self):
        return self._pattern

    # Validate Pattern is not empty
    @pattern.setter
    def pattern(self, pattern):
        if pattern == "":
            raise ValueError("Pattern cannot be empty")
        self._pattern = pattern

    def __hash(self, txt):
        """
        HASH Algo
        """
        value = 0
        for i in range(self.size):
            value += (ord(txt[i]) - ord("a")+1) * \
                (self.total_alpha**(self.size - i - 1))
        return value

    def __update_hash(self):
        """
        Rolling Hash
        """
        self.text_hash -= (ord(self.text[self.window_start]) -
                           ord("a")+1)*self.total_alpha**(self.size-1)
        self.text_hash *= self.total_alpha
        self.text_hash += ord(self.text[self.window_end]) - ord("a")+1
        self.window_start += 1
        self.window_end += 1

    def rabin_karp(self):
        """
        Rabin Karp function
        Best & average-case: O(m + n) 
        Worst-case: O(nm)
        MyRef: https://brilliant.org/wiki/rabin-karp-algorithm/
        """
        while True:
            # print(self.text_hash, self.text[self.window_start: self.window_end])
            if self.pattern_hash == self.text_hash:   # Check if hash match
                self.count += 1   # Increment count
                # Append ptrn position
                self.positions.append((self.window_start, self.window_end))
            if self.window_end >= len(self.text):
                break
            self.__update_hash()    # Update text hash
        return self.count

    def get_ptrn_positions(self):
        """
        Get postion of pattern in text
        """
        return self.positions

    def brute_force(self):
        """
        Brute-Force Method: O(nm)
        """
        c = 0
        for i in range(len(self.text)):
            val = self.text[i: self.size+i]  # Sliding Window
            if len(val) < self.size:
                break
            if self.pattern == val:
                c += 1
        return c


data = [
    ("AABAACABAA", "BAA", 2),
    ("ata", "ata", 1),
    ("atata", "ata", 2),
    ("aaaaaaa", "ata", 0),
    ("ata", "", 0),
    ("aagcgagcgatatatat", "ata", 3),
    ("abcdefgh", "a", 1),
    ("abcdefgh", "d", 1),
    ("balloonsandcupcakes", "cupcakes", 1),
    ("GEEKS FOR GEEKS", "GEEK", 2)
]
for txt, ptrn, result in data:
    try:
        rp = RabinKarp(txt, ptrn)
        print(f"Text: {rp.text}, Pattern: {rp.pattern}")
        print("Rabin-Karp", rp.rabin_karp() == result)
        print("Brute Force", rp.brute_force() == result, end="\n\n")
    except:
        print("Args should not be empty!", end="\n\n")
