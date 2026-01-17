package com.example.designPatterns.creationalDesignPatterns.factory.practicalfactory;

import com.example.designPatterns.creationalDesignPatterns.factory.practicalfactory.flutter.Flutter;
import com.example.designPatterns.creationalDesignPatterns.factory.practicalfactory.flutter.IOSFlutter;
import com.example.designPatterns.creationalDesignPatterns.factory.practicalfactory.uiComponents.Button;
import com.example.designPatterns.creationalDesignPatterns.factory.practicalfactory.uiComponents.Input;

public class MyApp {
    public static void main(String[] args) {
        Flutter flutter = new IOSFlutter();
        flutter.render();
        Button btn = flutter.createButton();
        btn.render();
        btn.onClick();
        Input ip = flutter.createInput();
        ip.render();
        ip.onChange();
    }
}
