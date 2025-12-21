package com.example.designPatterns.creationalDesignPatterns.builder.way1;

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

    private Student(StudentHelper helper) {
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

    public static Student build(StudentHelper helper) {
        helper.validate();
        return new Student(helper);
    }


}
