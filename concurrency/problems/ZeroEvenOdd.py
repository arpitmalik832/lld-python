from threading import Thread, Semaphore


class IntConsumer:
    def accept(self, n: int):
        print(n, end=" ")


class ZeroOddEven:
    def __init__(self, n, printNumber: IntConsumer):
        self.n = n
        self.semaZ = Semaphore(1)
        self.semaE = Semaphore(0)
        self.semaO = Semaphore(0)
        self.printNumber = printNumber

    def zero(self):
        for i in range(1, self.n + 1):
            self.semaZ.acquire()
            self.printNumber.accept(0)
            if i % 2 == 1:
                self.semaO.release()
            else:
                self.semaE.release()

    def even(self):
        for i in range(2, self.n + 1, 2):
            self.semaE.acquire()
            self.printNumber.accept(i)
            self.semaZ.release()

    def odd(self):
        for i in range(1, self.n + 1, 2):
            self.semaO.acquire()
            self.printNumber.accept(i)
            self.semaZ.release()


def main():
    printNumber = IntConsumer()
    zeroOddEven = ZeroOddEven(10, printNumber)

    printZero = Thread(target=zeroOddEven.zero)
    printZero.start()

    printOdd = Thread(target=zeroOddEven.odd)
    printOdd.start()

    printEven = Thread(target=zeroOddEven.even)
    printEven.start()


main()
