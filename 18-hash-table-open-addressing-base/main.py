class HashTableOpenAddressingBase:
    def __init__(self, capacity=7, load_factor=0.65):
        if capacity <= 0:
            raise ValueError(f"Illegal capacity: {capacity}")
        if load_factor <= 0 or not isinstance(load_factor, (float, int)):
            raise ValueError(f"Illegal load factor: {load_factor}")

        self.load_factor = load_factor
        self.capacity = max(7, capacity)
        self.threshold = int(self.capacity * self.load_factor)

        self.keys = [None] * self.capacity
        self.values = [None] * self.capacity

        self.TOMBSTONE = object()
        self.size = 0
        self.modification_count = 0

    def normalize_index(self, hash_code):
        return (hash_code & 0x7FFFFFFF) % self.capacity

    def setup_probing(self, key):
        raise NotImplementedError(
            "setupProbing() must be implemented by subclasses")

    def probe(self, x):
        raise NotImplementedError("probe() must be implemented by subclasses")

    def adjust_capacity(self):
        raise NotImplementedError(
            "adjustCapacity() must be implemented by subclasses")

    def increase_capacity(self):
        self.capacity = (2 * self.capacity) + 1

    def clear(self):
        self.keys = [None] * self.capacity
        self.values = [None] * self.capacity
        self.size = 0
        self.modification_count += 1

    def get_size(self):
        return self.size

    def get_capacity(self):
        return self.capacity

    def is_empty(self):
        return self.size == 0

    def get_hash(self, key):
        if isinstance(key, str):
            hash_code = 0
            for char in key:
                hash_code = (31 * hash_code + ord(char)) & 0xFFFFFFFF
            return hash_code
        elif isinstance(key, int):
            return key
        else:
            raise TypeError("Unsupported key type")

    def insert(self, key, value):
        if key is None:
            raise ValueError("Null key")
        if self.size >= self.threshold:
            self.resize_table()

        self.setup_probing(key)
        offset = self.normalize_index(self.get_hash(key))

        for i in range(self.capacity):
            index = self.normalize_index(offset + self.probe(i))
            if self.keys[index] is None or self.keys[index] is self.TOMBSTONE:
                self.keys[index] = key
                self.values[index] = value
                self.size += 1
                self.modification_count += 1
                return
            elif self.keys[index] == key:
                self.values[index] = value
                return

    def has_key(self, key):
        if key is None:
            raise ValueError("Null key")

        self.setup_probing(key)
        offset = self.normalize_index(self.get_hash(key))

        for i in range(self.capacity):
            index = self.normalize_index(offset + self.probe(i))
            if self.keys[index] == key:
                return True
            elif self.keys[index] is None:
                return False

        return False

    def get(self, key):
        if key is None:
            raise ValueError("Null key")

        self.setup_probing(key)
        offset = self.normalize_index(self.get_hash(key))

        for i in range(self.capacity):
            index = self.normalize_index(offset + self.probe(i))
            if self.keys[index] == key:
                return self.values[index]
            elif self.keys[index] is None:
                return None

        return None

    def remove(self, key):
        if key is None:
            raise ValueError("Null key")

        self.setup_probing(key)
        offset = self.normalize_index(self.get_hash(key))

        for i in range(self.capacity):
            index = self.normalize_index(offset + self.probe(i))
            if self.keys[index] == key:
                self.size -= 1
                self.modification_count += 1
                old_value = self.values[index]
                self.keys[index] = self.TOMBSTONE
                self.values[index] = None
                return old_value
            elif self.keys[index] is None:
                return None

        return None

    def resize_table(self):
        old_capacity = self.capacity
        old_keys = self.keys[:]
        old_values = self.values[:]

        self.increase_capacity()
        self.threshold = int(self.capacity * self.load_factor)
        self.keys = [None] * self.capacity
        self.values = [None] * self.capacity
        self.size = 0

        for i in range(old_capacity):
            if old_keys[i] is not None and old_keys[i] is not self.TOMBSTONE:
                self.insert(old_keys[i], old_values[i])

    def __str__(self):
        result = "{"
        for i in range(self.capacity):
            if self.keys[i] is not None and self.keys[i] is not self.TOMBSTONE:
                result += f"{self.keys[i]} => {self.values[i]}, "
        result += "}"
        return result

    def __iter__(self):
        self._index = 0
        self._keys_left = self.size
        self._modification_count_at_start = self.modification_count
        return self

    def __next__(self):
        if self._modification_count_at_start != self.modification_count:
            raise RuntimeError("Concurrent modification detected")

        while self._index < self.capacity and (self.keys[self._index] is None or self.keys[self._index] is self.TOMBSTONE):
            self._index += 1

        if self._keys_left > 0 and self._index < self.capacity:
            key = self.keys[self._index]
            self._index += 1
            self._keys_left -= 1
            return key
        else:
            raise StopIteration

