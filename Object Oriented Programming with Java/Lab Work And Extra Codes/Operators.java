public class Operators {
	/**
	 * @param args
	 */
	public static void main(String[] args) {
		int j=5,k,l,m, n = 4, o;
		
		//Increment, Decrement (unary arithmetic operators)
		k = j+1;
		System.out.println("j+1 = " + k);
		l = ++j + 1;
		System.out.println("++j + 1 = " + l);
        System.out.println("j = " + j);
        j = 5;
        m = j++ + 1;
        System.out.println("j++ + 1 = " + m);
        System.out.println("j = " + j);
        o = ++n + n++ + n++ ;
        System.out.println("o = " + o);
        //System.out.println("n = " + n);
        
        //Relational Operator
        boolean b;
        b = j>n;
        System.out.println("b = " + b);
        
        //Arithmetic Operators
        j *=n; // j = j*n
        System.out.println("j = " + j);
        j /=n; /* j = j/n  */
        System.out.println("j = " + j);   
	}
}
