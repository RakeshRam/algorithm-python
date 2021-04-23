class MapHash:
    def __init__(self, maxsize=6):
        self.maxsize = maxsize               # Real scenario 64.
        self.hash = [None] * self.maxsize    # Will be a 2D list

    def _get_hash_key(self, key):
        hash = sum(ord(k) for k in key)
        return hash % self.maxsize

    def add(self, key, value):
        hash_key = self._get_hash_key(key)       # Hash key
        hash_value = [key, value]
        # ADD
        if self.hash[hash_key] is None:
            self.hash[hash_key] = [hash_value]   # Key-value(IS a list)
            return True
        else:  # Update
            for pair in self.hash[hash_key]:  # Update-value
                if pair[0] == key:
                    pair[1] = value   # Update-value
                    return True
            # append new Key in same hash key
            self.hash[hash_key].append(hash_value)

    def get(self, key):
        hash_key = self._get_hash_key(key)
        if self.hash[hash_key] is not None:
            for k, v in self.hash[hash_key]:
                if k == key:
                    return v
        return "Key Error"

    def delete(self, key):
        hash_key = self._get_hash_key(key)
        if self.hash[hash_key] is not None:
            for i in range(len(self.hash[hash_key])):
                if self.hash[hash_key][i][0] == key:
                    self.hash[hash_key].pop(i)
                    return True
        else:
            return "Key Error"

    def __str__(self):
        return str(self.hash)

    def pprint(self):
        for item in self.hash:
            if item is not None:
                print(str(item))


data = MapHash()
data.add('CaptainAmerica', '567-8888')
data.add('Thor', '293-6753')
data.add('Thor', '333-8233')
data.add('IronMan', '293-8625')
data.add('BlackWidow', '852-6551')
data.add('Hulk', '632-4123')
data.add('Spiderman', '567-2188')
data.add('BlackPanther', '777-8888')

print(data)
print(data.get('BlackPanther'))
print(data.delete('BlackPanther'))
print(data.pprint())
