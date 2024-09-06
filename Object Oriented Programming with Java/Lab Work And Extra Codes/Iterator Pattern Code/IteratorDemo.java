

interface Aggregate {
	    Iterator getIterator();
  }
  

interface Iterator {
	public boolean hasNext();
	   public Object next();
}

  

class ConcreteAgg implements Aggregate{
	public String names[] = {"Rohit" , "Jignesh" ,"Aashvi" , "Lipi"};

	   
	    public Iterator getIterator() {
	      return new NameIterator();
	   }

	  class NameIterator implements Iterator {

	      int index;

	      
	      public boolean hasNext() {
	      
	         if(index < names.length){
	            return true;
	         }
	         return false;
	      }

	      
	      public Object next() {
	      
	         if(this.hasNext()){
	            return names[index++];
	         }
	         return null;
	      }		
	   }

}

public class IteratorDemo {

	public static void main(String[] args) {


		
		ConcreteAgg ca = new ConcreteAgg();

	      for(Iterator iter = ca.getIterator(); iter.hasNext();){
	         String name = (String)iter.next();
	         System.out.println("Name : " + name);}

	}

}
