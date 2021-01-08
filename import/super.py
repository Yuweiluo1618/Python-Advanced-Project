class parent(object):
    def __init__(self, name):
        self.name = name
        print("parent")


class son(parent):
    def __init__(self, name, age):
        self.age = age
        super().__init__(name)
        print("son")


class grandson(son):
    def __init__(self, name, age, gender):
        self.gender = gender
        super().__init__(name, age)
        print("grandson")



if __name__ == '__main__':
    gs = grandson("we", 13, "male")
    print(grandson.__mro__)
