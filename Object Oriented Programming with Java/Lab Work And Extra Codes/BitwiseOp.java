public class BitwiseOp {
	/**
	 * @param args
	 */
	public static void main(String[] args) {
		//Variables Definition and Initialization
		  int num1 = 30, num2 = 6, num3 =0;

		  //Bitwise AND
		  System.out.println("num1 & num2 = " + (num1 & num2));
		  
		  //Bitwise OR
		  System.out.println("num1 | num2 = " + (num1 | num2) );
		  
		  //Bitwise XOR
		  System.out.println("num1 ^ num2 = " + (num1 ^ num2) );
		  
		  //Binary Complement Operator
		  System.out.println("~num1 = " + ~num1 );

		  //Binary Left Shift Operator
		  num3 = num1 <<  2;
		  System.out.println("num1 << 1 = " + num3 );

		  //Binary Right Shift Operator
		  num3 = num1 >>  2;
		  System.out.println("num1 >> 1  = " + num3 );

		  //Shift right zero fill operator
		  num3 = num1 >>> 2;
		  System.out.println("num1 >>> 1 = " + num3 );
	}
}
