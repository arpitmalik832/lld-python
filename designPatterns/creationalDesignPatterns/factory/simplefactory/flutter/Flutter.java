package com.example.designPatterns.creationalDesignPatterns.factory.simplefactory.flutter;

import com.example.designPatterns.creationalDesignPatterns.factory.simplefactory.uiComponents.Button;
import com.example.designPatterns.creationalDesignPatterns.factory.simplefactory.uiComponents.Input;

public interface Flutter {
    void setTheme();

    void setRefreshRate();

    void render();

    Button createButton();

    Input createInput();
}
