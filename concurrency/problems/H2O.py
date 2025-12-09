from threading import Semaphore, Thread


class PrintConsumer:
    def accept(self, i):
        print(i, end=" ")


class H2O:
    # Semaphore semaH, semaO;

    def __init__(self):
        self.semaH = Semaphore(2)
        self.semaO = Semaphore(0)

    def hydrogen_releaser(self):
        self.semaH.acquire()
        print("H")
        if self.semaH.availablePermits() == 0:
            self.semaO.release()

    def oxygen_releaser(self):
        self.semaO.acquire()
        print("O")
        self.semaH.release(2)


def main():
    s = "OOHHHH"
    h2o = H2O()

    for c in s:
        if c == "H":
            thread = Thread(target=h2o.hydrogen_releaser)
            thread.start()
        elif c == "O":
            thread = Thread(target=h2o.oxygen_releaser)
            thread.start()
