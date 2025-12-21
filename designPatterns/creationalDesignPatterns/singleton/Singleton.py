package com.example.designPatterns.creationalDesignPatterns.singleton;

/**
 * Singleton - We can have one and only one object of the class at the runtime.
 * Steps -
 * 1. Create a private constructor.
 * 2. Create a public method to create the object.
 * 3. To access that method, we'll need an object -> deadlock. So, make this method static.
 * 4. We can't create an object at every call of the method. So, we'll need one private static reference variable
 * to store the instance.
 */
public class Singleton {
    private static Singleton instance;

    private Singleton() {
    }

    public static Singleton getInstance() {
        if (instance == null) {
            instance = new Singleton();
        }

        return instance;
    }

    public static void main(String[] args) {
        Singleton s1 = Singleton.getInstance();
        Singleton s2 = Singleton.getInstance();
        Singleton s3 = Singleton.getInstance();
        Singleton s4 = Singleton.getInstance();
    }
}
