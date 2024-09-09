package vedant_19bcp138;

public class Vedant_19BCP138_Pizza implements Vedant_19BCP138_Food {
	
	public String preparedItems;
	
	@Override
	public void prepareFood(String itemsRequired)
	{
	preparedItems = "Pizza prepared with ingredients : " + itemsRequired;
	}
	
	@Override
	public String deliverFood()
	{
	return preparedItems;
	}

}
