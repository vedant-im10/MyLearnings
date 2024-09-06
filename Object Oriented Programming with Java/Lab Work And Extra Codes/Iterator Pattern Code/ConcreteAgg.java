
public class ConcreteAgg implements Aggregate{
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
