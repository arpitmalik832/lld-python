package com.example.designPatterns.creationalDesignPatterns.factory.abstractfactory.flutter;

import com.example.designPatterns.creationalDesignPatterns.factory.abstractfactory.flutterFactory.FlutterFactory;

public interface Flutter {
    void setTheme();

    void setRefreshRate();

    void render();

    FlutterFactory createFactory();
}
