import threading


def run_print():
    print("Hello, World! using thread: " + str(threading.current_thread().name) + "\n")


thread = threading.Thread(target=run_print)
thread.start()
run_print()
