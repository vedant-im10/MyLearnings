
public class CompoundassignOp {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		//Simple assigns
		  byte bt = 24;
		  System.out.println("bt: " + bt);
		  
		  //Increments then assigns
		  bt += 10;
		  System.out.println("bt: " + bt);
		  
		  //Decrements then assigns
		  bt -= 2;
		  System.out.println("bt: " + bt);
		  
		  //Multiplies then assigns
		  bt *= 2;
		  System.out.println("bt: " + bt);
		  
		  //Divides then assigns
		  bt /= 2;
		  System.out.println("bt: " + bt);
		  
		  //Modulus then assigns
		  bt %= 7;
		  System.out.println("bt: " + bt);
		  
		  //Binary Left Shift  and assigns
		  bt <<= 3;
		  System.out.println("bt: " + bt);

		  //Binary Right Shift and assigns
		  bt >>= 4;
		  System.out.println("bt: " + bt);
		  
		  //Shift right zero fill and assigns
		  bt >>>= 1;
		  System.out.println("bt: " + bt);
		  
		  //Binary AND assigns
		  bt &= 4;
		  System.out.println("bt: " + bt);
		  
		  //Binary exclusive OR and assigns
		  bt ^= 4;
		  System.out.println("bt: " + bt);
		  
		  //Binary inclusive OR and assigns
		  bt |= 4;
		  System.out.println("bt: " + bt);
	}

}
