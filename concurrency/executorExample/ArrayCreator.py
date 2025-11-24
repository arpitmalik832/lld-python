from concurrent.futures import as_completed
from concurrent.futures.thread import ThreadPoolExecutor


def array_creator(n):
    return [i for i in range(1, n + 1)]


def main():
    with ThreadPoolExecutor(max_workers=1) as es:
        al_f = es.submit(array_creator, 100)
        al = as_completed([al_f])
        for a in al:
            print(a.result())

        es.shutdown()


main()
