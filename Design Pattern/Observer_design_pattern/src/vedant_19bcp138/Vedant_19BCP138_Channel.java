package vedant_19bcp138;

import java.util.ArrayList;
import java.util.List;

public class Vedant_19BCP138_Channel implements Vedant_19BCP138_Subject {
	
	private List<Vedant_19BCP138_Subscriber> subs = new ArrayList<Vedant_19BCP138_Subscriber>();
	
	public String title;
	
	public void subscribe(Vedant_19BCP138_Subscriber sub) {
		subs.add(sub);
	}
	
	public void unsubscribe(Vedant_19BCP138_Observer sub) {
		subs.remove(sub);
	}
	public void notifySubscriber() {
		for(Vedant_19BCP138_Observer sub:subs) {
			sub.update();
		}
	}
	
	public void upload(String title) {
		this.title = title;
		notifySubscriber();
	}

}
