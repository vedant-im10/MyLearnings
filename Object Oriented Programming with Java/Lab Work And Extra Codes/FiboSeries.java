
public class FiboSeries {

	public static void main(String[] args) {
	    int temp = 0,temp1,sum =1, iter=10;
	    
        System.out.print(temp + " ");
        System.out.print(sum + " ");
        while(iter>0)
        {    
        	 temp1 = sum;
        	 sum+=temp; 
        	 temp = temp1;
        	 System.out.print(sum + " ");                         
               
             iter--;
        }	
        	
	}

}
