package vedant_19bcp138;

import java.util.*;

public class Vedant_19bcp138_Student implements Cloneable {

	private List<String> studentDetails;
	
	public Vedant_19bcp138_Student()
	{
		this.studentDetails = new ArrayList<String>();
	}
	public Vedant_19bcp138_Student(List<String> list)
	{
		this.studentDetails = list;
	}
	public void insertData()
	{
		studentDetails.add("College Name : PDEU");
		studentDetails.add("Branch : Computer Engineering");
		studentDetails.add("Name : Vedant Patel");
		studentDetails.add("Roll No. : 19BCP138");
		studentDetails.add("CGPA : 9.6");
		studentDetails.add("SGPA : 9.5");
		studentDetails.add("Division : 2");
		studentDetails.add("Total Credits : 120");
	}
	public void modify(String name, String rollNo, float sgpa, float cgpa, float div)
	{
		studentDetails.set(0, "Name : "+name);
		studentDetails.set(1, "Roll No. : "+rollNo);
		studentDetails.set(2, "SGPA : "+sgpa);
		studentDetails.set(3, "CGPA : "+cgpa);
		studentDetails.set(4, "Division : "+div);
	}
	public List<String> getStudentDetails()
	{
		return this.studentDetails;
	}
	public Object clone() throws CloneNotSupportedException
	{
		List<String> tempList = new ArrayList<String>();
		
		for(String s : this.studentDetails)
		{
			tempList.add(s);
		}
		return new Vedant_19bcp138_Student(tempList);
	}
}
