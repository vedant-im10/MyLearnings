package vedant_19bcp138;

import java.util.*;

public class Vedant_19bcp138_StudentMain {

	public static void main(String[] args) throws CloneNotSupportedException {
		Scanner sc = new Scanner(System.in);

		Vedant_19bcp138_Student student1 = new Vedant_19bcp138_Student();
		student1.insertData();
		
		Vedant_19bcp138_Student student2 = (Vedant_19bcp138_Student) student1.clone();
		
		String name, rollNo;
		float sgpa, cgpa, div;
		
		System.out.print("Enter the Name : ");
		name = sc.nextLine();
		System.out.print("Enter the Roll No. : ");
		rollNo = sc.next();
		System.out.print("Enter the SGPA : ");
		sgpa = sc.nextFloat();
		System.out.print("Enter the CGPA : ");
		cgpa = sc.nextFloat();
		System.out.print("Enter the Division : ");
		div = sc.nextFloat();
		
		student2.modify(name, rollNo, sgpa, cgpa, div);
		
		System.out.println(student1.getStudentDetails());
		
		List<String> list = student2.getStudentDetails();
		System.out.println(list);
		System.out.println(student1.getStudentDetails());
		
		sc.close();
	}
}
