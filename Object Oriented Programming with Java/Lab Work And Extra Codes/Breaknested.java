
public class Breaknested {


	public static void main(String[] args) {

		int i,j; 
		for(i=0;i<3;i++)
		{  for(j=10;j<15;j++)
		   {
             System.out.print(j+" ");			
		     if(j==13)
		     {break;}
		   }
		   System.out.print(i+" ");
		}
	}

}
