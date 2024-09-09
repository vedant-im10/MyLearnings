package vedant_19bcp138;

public interface Vedant_19BCP138_Subject {
	
	void subscribe(Vedant_19BCP138_Subscriber sub);
	void unsubscribe(Vedant_19BCP138_Observer sub);
	void notifySubscriber();
	void upload(String title);

}
