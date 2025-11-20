import multiprocessing
import os


def print_hello_world():
    print("Hello World with process ID: " + str(os.getpid()))


if __name__ == "__main__":
    process = multiprocessing.Process(target=print_hello_world)
    process.start()
    print_hello_world()
