package com.example.designPatterns.creationalDesignPatterns.builder.exceptions;

public class InvalidNameException extends RuntimeException {

    public InvalidNameException(String message) {
        super(message);
    }
}
