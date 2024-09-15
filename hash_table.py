""" Understanding Hasing with Chaining through Hash Table """

import random

class HashTable:
    """ Data structure to store data based on the key """
    def __init__(self, size = 10):
        self.size = size
        self.prime_number = 1000000007                              # A large prime number
        self.a = random.randint(1, self.prime_number - 1)
        self.b = random.randint(0, self.prime_number - 1)
        self.table = [[] for _ in range(size)]

    def universal_hash(self, key):
        """ Universal hash function using modulo (((ak + b) mod p) mod m) """
        return ((self.a * key + self.b) % self.prime_number) % self.size

    def insert(self, key, value):
        """ Insert a key-value pair into the hash table """
        hash_index = self.universal_hash(key)

        # Check if the key already exists, and update the value if it does
        for pair in self.table[hash_index]:
            if pair[0] == key:
                pair[1] = value
                return

        # If key doesn't exist, append the new key-value in the table
        self.table[hash_index].append([key,value])

    def search(self, key):
        """ Seach for the value based on the key provided """
        hash_index = self.universal_hash(key)

        # Search through the list at the hash index for the key
        # Return the value if the key is found
        for pair in self.table[hash_index]:
            if pair[0] == key:
                return pair[1]

        # Return None if the key is not found
        return None

    def delete(self, key):
        """ Delete a key-value pair from the hash table """
        hash_index = self.universal_hash(key)

        # Search through the list at the hash index for the key
        # Delete the key-value pair if the key is found and return true
        for index, pair in enumerate(self.table[hash_index]):
            if pair[0] == key:
                del self.table[hash_index][index]
                return True

        # Return false if the key is not found
        return False


hash_table = HashTable()                            # Create a hash table of default slot size 10

# Insert key-value pairs
hash_table.insert(1, "Peoria")
hash_table.insert(10, "Dallas")
hash_table.insert(5, "Pheonix")
hash_table.insert(20, "Austin")
hash_table.insert(24, "Brooklyn")
hash_table.insert(13, "Williamsburg")

# Display the hash table
print("Hash Table after insertions:")
for i, bucket in enumerate(hash_table.table):
    print(f"Index {i}: {bucket}")

# Search for location based on the key
print("\nSearch for key 24:", hash_table.search(24))
print("Search for key 13:", hash_table.search(13))
print("Search for key 5:", hash_table.search(5))
print("Search for key 30 (not present):", hash_table.search(30))

# Delete Dallas and Williamsburg
hash_table.delete(10)
hash_table.delete(13)

# Display the hash table after deletion
print("\nHash Table after deletion:")
for i, bucket in enumerate(hash_table.table):
    print(f"Index {i}: {bucket}")
