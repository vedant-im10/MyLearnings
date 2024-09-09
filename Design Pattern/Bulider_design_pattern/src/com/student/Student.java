package com.student;

public class Student {
	
	private int student_id;
	private String student_name;
	private String student_dept;
	private int student_semester;
	private double student_CGPA;
	private String student_grade;
	
	public Student(int student_id, String student_name, String student_dept, int student_semester, double student_CGPA, String student_grade) {
		
		super();
		this.student_id = student_id;
		this.student_name = student_name;
		this.student_dept = student_dept;
		this.student_semester = student_semester;
		this.student_CGPA = student_CGPA;
		this.student_grade = student_grade;
	}
	
	public String toString() {
		return "Student[Student Id="+student_id+",Student Name="+student_name+",Student Department="+student_dept+",Student Semester="+student_semester+",Student CGPA="+student_CGPA+",Student Grade="+student_grade+"]";
		
	}
}
