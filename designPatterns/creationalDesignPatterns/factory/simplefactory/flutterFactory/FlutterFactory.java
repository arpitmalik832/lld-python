package com.example.designPatterns.creationalDesignPatterns.factory.simplefactory.flutterFactory;


import com.example.designPatterns.creationalDesignPatterns.factory.simplefactory.flutter.AndroidFlutter;
import com.example.designPatterns.creationalDesignPatterns.factory.simplefactory.flutter.Flutter;
import com.example.designPatterns.creationalDesignPatterns.factory.simplefactory.flutter.IOSFlutter;

public class FlutterFactory {
    public static Flutter getFlutter(FlutterType type) {
        switch (type) {
            case ANDROID:
                return new AndroidFlutter();
            case IOS:
                return new IOSFlutter();
            default:
                throw new IllegalArgumentException("Invalid Flutter Type");
        }
    }
}
