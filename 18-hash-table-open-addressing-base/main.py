class Entry:
    def __init__(self, key, value):
        if key is None:
            raise ValueError("Null key is not allowed")
        self.key = key
        self.value = value
        self.hash = self.compute_hash()

    def compute_hash(self):
        # Hash function similar to JavaScript's hashCode()
        hash_value = 0
        for char in str(self.key):
            hash_value = (hash_value * 31 + ord(char)) & 0xFFFFFFFF
        return hash_value

    def __eq__(self, other):
        return self.hash == other.hash and self.key == other.key

    def __str__(self):
        return f"{self.key} => {self.value}"


class HashTableOpenAddressing:
    def __init__(self, capacity=3, max_load_factor=0.75):
        if capacity < 1:
            raise ValueError("Illegal capacity")
        if max_load_factor <= 0 or not (0 < max_load_factor < 1):
            raise ValueError("Illegal max_load_factor")

        self.max_load_factor = max_load_factor
        self.capacity = max(3, capacity)
        self.threshold = int(self.capacity * self.max_load_factor)
        self.size = 0
        self.table = [None] * self.capacity

    def normalize_index(self, key_hash):
        return abs(key_hash) % self.capacity

    def clear(self):
        self.table = [None] * self.capacity
        self.size = 0

    def contains_key(self, key):
        return self.has_key(key)

    def has_key(self, key):
        bucket_index = self.normalize_index(self.compute_hash(key))
        return self.probe_for_entry(bucket_index, key) is not None

    def put(self, key, value):
        return self.insert(key, value)

    def add(self, key, value):
        return self.insert(key, value)

    def insert(self, key, value):
        if key is None:
            raise ValueError("Null key is not allowed")
        new_entry = Entry(key, value)
        bucket_index = self.normalize_index(new_entry.hash)
        old_value = self.bucket_insert_entry(bucket_index, new_entry)
        if self.size > self.threshold:
            self.resize_table()
        return old_value

    def get(self, key):
        if key is None:
            return None
        bucket_index = self.normalize_index(self.compute_hash(key))
        entry = self.probe_for_entry(bucket_index, key)
        return entry.value if entry else None

    def remove(self, key):
        if key is None:
            return None
        bucket_index = self.normalize_index(self.compute_hash(key))
        return self.bucket_remove_entry(bucket_index, key)

    def probe_for_entry(self, start_index, key):
        index = start_index
        while self.table[index] is not None:
            if self.table[index].key == key:
                return self.table[index]
            index = (index + 1) % self.capacity
            if index == start_index:  # Full loop completed
                break
        return None

    def bucket_remove_entry(self, bucket_index, key):
        entry = self.probe_for_entry(bucket_index, key)
        if entry is not None:
            self.table[bucket_index] = None
            self.size -= 1
            # Rehash the entries in the same cluster
            next_index = (bucket_index + 1) % self.capacity
            while self.table[next_index] is not None:
                rehash_entry = self.table[next_index]
                self.table[next_index] = None
                self.size -= 1
                self.insert(rehash_entry.key, rehash_entry.value)
                next_index = (next_index + 1) % self.capacity
            return entry.value
        return None

    def bucket_insert_entry(self, bucket_index, entry):
        initial_index = bucket_index
        while self.table[bucket_index] is not None:
            if self.table[bucket_index].key == entry.key:
                old_value = self.table[bucket_index].value
                self.table[bucket_index].value = entry.value
                return old_value
            bucket_index = (bucket_index + 1) % self.capacity
            if bucket_index == initial_index:
                raise RuntimeError("Hash table is full")
        self.table[bucket_index] = entry
        self.size += 1
        return None

    def resize_table(self):
        old_table = self.table
        self.capacity *= 2
        self.threshold = int(self.capacity * self.max_load_factor)
        self.table = [None] * self.capacity
        self.size = 0

        for entry in old_table:
            if entry is not None:
                self.insert(entry.key, entry.value)

    def compute_hash(self, key):
        return Entry(key, None).compute_hash()

    def keys(self):
        return [entry.key for entry in self.table if entry is not None]

    def values(self):
        return [entry.value for entry in self.table if entry is not None]

    def __str__(self):
        entries = ', '.join(str(entry)
                            for entry in self.table if entry is not None)
        return '{' + entries + '}'


# Example usage
if __name__ == "__main__":
    hash_table = HashTableOpenAddressing()

    hash_table.put("key1", "value1")
    hash_table.put("key2", "value2")
    hash_table.put("key3", "value3")

    print("HashTable:", hash_table)
    print("Get 'key1':", hash_table.get("key1"))
    print("Contains 'key2':", hash_table.contains_key("key2"))
    print("Keys:", hash_table.keys())
    print("Values:", hash_table.values())
    print("Remove 'key3':", hash_table.remove("key3"))
    print("HashTable after removal:", hash_table)
