from concurrent.futures import as_completed
from concurrent.futures.thread import ThreadPoolExecutor


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def tree_size_calculator(root, es):
    left_size = 0
    right_size = 0

    if root.left is not None:
        futures = [es.submit(tree_size_calculator, root.left, es)]
        left_size = [i.result() for i in as_completed(futures)][0]

    if root.right is not None:
        futures = [es.submit(tree_size_calculator, root.right, es)]
        right_size = [i.result() for i in as_completed(futures)][0]

    return left_size + right_size + 1


def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)

    es = ThreadPoolExecutor(max_workers=10)
    futures = [es.submit(tree_size_calculator, root, es)]
    size = [i.result() for i in as_completed(futures)][0]

    print(size)
    es.shutdown()


main()
