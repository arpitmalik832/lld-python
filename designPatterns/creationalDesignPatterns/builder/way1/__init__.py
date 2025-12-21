package com.example.designPatterns.creationalDesignPatterns.builder.way1;

public class Main {
    public static void main(String[] args) {
        StudentHelper helper = new StudentHelper();
        helper.id("1234")
                .name("ABC")
                .marks(90)
                .roll("1234")
                .mobile("1234567890")
                .email("abc@email.com")
                .intermediateYear(2022)
                .intermediateRoll("FE13")
                .intermediateSchool("APS")
                .intermediateMarks(50);

        Student s = Student.build(helper);

        System.out.println(s);
    }
}
