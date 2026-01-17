package com.example.designPatterns.creationalDesignPatterns.factory.abstractfactory.flutter;

import com.example.designPatterns.creationalDesignPatterns.factory.abstractfactory.flutterFactory.AndroidFlutterFactory;
import com.example.designPatterns.creationalDesignPatterns.factory.abstractfactory.flutterFactory.FlutterFactory;

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
    public FlutterFactory createFactory() {
        return new AndroidFlutterFactory();
    }
}
