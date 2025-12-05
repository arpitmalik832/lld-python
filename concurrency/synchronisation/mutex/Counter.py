import threading


class Counter:
    def __init__(self, value):
        self.__value = value

    def get_value(self):
        return self.__value

    def set_value(self, value):
        self.__value = value


class Adder(threading.Thread):
    def __init__(self, counter: Counter, offset, mutex: threading.Lock):
        super().__init__()
        self.__counter = counter
        self.__offset = offset
        self.__mutex = mutex

    def run(self):
        self.__mutex.acquire()
        for i in range(100000):
            self.__counter.set_value(self.__counter.get_value() + self.__offset)
        self.__mutex.release()


class Subtractor(threading.Thread):
    def __init__(self, counter: Counter, offset, mutex: threading.Lock):
        super().__init__()
        self.__counter = counter
        self.__offset = offset
        self.__mutex = mutex

    def run(self):
        self.__mutex.acquire()
        for i in range(100000):
            self.__counter.set_value(self.__counter.get_value() - self.__offset)
        self.__mutex.release()


def main():
    counter = Counter(0)
    mutex = threading.Lock()
    a = Adder(counter, 1, mutex)
    s = Subtractor(counter, 1, mutex)
    print(counter.get_value())
    a.start()
    s.start()
    a.join()
    s.join()
    print(counter.get_value())


main()
