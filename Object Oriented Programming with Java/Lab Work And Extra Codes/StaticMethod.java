
public class StaticMethod {

    int rollno;  
    String name;  
    static String university = "PDPU";  
    //static method to change the value of static variable  
    static void change(){  
    university = "DA-IICT";  
    }  
    //constructor to initialize the variable  
    StaticMethod(int r, String n){  
    rollno = r;  
    name = n;  
    }  
    //method to display values  
    void display(){System.out.println(rollno+" "+name+" "+university);}  
	public static void main(String[] args) {
		StaticMethod.change();//calling change method  
	    //creating objects  
		StaticMethod s1 = new StaticMethod(111,"Priyanshi");  
		StaticMethod s2 = new StaticMethod(222,"Riya");  
		StaticMethod s3 = new StaticMethod(333,"Devansh");  
	    //calling display method  
	    s1.display();  
	    s2.display();  
	    s3.display();  

	}

}