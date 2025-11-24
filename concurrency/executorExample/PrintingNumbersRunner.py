import threading
from concurrent.futures.thread import ThreadPoolExecutor


def printing_numbers(nos_to_print):
    print(str(nos_to_print) + " using Thread: " + threading.current_thread().name)


def main():
    es = ThreadPoolExecutor(max_workers=10)
    for i in range(1, 101):
        es.submit(printing_numbers, i)
    es.shutdown()


main()
