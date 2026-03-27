class HashMap:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.buckets = [[] for _ in range(capacity)]

    # O(1)
    def __len__(self):
        return self.size

    # O(1) or O(n)
    def __contains__(self, key):
        index = self._hash_function(key)
        bucket = self.buckets[index]

        for k,v in bucket:
            if k == key:
                return True
            
        return False

    # O(1) or O(n)
    def put(self, key, value):
        index = self._hash_function(key)
        bucket = self.buckets[index]
        for i, (k,v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key,value)
                break
        else:
            bucket.append((key, value))
            self.size += 1  

    # O(1) or O(n)
    def get(self, key):
        index = self._hash_function(key)
        bucket = self.buckets[index]

        for k,v in bucket:
            if k == key:
                return v
            
        raise KeyError("Key not found")

    # O(1) or O(n)
    def remove(self, key):
        index = self._hash_function(key)
        bucket = self.buckets[index]

        for i, (k,v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                self.size -= 1
                break
        else:
            raise KeyError("Key not found")

    # O(n)
    def keys(self):
        return [k for bucket in self.buckets for k, _ in bucket]

    # O(n)
    def values(self):
        return [v for bucket in self.buckets for _, v in bucket]

    # O(n)
    def items(self):
        return [(k, v) for bucket in self.buckets for k, v in bucket]

    # O(k), k - key length
    def _hash_function(self, key):
        key_string = str(key)
        hash_result = 0

        for c in key_string:
            hash_result = (hash_result * 31 + ord(c)) % self.capacity
        
        return hash_result

if __name__ == '__main__':
    hash_map = HashMap(5)

    hash_map.put('name', 'Roman')
    hash_map.put('age', 18)

    print(hash_map.items())