# Example subclass for linear probing


class HashTableLinearProbing(HashTableOpenAddressingBase):
    LINEAR_CONSTANT = 17

    def setup_probing(self, key):
        pass  # No specific setup needed for linear probing

    def probe(self, x):
        return x * HashTableLinearProbing.LINEAR_CONSTANT

    def adjust_capacity(self):
        pass  # Adjust capacity if needed based on subclass needs


# Example usage
if __name__ == "__main__":
    ht = HashTableLinearProbing()
    ht.insert("name", "Alice")
    ht.insert("age", 30)
    ht.insert("city", "New York")

    print(ht.get("name"))  # Output: Alice
    print(ht.get("age"))   # Output: 30
    print(ht.get("city"))  # Output: New York

    print(ht.has_key("name"))  # Output: True
    print(ht.has_key("country"))  # Output: False

    print(ht.remove("city"))  # Output: New York
    print(ht.get("city"))  # Output: None

    print(ht)  # Output: {name => Alice, age => 30, }

    for key in ht:
        print(key)  # Output: name, age

print("###############################################")
print("############  Quadratic Probing  ##############")
print("###############################################")


class HashTableQuadraticProbing(HashTableOpenAddressingBase):
    def __init__(self, capacity=7, load_factor=0.65, c1=1, c2=3):
        super().__init__(capacity, load_factor)
        self.c1 = c1
        self.c2 = c2

    def setup_probing(self, key):
        pass  # No specific setup needed for quadratic probing

    def probe(self, x):
        # Quadratic probing formula: x^2 + c1 * x + c2
        return self.c1 * x + self.c2 * x * x

    def adjust_capacity(self):
        pass  # Adjust capacity if needed based on subclass needs


# Example usage
if __name__ == "__main__":
    ht = HashTableQuadraticProbing()
    ht.insert("name", "Alice")
    ht.insert("age", 30)
    ht.insert("city", "New York")
    ht.insert("country", "USA")

    print(ht.get("name"))  # Output: Alice
    print(ht.get("age"))   # Output: 30
    print(ht.get("city"))  # Output: New York
    print(ht.get("country"))  # Output: USA

    print(ht.has_key("name"))  # Output: True
    print(ht.has_key("state"))  # Output: False

    print(ht.remove("city"))  # Output: New York
    print(ht.get("city"))  # Output: None

    print(ht)  # Output: {name => Alice, age => 30, country => USA, }

    for key in ht:
        print(key)  # Output: name, age, country

print("###############################################")
print("############  Quadratic Probing  ##############")
print("###############################################")


class HashTableDoubleHashing(HashTableOpenAddressingBase):
    def __init__(self, capacity=7, load_factor=0.65):
        super().__init__(capacity, load_factor)

    def setup_probing(self, key):
        # Calculate the hash of the key using a secondary hash function
        self.secondary_hash = self.secondary_hash_function(key)

    def probe(self, x):
        # Double hashing formula: x * secondary_hash
        return x * self.secondary_hash

    def adjust_capacity(self):
        pass  # Adjust capacity if needed based on subclass needs

    def secondary_hash_function(self, key):
        # A secondary hash function that should return a value in the range 1 to capacity-1
        hash_value = hash(key)
        return 1 + (hash_value % (self.capacity - 1))


# Example usage
if __name__ == "__main__":
    ht = HashTableDoubleHashing()
    ht.insert("name", "Alice")
    ht.insert("age", 30)
    ht.insert("city", "New York")
    ht.insert("country", "USA")

    print(ht.get("name"))  # Output: Alice
    print(ht.get("age"))   # Output: 30
    print(ht.get("city"))  # Output: New York
    print(ht.get("country"))  # Output: USA

    print(ht.has_key("name"))  # Output: True
    print(ht.has_key("state"))  # Output: False

    print(ht.remove("city"))  # Output: New York
    print(ht.get("city"))  # Output: None

    print(ht)  # Output: {name => Alice, age => 30, country => USA, }

    for key in ht:
        print(key)  # Output: name, age, country
