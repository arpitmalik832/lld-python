package com.example.designPatterns.creationalDesignPatterns.factory.abstractfactory.uiComponents;

public class IOSInput implements Input {
    @Override
    public void render() {
        System.out.println("Rendering IOS Input");
    }

    @Override
    public void onChange() {
        System.out.println("IOS Input Changed");
    }
}
