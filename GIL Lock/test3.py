import threading

def deadlock():
    while True:
        pass

t1 = threading.Thread(target=deadlock)
t1.start()

deadlock()