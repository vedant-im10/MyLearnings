package vedant_19bcp138;

public class Vedant_19BCP138_vedantYoutube {
	
	public static void main(String args[]) {
		
	Vedant_19BCP138_Channel design = new Vedant_19BCP138_Channel();
	
	Vedant_19BCP138_Subscriber v1 = new Vedant_19BCP138_Subscriber("Vedant");
	Vedant_19BCP138_Subscriber v2 = new Vedant_19BCP138_Subscriber("VEDANT");
	Vedant_19BCP138_Subscriber v3 = new Vedant_19BCP138_Subscriber("Vedu");
	Vedant_19BCP138_Subscriber v4 = new Vedant_19BCP138_Subscriber("VEDU");
	Vedant_19BCP138_Subscriber v5 = new Vedant_19BCP138_Subscriber("Ved");
	Vedant_19BCP138_Subscriber v6 = new Vedant_19BCP138_Subscriber("VED");
	Vedant_19BCP138_Subscriber v7 = new Vedant_19BCP138_Subscriber("Haresh");
	
	design.subscribe(v1);
	design.subscribe(v2);
	design.subscribe(v3);
	design.subscribe(v4);
	design.subscribe(v5);
	design.subscribe(v6);
	design.subscribe(v7);
	design.unsubscribe(v5);

	v1.subscribeToChannel(design);
	v2.subscribeToChannel(design);
	v3.subscribeToChannel(design);
	v4.subscribeToChannel(design);
	v5.subscribeToChannel(design);
	v6.subscribeToChannel(design);
	v7.subscribeToChannel(design);
		
	design.upload("Observer Design Pattern");
	}
		
}
