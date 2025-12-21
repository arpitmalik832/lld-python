package com.example.designPatterns.creationalDesignPatterns.builder.way1;

import com.example.designPatterns.creationalDesignPatterns.builder.exceptions.*;
import com.example.designPatterns.creationalDesignPatterns.builder.validators.EmailValidator;

public class StudentHelper {
    public String id;
    public String name;
    public int marks;
    public String roll;
    public String mobile;
    public String email;
    public int intermediateYear;
    public int intermediateMarks;
    public String intermediateRoll;
    public String intermediateSchool;

    public StudentHelper() {

    }

    // setter methods
    public StudentHelper id(String id) {
        this.id = id;
        return this;
    }

    public StudentHelper name(String name) {
        this.name = name;
        return this;
    }

    public StudentHelper marks(int marks) {
        this.marks = marks;
        return this;
    }

    public StudentHelper roll(String roll) {
        this.roll = roll;
        return this;
    }

    public StudentHelper mobile(String mobile) {
        this.mobile = mobile;
        return this;
    }

    public StudentHelper email(String email) {
        this.email = email;
        return this;
    }

    public StudentHelper intermediateYear(int intermediateYear) {
        this.intermediateYear = intermediateYear;
        return this;
    }

    public StudentHelper intermediateMarks(int intermediateMarks) {
        this.intermediateMarks = intermediateMarks;
        return this;
    }

    public StudentHelper intermediateRoll(String intermediateRoll) {
        this.intermediateRoll = intermediateRoll;
        return this;
    }

    public StudentHelper intermediateSchool(String intermediateSchool) {
        this.intermediateSchool = intermediateSchool;
        return this;
    }

    public void validate() {
        validateName();
        validateMobile();
        validateEmail();
        validateIntermediateYear();
        validateIntermediateMarks();
    }

    public void validateName() {
        if (name == null || name.isEmpty()) {
            throw new InvalidNameException("Name cannot be empty");
        }

    }

    public void validateMobile() {
        if (mobile == null || mobile.isEmpty()) {
            throw new InvalidMobileException("Mobile cannot be empty");
        }
        if (mobile.length() != 10) {
            throw new InvalidMobileException("Mobile number must be of 10 digits");
        }
    }

    public void validateEmail() {
        if (email == null || email.isEmpty()) {
            throw new InvalidEmailException("Email cannot be empty");
        }
        if (!EmailValidator.isValid(email)) {
            throw new InvalidEmailException("Invalid email format");
        }
    }

    public void validateIntermediateYear() {
        if (intermediateYear > 2022) {
            throw new InvalidIntermediateYearException("Only intermediate holders upto 2022 are allowed");
        }
    }

    public void validateIntermediateMarks() {
        if (intermediateMarks < 60) {
            throw new InvalidIntermediateMarksException("Intermediate marks cannot be less than 60");
        }
    }
}
