
public class Rectangle {
	private double length, width; 

	public void setdimension(double l, double w)
	{length = l;
	width = w;            
	}
	
	public void getdimension()
	{System.out.println("Length = " + getlength() + "\n" +"width" + getwidth());}
    
	public double getlength() 
	{return length;}
	
	public double getwidth()
	{return width;}
	
	public double area()
	{return getlength()*getwidth();}
	
	public void getarea()
    {System.out.println(area());}

	public static void main(String[] args) {
    
		Rectangle myrect = new Rectangle();
		myrect.setdimension(5, 4);
		myrect.area();
		myrect.getarea();
        myrect.getdimension();
	}

}
