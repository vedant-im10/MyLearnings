interface Bank{  
	float rateOfInterest();  
}  

class SBI implements Bank{  
	public float rateOfInterest(){return 9.15f;}  
}  

class PNB implements Bank{  
	public float rateOfInterest(){return 9.7f;}  
}  

public class Interfa {
	public static void main(String[] args) {
		Bank b=new SBI();  
		SBI sbi = new SBI();
		System.out.println("ROI: "+b.rateOfInterest());  
		System.out.println("ROI: "+sbi.rateOfInterest());  
	}
}
