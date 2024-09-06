public class StringJava {
	public static void main(String[] args) {
		 String str = "Learnjava"; 
		 System.out.println("str = " + str);
		 char ch[]={'L','e','a','r','n'}; 
		 System.out.println("ch = " + ch[0]);
		 String str22 = new String(ch); 
		 System.out.println("str22 = " + str22);
		 System.out.println(str.charAt(5));
		 System.out.println(str.length());
		 char[] array= str22.toCharArray();
		 System.out.println(array[0]);	 
	}
}
