class NumberIterator:
    def __init__(self, numbers):
        self.numbers = numbers
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.numbers):
            raise StopIteration
        value = self.numbers[self.index]
        self.index += 1
        return value

nums = NumberIterator([10, 20, 30, 40])
first = next(nums)
print(first)
second = next(nums)
print(second)
third = next(nums)
print(third)
fourth = next(nums)
print(fourth)
