package com.student;

public class College {
	public static void main(String[]s) {
		
		Student v1 = new Student(138,"Vedant","Computer",4,9.8,"O");
		System.out.println(v1);
		
		Student v2 = new StudentBuilder().setStudent_id(138).setStudent_name("Vedant").setStudent_semester(4).getStudent();
		System.out.println(v2);
	}
}
