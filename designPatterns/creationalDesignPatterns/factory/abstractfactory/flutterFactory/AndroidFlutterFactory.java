package com.example.designPatterns.creationalDesignPatterns.factory.abstractfactory.flutterFactory;

import com.example.designPatterns.creationalDesignPatterns.factory.abstractfactory.uiComponents.AndroidButton;
import com.example.designPatterns.creationalDesignPatterns.factory.abstractfactory.uiComponents.AndroidInput;
import com.example.designPatterns.creationalDesignPatterns.factory.abstractfactory.uiComponents.Button;
import com.example.designPatterns.creationalDesignPatterns.factory.abstractfactory.uiComponents.Input;

public class AndroidFlutterFactory implements FlutterFactory {
    @Override
    public Button createButton() {
        return new AndroidButton();
    }

    @Override
    public Input createInput() {
        return new AndroidInput();
    }
}
