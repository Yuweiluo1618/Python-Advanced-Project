import time
class Fibonacci(object):
    def __init__(self):
        self.fir = 1
        self.sec = 1

    def __next__(self):
        value = self.fir
        sum = self.fir + self.sec
        self.fir = self.sec
        self.sec = sum

        time.sleep(5)
        return value

    def __iter__(self):
        return self


fib = Fibonacci()
for value in fib:
    print(value)