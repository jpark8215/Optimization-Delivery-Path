# O(N)
# HashTable class using chaining.
class ChainingHashTable:

    # Constructor with optional initial capacity parameter
    # Assigns all buckets with an empty list
    def __init__(self, initial_capacity=10):
        # Initializes hash table with empty bucket list entries
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])

    # O(1)
    # Inserts a new item into the hash table
    def insert(self, key, item):
        # Gets bucket list where an item goes
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]
        # Updates key if it is already in the bucket
        for kv in bucket_list:
            if kv[0] == key:
                kv[1] = item
                return True
        # If not, insert the item to the end of bucket list
        key_value = [key, item]
        bucket_list.append(key_value)
        return True

    # O(N)
    # Searches for an item with matching key in hash table
    # Returns the item if found, or None if not found
    def search(self, key):
        # Gets bucket list where the key is
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]
        # Searches for the key in bucket list
        for kv in bucket_list:
            if kv[0] == key:
                return kv[1]
        return None

    # O(N)
    # Removes an item with matching key from hash table
    def remove(self, key):
        # get the bucket list where this item will be removed from.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]
        # Removes the item from bucket list if it is present
        for kv in bucket_list:
            if kv[0] == key:
                bucket_list.remove([kv[0], kv[1]])

    # O(n)
    # Updates package in hash table
    def update(self, key, value):
        bucket = hash(key) % len(self.table)
        if self.table[bucket] is None:
            print('Error with updating key #: ' + key)
        else:
            for kv in self.table[bucket]:
                if kv[0] == key:
                    kv[1] = value
                    print(kv[1])
                    return True
