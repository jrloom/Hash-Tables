# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def __repr__(self):
        return f"<{self.key}, {self.value}>"


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys
    """

    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity

    def _hash(self, key):
        """
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        """
        return hash(key)

    def _hash_djb2(self, key):
        """
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        """
        pass

    def _hash_mod(self, key):
        """
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        """
        return self._hash(key) % self.capacity

    def insert(self, key, value):
        """
        Store the value with the given key.

        # Part 1: Hash collisions should be handled with an error warning. (Think about and
        # investigate the impact this will have on the tests)

        # Part 2: Change this so that hash collisions are handled with Linked List Chaining.

        Fill this in.
        """
        # index = self._hash_mod(key)

        # if self.count == self.storage:
        #     self.resize()
        # if self.storage[index]:
        #     print("exists")
        # else:
        #     self.storage[index] = LinkedPair(key, value)
        #     self.count += 1

        # # ? from lecture
        # # Hashmod the key to find the bucket
        # index = self._hash_mod(key)

        # # Check if a pair already exists in the bucket
        # pair = self.storage[index]
        # if pair is not None:
        #     # If so, overwrite the key/value and throw a warning
        #     if pair.key != key:
        #         print("Warning: Overwriting value")
        #         pair.key = key
        #         pair.value = value
        # else:
        #     # If not, Create a new LinkedPair and place it in the bucket
        #     self.storage[index] = LinkedPair(key, value)

        # * from the top...

        # find the bucket
        bucket = self._hash_mod(key)
        pair = self.storage[bucket]

        # if pair is none, store it
        if pair is None:
            self.storage[bucket] = LinkedPair(key, value)
            return

        # if keys match, replace value
        if pair.key == key:
            pair.value = value
            return

        # find matching keys
        while pair.next:
            pair = pair.next
            if pair.key == key:
                pair.value = value
                # print(f"{pair.key} - {pair.value}")
                return

        # if no key, set next
        pair.next = LinkedPair(key, value)

    def remove(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        """
        bucket = self._hash_mod(key)
        pair = self.storage[bucket]

        if pair is not None and pair.key == key:
            # print(f"removing {key}")
            self.storage[bucket] = None  # using the variable here fails
        else:
            print(f"{key} does not exist")

        # # ? from lecture
        # index = self._hash_mod(key)

        # # Check if a pair exists in the bucket with matching keys
        # if self.storage[index] is not None and self.storage[index].key == key:
        #     # If so, remove that pair
        #     self.storage[index] = None
        # else:
        #     # Else print warning
        #     print("Warning: Key does not exist")

    def retrieve(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        """
        # works in this file, fails test
        # index = self._hash_mod(key)

        # if self.storage[index]:
        #     if self.storage[index].key == key:
        #         return self.storage[index].value
        # else:
        #     return None

        # # ? from lecture - fails tests
        # # Get the index from hashmod
        # index = self._hash_mod(key)

        # # Check if a pair exists in the bucket with matching keys
        # if self.storage[index] is not None and self.storage[index].key == key:
        #     # If so, return the value
        #     return self.storage[index].value
        # else:
        #     # Else return None
        #     return None

        # * from the top, using a loop
        bucket = self._hash_mod(key)
        pair = self.storage[bucket]

        # find matching keys
        while pair:
            if pair.key == key:
                return pair.value
            # print(f"{pair} || {pair.next}")
            pair = pair.next

    def resize(self):
        """
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        """
        # doubles cap
        # self.capacity *= 2
        # new_storage = [None] * self.capacity

        # for i in range(self.count):
        #     new_storage[i] = self.storage[i]

        # self.storage = new_storage

        current_store = self.storage

        # doubles cap
        self.capacity *= 2
        self.storage = [None] * self.capacity

        # print(f">>> current store >>> {current_store}")
        # print(f">>> double cap >>> {self.storage}")

        for pair in current_store:
            # insert k/v's
            while pair:
                self.insert(pair.key, pair.value)
                pair = pair.next

        # print(f">>> at end >>> {self.storage}")
        return self.storage


if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print(f"storage --> {ht.storage}")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
