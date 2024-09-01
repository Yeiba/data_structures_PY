class HashTable:
    def __init__(self, size=53):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        total = 0
        prime = 31
        for i in range(min(len(key), 100)):
            total = (total * prime + ord(key[i])) % self.size
        return total

    def insert(self, key, value):
        index = self._hash(key)
        # Check if the key already exists in the chain
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value  # Update existing key
                return
        # If the key does not exist, add the new key-value pair
        self.table[index].append([key, value])

    def get(self, key):
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        return None

    def remove(self, key):
        index = self._hash(key)
        for i, pair in enumerate(self.table[index]):
            if pair[0] == key:
                del self.table[index][i]
                return True
        return False

    def keys(self):
        keys_list = []
        for bucket in self.table:
            for pair in bucket:
                keys_list.append(pair[0])
        return keys_list

    def values(self):
        values_list = []
        for bucket in self.table:
            for pair in bucket:
                values_list.append(pair[1])
        return values_list


# Example usage
ht = HashTable()
ht.insert("pink", "#ffc0cb")
ht.insert("blue", "#0000ff")
ht.insert("black", "#000000")
ht.insert("white", "#ffffff")

print("Value associated with 'pink':", ht.get("pink"))  # "#ffc0cb"
print("Value associated with 'blue':", ht.get("blue"))  # "#0000ff"
print("Removing 'pink':", ht.remove("pink"))            # True
print("Value associated with 'pink' after removal:", ht.get("pink"))  # None
# ["blue", "black", "white"]
print("All keys in hash table:", ht.keys())
# ["#0000ff", "#000000", "#ffffff"]
print("All values in hash table:", ht.values())
