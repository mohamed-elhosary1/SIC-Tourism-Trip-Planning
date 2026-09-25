#-------------------------------------------------------------
# 1) Data Structures
#-------------------------------------------------------------

#class Node:
#    def __init__(self, data):
#        pass
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0


class HashTable:

    def __init__(self, size=101):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        total = 0
        for ch in str(key):
            total += ord(ch)
        return total % self.size

    def insert(self, key, value):
        index = self._hash(key)
        bucket = self.table[index]

        for pair in bucket:
            if pair[0] == key:
                pair[1] = value
                return

        bucket.append([key, value])

    def get(self, key):
        index = self._hash(key)
        bucket = self.table[index]

        for pair in bucket:
            if pair[0] == key:
                return pair[1]

        return None

    def remove(self, key):
        index = self._hash(key)
        bucket = self.table[index]

        for pair in bucket:
            if pair[0] == key:
                bucket.remove(pair)
                return True

        return False

    def contains(self, key):
        return self.get(key) is not None


#-------------------------------------------------------------
# 2) Algorithms
#-------------------------------------------------------------

def binary_search(sorted_list, target_name, key=lambda x: x):
    low = 0
    high = len(sorted_list) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_value = key(sorted_list[mid])

        if mid_value == target_name:
            return mid
        elif mid_value < target_name:
            low = mid + 1
        else:
            high = mid - 1

    return -1


def quick_sort(items, key, ascending=True):
    if len(items) <= 1:
        return items

    pivot = items[len(items) // 2]
    pivot_value = key(pivot)

    left = []
    middle = []
    right = []

    for item in items:
        value = key(item)
        if value < pivot_value:
            left.append(item)
        elif value > pivot_value:
            right.append(item)
        else:
            middle.append(item)

    if ascending:
        return quick_sort(left, key, ascending) + middle + quick_sort(right, key, ascending)
    else:
        return quick_sort(right, key, ascending) + middle + quick_sort(left, key, ascending)