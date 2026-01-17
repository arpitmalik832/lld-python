package com.example.designPatterns.creationalDesignPatterns.factory.practicalfactory.flutter;

import com.example.designPatterns.creationalDesignPatterns.factory.practicalfactory.uiComponents.AndroidButton;
import com.example.designPatterns.creationalDesignPatterns.factory.practicalfactory.uiComponents.AndroidInput;
import com.example.designPatterns.creationalDesignPatterns.factory.practicalfactory.uiComponents.Button;
import com.example.designPatterns.creationalDesignPatterns.factory.practicalfactory.uiComponents.Input;

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
