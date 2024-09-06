public class Box extends Rectangle {
    private double height;
    
    public void setdimension(double l,double w, double h) 
    {super.setdimension(l, w);
     if (h>=0)
     {height = h;}
     else 
     {height = 0;}	 
    }
	
    public void getheight() 
    {System.out.println("height = " + height);} 
    
    public double area() 
    {return 2*(getlength()*getwidth() + getlength()*height + getwidth()*height);
     }
	
    public void getarea()
    {System.out.println(area());}
    
    public static void main(String[] args) {
    Box mybox = new Box();    	 
    mybox.setdimension(5, 4, 2);	
    mybox.area();
    mybox.getarea();
    Rectangle recbox = new Box();
    recbox.getarea();
	}
}
