package com.example.designPatterns.creationalDesignPatterns.factory.abstractfactory;

import com.example.designPatterns.creationalDesignPatterns.factory.abstractfactory.flutter.Flutter;
import com.example.designPatterns.creationalDesignPatterns.factory.abstractfactory.flutter.IOSFlutter;
import com.example.designPatterns.creationalDesignPatterns.factory.abstractfactory.flutterFactory.FlutterFactory;
import com.example.designPatterns.creationalDesignPatterns.factory.abstractfactory.uiComponents.Button;
import com.example.designPatterns.creationalDesignPatterns.factory.abstractfactory.uiComponents.Input;

public class MyApp {
    public static void main(String[] args) {
        Flutter flutter = new IOSFlutter();

        flutter.setTheme();
        flutter.setRefreshRate();
        flutter.render();
        FlutterFactory factory = flutter.createFactory();
        Button btn = factory.createButton();
        btn.render();
        btn.onClick();
        Input ip = factory.createInput();
        ip.render();
        ip.onChange();
    }
}
