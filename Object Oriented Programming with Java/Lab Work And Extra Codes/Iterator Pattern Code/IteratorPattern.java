public class IteratorPattern {
	public static void main(String[] args) {
		ConcreteAgg ca = new ConcreteAgg();

	      for(Iterator iter = ca.getIterator(); iter.hasNext();){
	         String name = (String)iter.next();
	         System.out.println("Name : " + name);
	      } 	
	}
}
