package com.example.designPatterns.creationalDesignPatterns.factory.abstractfactory.uiComponents;

public class IOSButton implements Button {

    @Override
    public void render() {
        System.out.println("Rendering IOS Button");
    }

    @Override
    public void onClick() {
        System.out.println("IOS Button Clicked");
    }
}
