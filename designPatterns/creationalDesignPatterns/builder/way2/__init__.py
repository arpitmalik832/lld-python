package com.example.designPatterns.creationalDesignPatterns.builder.way2;

public class Main {
    public static void main(String[] args) {
        Student s = new Student.Builder()
                .id("1234")
                .name("ABC")
                .marks(90)
                .roll("1234")
                .mobile("1234567890")
                .email("abc@email.com")
                .intermediateYear(2022)
                .intermediateRoll("FE13")
                .intermediateSchool("APS")
                .intermediateMarks(60)
                .build();

        System.out.println(s);
    }
}
