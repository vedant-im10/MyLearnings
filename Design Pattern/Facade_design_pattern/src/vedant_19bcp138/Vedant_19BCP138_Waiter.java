package vedant_19bcp138;

public class Vedant_19BCP138_Waiter {
	
	public static String deliverFood(String s) {
		
	Vedant_19BCP138_Ingredients ingredients = new Vedant_19BCP138_Ingredients();
	
	if(s.equals("Pizza"))
	{
	Vedant_19BCP138_Food pizza = new Vedant_19BCP138_Pizza();
	String pizzaItems = ingredients.getPizzaItems();
	pizza.prepareFood(pizzaItems);
	return pizza.deliverFood();
	}
	
	if(s.equals("Pasta"))
	{
	Vedant_19BCP138_Food pasta = new Vedant_19BCP138_Pasta();
	String pastaItems = ingredients.getPastaItems();
	pasta.prepareFood(pastaItems);
	return pasta.deliverFood();
	}
	return null;
	}

}
