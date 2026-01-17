package com.example.designPatterns.creationalDesignPatterns.factory.practicalfactory.flutter;

import com.example.designPatterns.creationalDesignPatterns.factory.practicalfactory.uiComponents.Button;
import com.example.designPatterns.creationalDesignPatterns.factory.practicalfactory.uiComponents.Input;

public interface Flutter {
    void setTheme();

    void setRefreshRate();

    void render();

    Button createButton();

    Input createInput();
}
