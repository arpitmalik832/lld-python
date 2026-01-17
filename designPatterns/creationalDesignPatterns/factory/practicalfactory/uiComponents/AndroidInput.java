package com.example.designPatterns.creationalDesignPatterns.factory.practicalfactory.uiComponents;

public class AndroidInput implements Input {
    @Override
    public void render() {
        System.out.println("Rendering Android Input");
    }

    @Override
    public void onChange() {
        System.out.println("Android Input Changed");
    }
}
