package com.example.designPatterns.creationalDesignPatterns.factory.abstractfactory.flutterFactory;

import com.example.designPatterns.creationalDesignPatterns.factory.abstractfactory.uiComponents.Button;
import com.example.designPatterns.creationalDesignPatterns.factory.abstractfactory.uiComponents.Input;

public interface FlutterFactory {
    Button createButton();

    Input createInput();
}
