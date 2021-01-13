class Myfile(object):
    def __init__(self, file_name, file_mode):
        self.file_name = file_name
        self.file_mode = file_mode

    def __enter__(self):
        print("enter")
        self.file = open(self.file_name, self.file_mode)
        return  self.file
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("exit")
        self.file.close()

if __name__ == '__main__':
    with Myfile("test.txt", "r") as file:
        print(file.read())
