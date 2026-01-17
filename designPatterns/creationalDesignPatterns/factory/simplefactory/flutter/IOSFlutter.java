package com.example.designPatterns.creationalDesignPatterns.factory.simplefactory.flutter;

import com.example.designPatterns.creationalDesignPatterns.factory.simplefactory.uiComponents.Button;
import com.example.designPatterns.creationalDesignPatterns.factory.simplefactory.uiComponents.IOSButton;
import com.example.designPatterns.creationalDesignPatterns.factory.simplefactory.uiComponents.IOSInput;
import com.example.designPatterns.creationalDesignPatterns.factory.simplefactory.uiComponents.Input;

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
