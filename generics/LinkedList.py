from typing import TypeVar, Generic, Optional

T = TypeVar("T")


class Node(Generic[T]):
    def __init__(self, data: T):
        self.data: T = data
        self.next: Optional[Node[T]] = None


class LinkedList(Generic[T]):
    def __init__(self):
        self.head = Node(0)
        self.tail = self.head

    def append(self, data: T):
        node = Node(data)
        self.tail.next = node
        self.tail = node

    def print_list(self):
        current_node = self.head.next
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")


# Example usage:

# Create a linked list of integers
ll_int = LinkedList[int]()
ll_int.append(1)
ll_int.append(2)
ll_int.append(3)
ll_int.print_list()  # Output: 1 -> 2 -> 3 -> None

# Create a linked list of strings
ll_str = LinkedList[str]()
ll_str.append("a")
ll_str.append("b")
ll_str.append("c")
ll_str.print_list()  # Output: a -> b -> c -> None
