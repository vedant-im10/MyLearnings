package singleton_19BCP138_Vedant;

public class Singleton_Vedant_138 {

	private static Singleton_Vedant_138 Vedant_138_SoleInstance = new Singleton_Vedant_138();
	
	private Singleton_Vedant_138()
	{
		System.out.println("Object has been Created successfully !!!");
	}
	
	private String studentsName;
	
	public void setStudentName(String studentName) 
	{
		this.studentsName = studentName;
	}
	
	public String getStudentName() 
	{
		return "Student Name : " + studentsName;
	}
	
	public static Singleton_Vedant_138 getInstance()
	{
		return Vedant_138_SoleInstance;
	}

}
