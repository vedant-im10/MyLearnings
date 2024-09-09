package vedant_19bcp138;

public class Vedant_19BCP138_Pasta implements Vedant_19BCP138_Food {
	
	public String preparedItems;
	
	@Override
	public void prepareFood(String itemsRequired)
	{
	preparedItems = "Tomato Paste with ingredients : " + itemsRequired;
	}
	
	@Override
	public String deliverFood()
	{
	return preparedItems;
	}

}
