package com.example.designPatterns.creationalDesignPatterns.factory.practicalfactory.flutter;

import com.example.designPatterns.creationalDesignPatterns.factory.practicalfactory.uiComponents.Button;
import com.example.designPatterns.creationalDesignPatterns.factory.practicalfactory.uiComponents.IOSButton;
import com.example.designPatterns.creationalDesignPatterns.factory.practicalfactory.uiComponents.IOSInput;
import com.example.designPatterns.creationalDesignPatterns.factory.practicalfactory.uiComponents.Input;

public class IOSFlutter implements Flutter {
    @Override
    public void setTheme() {
        System.out.println("Setting IOS Theme");
    }

    @Override
    public void setRefreshRate() {
        System.out.println("Setting IOS Refresh Rate");
    }

    @Override
    public void render() {
        System.out.println("Rendering IOS Flutter");
    }

    @Override
    public Button createButton() {
        return new IOSButton();
    }

    @Override
    public Input createInput() {
        return new IOSInput();
    }
}
