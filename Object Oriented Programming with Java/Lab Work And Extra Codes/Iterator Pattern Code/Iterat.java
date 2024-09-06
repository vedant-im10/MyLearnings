// Import the ArrayList class and the Iterator class
import java.util.ArrayList;
import java.util.Iterator;

public class Iterat {
	public static void main(String[] args) {
		// Make a collection
	    ArrayList<String> student = new ArrayList<String>();
	    student.add("Rohit");
	    student.add("Mahesh");
	    student.add("Rudrika");
	    student.add("Roshani");

	    // Get the iterator
	    Iterator<String> it = student.iterator();

	 // Traversing elements
		while(it.hasNext()){
			System.out.println(it.next());			
		}		
	}
}
