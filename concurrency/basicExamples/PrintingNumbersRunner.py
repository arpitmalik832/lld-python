import threading
from threading import Thread


class PrintingNumbersRunner(Thread):
    def __init__(self, number_to_print):
        super().__init__()
        self.__number_to_print = number_to_print

    def run(self):
        print(
            str(self.__number_to_print)
            + " using Thread: "
            + threading.current_thread().name
        )


def main():
    for i in range(1, 101):
        thread = PrintingNumbersRunner(i)
        thread.start()


main()
