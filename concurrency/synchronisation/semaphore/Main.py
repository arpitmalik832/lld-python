import threading

from ds.LinkedListQueue import LinkedListQueue


class Item:
    def __init__(self, name: str, producer_name: str):
        self.__name = name
        print(f"{name} created by {producer_name}")

    def get_name(self):
        return self.__name


class Producer(threading.Thread):
    def __init__(
        self,
        store: LinkedListQueue,
        max_size: int,
        name: str,
        sema_producer: threading.Semaphore,
        sema_consumer: threading.Semaphore,
    ):
        super().__init__()
        self.__store = store
        self.__max_size = max_size
        self.__name = name
        self.__sema_producer = sema_producer
        self.__sema_consumer = sema_consumer

    def run(self):
        i = 0
        while True:
            self.__sema_producer.acquire()
            self.__store.enqueue(Item(f"item {i} of {self.__name}", self.__name))
            i += 1
            print(f"Store size : {self.__store.size()}")
            self.__sema_consumer.release()


class Consumer(threading.Thread):
    def __init__(
        self,
        store: LinkedListQueue,
        max_size: int,
        name: str,
        sema_producer: threading.Semaphore,
        sema_consumer: threading.Semaphore,
    ):
        super().__init__()
        self.__store = store
        self.__maxSize = max_size
        self.__name = name
        self.__sema_producer = sema_producer
        self.__sema_consumer = sema_consumer

    def run(self):
        while True:
            self.__sema_consumer.acquire()
            item = self.__store.dequeue()
            print(f"{item.get_name()} bought by {self.__name}")
            print(f"Store size : {self.__store.size()}")
            self.__sema_producer.release()


def main():
    store = LinkedListQueue()
    max_store = 5
    sema_producer = threading.Semaphore(max_store)
    sema_consumer = threading.Semaphore(0)

    p1 = Producer(store, max_store, "P1", sema_producer, sema_consumer)
    p2 = Producer(store, max_store, "P2", sema_producer, sema_consumer)
    p3 = Producer(store, max_store, "P3", sema_producer, sema_consumer)
    p4 = Producer(store, max_store, "P4", sema_producer, sema_consumer)
    p5 = Producer(store, max_store, "P5", sema_producer, sema_consumer)

    c1 = Consumer(store, max_store, "C1", sema_producer, sema_consumer)
    c2 = Consumer(store, max_store, "C2", sema_producer, sema_consumer)
    c3 = Consumer(store, max_store, "C3", sema_producer, sema_consumer)
    c4 = Consumer(store, max_store, "C4", sema_producer, sema_consumer)
    c5 = Consumer(store, max_store, "C5", sema_producer, sema_consumer)

    p1.start()
    c1.start()
    p2.start()
    c2.start()
    p3.start()
    c3.start()
    p4.start()
    c4.start()
    p5.start()
    c5.start()


main()
