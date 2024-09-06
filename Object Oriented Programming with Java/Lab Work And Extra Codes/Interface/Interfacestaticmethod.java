interface Drawing{  
	void draw();  
	static int cube(int x){return x*x*x;}  
}  

class Recta implements Drawing{  
	public void draw(){System.out.println("drawing rectangle");}  
}  

public class Interfacestaticmethod {
	public static void main(String[] args) {
		Drawing d=new Recta();  
		d.draw();  
		System.out.println(Drawing.cube(4));  
	}
}
