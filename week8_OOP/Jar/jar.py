class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self._size = 0

    @property
    def capacity(self):
        return self._capacity
    
    @capacity.setter
    def capacity(self, cap):
        if cap <= 0:
            raise ValueError("The capacity cannot be a negative number")
        self._capacity = cap

    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, num_of_cookies):
        if num_of_cookies < 0:
            raise ValueError("The number of cookies cannot be a negative number")
        self._size = num_of_cookies

    def __str__(self):
        return "🍪" * self._size

    def deposit(self, n):
        if self.size + n > self.capacity:
            raise ValueError("The number of cookies will exceed the maximum capacity")
        if n <= 0:
            raise ValueError("The number of cookies deposited needs to be positive")
        self.size += n
    
    def withdraw(self, n):
        if n > self.size:
            raise ValueError("The number of requested cookies is more than the available")
        if n <= 0:
            raise ValueError("The number of cookies withdrawn needs to be positive")
        self.size -= n


j = Jar(capacity=5)
print(j)         # ''
j.deposit(3)
print(j)         # '🍪🍪🍪'
j.withdraw(2)
print(j)         # '🍪'
print(j.capacity)  # 5
print(j.size)      # 1