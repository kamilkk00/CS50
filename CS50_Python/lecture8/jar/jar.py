class Jar:
    def __init__(self, capacity=12):
        if capacity == str(capacity) or capacity != int(capacity) or  capacity < 0:
            raise ValueError
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        x = ""
        for _ in range(self._size):
            x = x + "🍪"
        return x

    def deposit(self, n):
        n = n + self._size
        self._size = n
        if n > 12:
            raise ValueError ("Too much cookie")

    def withdraw(self, n):
        n = self._size - n
        self._size = n
        if n < 0:
            raise ValueError ("Not enought cookie")


    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size


