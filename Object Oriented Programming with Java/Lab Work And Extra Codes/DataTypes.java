public class DataTypes {
	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// byte, short, integer , long
		int i = 50; //Declare a variable i as an integer and assign value to it
		//i = 50;
		System.out.println("i = " + i);
		long l=100; //declare a variable l of type long 
        i = (int) (i + l);
        System.out.println("i = " + i);
        byte by = 10;
        System.out.println("by = " + by);
        
        // float, double        
        float f; //Declare variable f as a float
        f = (float) 3.14; //type casting
        System.out.println("f = " + f);
        double d = 10000; //declare a variable d of type long 
        System.out.println("d = " + d);
        
        // character
        char ch='a', ch1='B'; // declare variables of type character
        i = ch;
        System.out.println("ch = " + ch);
        System.out.println("i = " + i);
        char c = (char) (ch + ch1); // type casting and type promotion
        
        //boolean
        boolean b = true; // declare a variable of type boolean
        System.out.println("b = " + b);
        System.out.println("c = " + c);
	}
}
