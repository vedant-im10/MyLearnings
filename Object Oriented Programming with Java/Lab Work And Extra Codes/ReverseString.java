import java.util.Scanner;
public class ReverseString {

	
	public static void main(String[] args) {
		
		int strlen,i,j;
		char temp;
		
		// take the string input from user
		Scanner scan = new Scanner(System.in);
        System.out.print("Enter any String: ");
        String str = scan.nextLine();
        scan.close();		
        strlen = str.length();
        j = strlen-1;
        
        
        // convert string to character array
        char[] ch = str.toCharArray();
        System.out.println(ch);
        
        
          for(i=0;i<strlen/2;i++)
              {temp = ch[i];
               ch[i] = ch[j];
               ch[j] = temp;
               j--;               
              }  
          String rstr = new String(ch);
          System.out.println("Reverse String : " + rstr);
        
     }

}
