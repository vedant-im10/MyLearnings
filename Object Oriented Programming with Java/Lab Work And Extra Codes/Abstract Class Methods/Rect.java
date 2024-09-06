public class Rect extends Shape {    
	public static void main(String[] args) {
		Rect myrect = new Rect();
		myrect.draw();
	}

	@Override
	public void draw() {
		System.out.println("Draw a rectangle");	
	}
}
