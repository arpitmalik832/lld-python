# Singleton - We can have one and only one object of the class at the runtime.
# Steps -
# 1. Create a private constructor.
# 2. Create a public method to create the object.
# 3. To access that method, we'll need an object -> deadlock. So, make this method static.
# 4. We can't create an object at every call of the method. So, we'll need one private static reference variable
# to store the instance.
# <p>
# Core Mechanisms for Breaking Singleton
# There are three primary ways to break a Singleton implementation:
# 1. Reflection: This is the most common method. Using Java's Reflection API, you can access the private constructor of the Singleton class. By calling setAccessible(true),
# you can force the constructor to be public and create a new instance bypassing the getInstance() check.
# 2. Serialization and Deserialization: If a Singleton class implements the Serializable interface, deserializing an object creates a deep copy of it.
# This means the readObject() method creates a new instance rather than returning the existing one, resulting in two distinct objects in memory.
# 3. Cloning: If the Singleton class extends a class that implements Cloneable and does not override the clone() method to prevent it, invoking clone() will create a copy
# of the existing instance, violating the single instance rule.
import threading


class ConcurrentSingleton:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
        return cls._instance


def main():
    s1 = ConcurrentSingleton()
    s2 = ConcurrentSingleton()
    s3 = ConcurrentSingleton()
    s4 = ConcurrentSingleton()


main()
