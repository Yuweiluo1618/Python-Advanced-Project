class Fibonacci(object):
    def __init__(self, num):
        self.num = num
        self.cur_index = 0

        self.a = 1
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.cur_index < self.num:
            value = self.a
            self.a, self.b = self.b, self.a + self.b
            self.cur_index += 1
            return value

        else:
            raise StopIteration


if __name__ == '__main__':
    fib = Fibonacci(7)
    for value in fib:
        print(value)