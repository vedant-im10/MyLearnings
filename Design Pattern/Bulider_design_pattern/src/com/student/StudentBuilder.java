package com.student;

public class StudentBuilder {
	
	private int student_id;
	private String student_name;
	private String student_dept;
	private int student_semester;
	private double student_CGPA;
	private String student_grade;
	
	public StudentBuilder setStudent_id(int student_id) {
		this.student_id = student_id;
		return this;
	}
	public StudentBuilder setStudent_name(String student_name) {
		this.student_name = student_name;
		return this;
	}
	public StudentBuilder setStudent_dept(String student_dept) {
		this.student_dept = student_dept;
		return this;
	}
	public StudentBuilder setStudent_semester(int student_semester) {
		this.student_semester = student_semester;
		return this;
	}
	public StudentBuilder setStudent_CGPA(double student_CGPA) {
		this.student_CGPA = student_CGPA;
		return this;
	}
	public StudentBuilder setStudent_grade(String student_grade) {
		this.student_grade = student_grade;
		return this;
	}
	public Student getStudent() {
		return new Student(student_id, student_name, student_dept, student_semester, student_CGPA, student_grade);
	}
}
