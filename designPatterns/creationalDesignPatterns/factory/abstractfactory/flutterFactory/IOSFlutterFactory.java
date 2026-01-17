package com.example.designPatterns.creationalDesignPatterns.factory.abstractfactory.flutterFactory;

import com.example.designPatterns.creationalDesignPatterns.factory.abstractfactory.uiComponents.Button;
import com.example.designPatterns.creationalDesignPatterns.factory.abstractfactory.uiComponents.IOSButton;
import com.example.designPatterns.creationalDesignPatterns.factory.abstractfactory.uiComponents.IOSInput;
import com.example.designPatterns.creationalDesignPatterns.factory.abstractfactory.uiComponents.Input;

public class IOSFlutterFactory implements FlutterFactory {
    @Override
    public Button createButton() {
        return new IOSButton();
    }

    @Override
    public Input createInput() {
        return new IOSInput();
    }
}
