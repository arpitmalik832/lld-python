package com.example.designPatterns.creationalDesignPatterns.factory.abstractfactory.flutter;

import com.example.designPatterns.creationalDesignPatterns.factory.abstractfactory.flutterFactory.FlutterFactory;
import com.example.designPatterns.creationalDesignPatterns.factory.abstractfactory.flutterFactory.IOSFlutterFactory;

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
    public FlutterFactory createFactory() {
        return new IOSFlutterFactory();
    }
}
