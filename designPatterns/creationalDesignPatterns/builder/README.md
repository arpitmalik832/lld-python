# Builder Design Pattern

## Use Case

* Let's say we have a class with a lot of attributes.
* We can create objects using parameterized constructor or using setters.
* But that is prone to multiple errors.
    1. If we use the parameterized constructor, the parameters might get swapped while calling the constructor.
    2. If we us setters, it will lead to a lot of boilerplate code.
    3. And the object will be created before even doing the validations.
    4. Ideally, the object should be created after doing the required validations.
    5. Here, we'll require the builder design pattern.

## Steps for the Builder Design Pattern

1. For that, we'll require a helper class to create an object and perform validations before even creating the actual
   object.