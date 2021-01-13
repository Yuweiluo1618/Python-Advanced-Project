from contextlib import contextmanager

@contextmanager
def myopen(file_name, file_mode):
    print("enter")
    file = open(file_name, file_mode)
    yield file
    print("exit")
    file.close()



if __name__ == '__main__':
    with myopen("test.txt", 'r') as file:
        print(file.read())