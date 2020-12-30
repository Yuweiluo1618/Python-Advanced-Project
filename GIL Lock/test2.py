import multiprocessing

def deadloop():
    while True:
        pass

p1 = multiprocessing.Process(target = deadloop)
p1.start()

deadloop()