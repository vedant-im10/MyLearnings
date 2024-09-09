package singleton_19BCP138_Vedant;

public class StudentClass_Vedant_138 {

	public static void main(String[] args) {
			
			Singleton_Vedant_138 v1 = Singleton_Vedant_138.getInstance();
			Singleton_Vedant_138 v2 = Singleton_Vedant_138.getInstance();
				
			v1.setStudentName("Vedant");
			v2.setStudentName("Vedant Patel");
				
			System.out.println(v1.getStudentName());
			System.out.println(v2.getStudentName());
				
			printDetails("Vedant-1", v1);
			printDetails("Vedant-2", v2);

		}
		static void printDetails(String name, Singleton_Vedant_138 object)
		{
			System.out.println(String.format("Object : %s, Hashcode : %d", name, object.hashCode()));
		}
			
}