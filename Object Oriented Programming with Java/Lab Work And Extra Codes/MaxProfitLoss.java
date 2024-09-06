import java.util.Scanner;
public class MaxProfitLoss {
	public static void main(String[] args) {
		// take the string input from user
		int n,maxprof = 0, maxlos=0;
		Scanner s = new Scanner(System.in);
		System.out.print("Enter no. of elements you want in array:");
		n = s.nextInt();
        int a[] = new int[n];
        System.out.println("Enter all the elements:");		
        
	for(int i = 0; i < n; i++)
        {
            a[i] = s.nextInt();
        }
        s.close();  
        
	for(int i = 0; i < n; i++)
        {
            System.out.print(a[i] + " ");
        }
        
        for(int i=0;i<n-1;i++)
        {  for(int j=i+1;j<n;j++)
           {   if(maxprof < a[j]-a[i])
               {    maxprof = a[j]-a[i];}                  
               if(maxlos > a[j]-a[i]) 
               {    maxlos = a[j]-a[i];}    
           }
        }
        
        System.out.println("\n" + "maximum profit = " + maxprof);
        System.out.println("maximum loss = " + maxlos);
	}
}
