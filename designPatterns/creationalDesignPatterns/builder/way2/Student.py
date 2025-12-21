package com.example.designPatterns.creationalDesignPatterns.builder.way2;

import com.example.designPatterns.creationalDesignPatterns.builder.exceptions.*;
import com.example.designPatterns.creationalDesignPatterns.builder.validators.EmailValidator;

/**
 * Better way using inner class.
 */
public class Student {
    private String id;
    private String name;
    private int marks;
    private String roll;
    private String mobile;
    private String email;
    private int intermediateYear;
    private int intermediateMarks;
    private String intermediateRoll;
    private String intermediateSchool;

    private Student(String id, String name, int marks, String roll, String mobile, String email, int intermediateYear,
                    int intermediateMarks, String intermediateRoll, String intermediateSchool) {
        this.id = id;
        this.name = name;
        this.marks = marks;
        this.roll = roll;
        this.mobile = mobile;
        this.email = email;
        this.intermediateYear = intermediateYear;
        this.intermediateMarks = intermediateMarks;
        this.intermediateRoll = intermediateRoll;
        this.intermediateSchool = intermediateSchool;
    }

    private Student(Student.Builder helper) {
        this(helper.id,
                helper.name,
                helper.marks,
                helper.roll,
                helper.mobile,
                helper.email,
                helper.intermediateYear,
                helper.intermediateMarks,
                helper.intermediateRoll,
                helper.intermediateSchool);
    }

    static class Builder {
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

        public Builder() {

        }

        // setter methods
        public Student.Builder id(String id) {
            this.id = id;
            return this;
        }

        public Student.Builder name(String name) {
            this.name = name;
            return this;
        }

        public Student.Builder marks(int marks) {
            this.marks = marks;
            return this;
        }

        public Student.Builder roll(String roll) {
            this.roll = roll;
            return this;
        }

        public Student.Builder mobile(String mobile) {
            this.mobile = mobile;
            return this;
        }

        public Student.Builder email(String email) {
            this.email = email;
            return this;
        }

        public Student.Builder intermediateYear(int intermediateYear) {
            this.intermediateYear = intermediateYear;
            return this;
        }

        public Student.Builder intermediateMarks(int intermediateMarks) {
            this.intermediateMarks = intermediateMarks;
            return this;
        }

        public Student.Builder intermediateRoll(String intermediateRoll) {
            this.intermediateRoll = intermediateRoll;
            return this;
        }

        public Student.Builder intermediateSchool(String intermediateSchool) {
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

        public Student build() {
            this.validate();
            return new Student(this);
        }
    }
}
