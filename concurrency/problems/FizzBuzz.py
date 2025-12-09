from threading import Semaphore, Thread


class FizzBuzz:
    def __init__(self, n: int):
        self.n = n
        self.semaFizz = Semaphore(0)
        self.semaBuzz = Semaphore(0)
        self.semaFizzBuzz = Semaphore(0)
        self.semaNumber = Semaphore(1)

    def release_expected(self, i):
        next = i + 1
        # Check the NEXT number
        if next % 3 == 0 and next % 5 == 0:
            self.semaFizzBuzz.release()
        elif next % 3 == 0:
            self.semaFizz.release()
        elif next % 5 == 0:
            self.semaBuzz.release()
        else:
            self.semaNumber.release()

    def print_fizz(self):
        for i in range(1, self.n + 1):
            if i % 3 == 0 and i % 5 != 0:
                self.semaFizz.acquire()
                print("fizz", end=" ")
                self.release_expected(i)

    def print_buzz(self):
        for i in range(1, self.n + 1):
            if i % 3 != 0 and i % 5 == 0:
                self.semaBuzz.acquire()
                print("buzz", end=" ")
                self.release_expected(i)

    def print_fizz_buzz(self):
        for i in range(1, self.n + 1):
            if i % 3 == 0 and i % 5 == 0:
                self.semaFizzBuzz.acquire()
                print("fizzbuzz", end=" ")
                self.release_expected(i)

    def print_number(self):
        for i in range(1, self.n + 1):
            if i % 3 != 0 and i % 5 != 0:
                self.semaNumber.acquire()
                print(i, end=" ")
                self.release_expected(i)


def main():
    fizzBuzz = FizzBuzz(30)

    tFizz = Thread(target=fizzBuzz.print_fizz)
    tFizz.start()

    tBuzz = Thread(target=fizzBuzz.print_buzz)
    tBuzz.start()

    tFizzBuzz = Thread(target=fizzBuzz.print_fizz_buzz)
    tFizzBuzz.start()

    tNumber = Thread(target=fizzBuzz.print_number)
    tNumber.start()

    tFizz.join()
    tBuzz.join()
    tFizzBuzz.join()
    tNumber.join()


main()
