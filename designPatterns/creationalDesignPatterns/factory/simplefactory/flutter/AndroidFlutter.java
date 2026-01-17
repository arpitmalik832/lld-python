package com.example.designPatterns.creationalDesignPatterns.factory.simplefactory.flutter;

import com.example.designPatterns.creationalDesignPatterns.factory.simplefactory.uiComponents.AndroidButton;
import com.example.designPatterns.creationalDesignPatterns.factory.simplefactory.uiComponents.AndroidInput;
import com.example.designPatterns.creationalDesignPatterns.factory.simplefactory.uiComponents.Button;
import com.example.designPatterns.creationalDesignPatterns.factory.simplefactory.uiComponents.Input;

public class AndroidFlutter implements Flutter {
    @Override
    public void setTheme() {
        System.out.println("Setting Android Theme");
    }

    @Override
    public void setRefreshRate() {
        System.out.println("Setting Android Refresh Rate");
    }

    @Override
    public void render() {
        System.out.println("Rendering Android Flutter");
    }

    @Override
    public Button createButton() {
        return new AndroidButton();
    }

    @Override
    public Input createInput() {
        return new AndroidInput();
    }
}
