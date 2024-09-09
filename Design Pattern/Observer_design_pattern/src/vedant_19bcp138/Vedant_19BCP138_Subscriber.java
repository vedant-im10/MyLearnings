package vedant_19bcp138;

public class Vedant_19BCP138_Subscriber implements Vedant_19BCP138_Observer {
	
	private String name;
	private Vedant_19BCP138_Channel channel = new Vedant_19BCP138_Channel();
	
	public Vedant_19BCP138_Subscriber(String name) {
		super();
		this.name = name;
	}
	
	public void update() {
		System.out.println("Hey " + name + ", A new video just uploaded on: " + channel.title);
	}
	
	public void subscribeToChannel(Vedant_19BCP138_Channel ch) {
		channel = ch;
	}

}
