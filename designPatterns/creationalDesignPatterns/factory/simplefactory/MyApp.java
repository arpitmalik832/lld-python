package com.example.designPatterns.creationalDesignPatterns.factory.simplefactory;

import com.example.designPatterns.creationalDesignPatterns.factory.simplefactory.flutter.Flutter;
import com.example.designPatterns.creationalDesignPatterns.factory.simplefactory.flutterFactory.FlutterFactory;
import com.example.designPatterns.creationalDesignPatterns.factory.simplefactory.flutterFactory.FlutterType;
import com.example.designPatterns.creationalDesignPatterns.factory.simplefactory.uiComponents.Button;
import com.example.designPatterns.creationalDesignPatterns.factory.simplefactory.uiComponents.Input;

public class MyApp {
    public static void main(String[] args) {
        Flutter flutter = FlutterFactory.getFlutter(FlutterType.ANDROID);
        flutter.render();
        Button btn = flutter.createButton();
        btn.render();
        btn.onClick();
        Input ip = flutter.createInput();
        ip.render();
        ip.onChange();
    }
}
