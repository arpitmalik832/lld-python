import threading
from threading import Thread


# way 1
def print_hello_world():
    print("Hello World with thread ID: " + str(threading.current_thread().name) + "\t")


th = Thread(target=print_hello_world)
th.start()
print_hello_world()


# way 2
class MyThread(Thread):
    def run(self):
        print_hello_world()


th2 = MyThread()
th2.start()
