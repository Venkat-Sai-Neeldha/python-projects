# #6. Zoo Animal Sounds
# class Animal:
#     def make_sound(self):
#         return "Animal sound "
# class Dog(Animal):
#     def make_sound(self):
#         return "Dog sound "
# class Cat(Animal):
#     def make_sound(self):
#         return "Cat sound "
# class Cow(Animal):
#     def make_sound(self):
#         return "Cow sound "
#
# animals=[Dog(),Cat(),Cow()]
# for a in animals:
#     print(a.make_sound())

# #7)Custom Range Generator
# class MyRange:
#     def __init__(self, start, end):
#         self.start = start
#         self.end = end
#         self.current = start
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.current >= self.end:
#             raise StopIteration
#         self.current += 1
#         return self.current - 1
# for num in MyRange(1, 5):
#     print(num)

# #8) fibonacci number iterator
# class Fibonacci:
#     def __init__(self, limit):
#         self.limit = limit
#         self.a, self.b = 0, 1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.a > self.limit:
#             raise StopIteration
#
#         next_value = self.a
#         self.a, self.b = self.b, self.a + self.b
#         return next_value
#
# fib = Fibonacci(50)
# for num in fib:
#     print(num)

#9) Reverse String Iterator

class ReverseString:
    def __init__(self, text):
        self.text = text
        self.index = len(text) - 1

    def __iter__(self):

        return self

    def __next__(self):
        if self.index >= 0:
            char = self.text[self.index]
            self.index -= 1
            return char
        else:

            raise StopIteration

reverse_iterator = ReverseString("Hello")
for char in reverse_iterator:
    print(char,end="")


#10)File Line Grouper
class FileLineGrouper:
    def __init__(self, file_path, group_size):
        self.file_path = file_path
        self.group_size = group_size

    def __iter__(self):
        with open(self.file_path) as f:
            group = []
            for line in f:
                group.append(line.strip())
                if len(group) == self.group_size:
                    yield group
                    group = []
            if group:
                yield group
