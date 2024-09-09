package vedant_19bcp138;

public class Vedant_19BCP138_Customer {
	
	public static void main(String[] args) {
		
		//Without Facade Design Pattern
		System.out.println("WITHOUT FACADE DESIGN PATTERN");
		Vedant_19BCP138_Ingredients ingredients = new Vedant_19BCP138_Ingredients();
		
		Vedant_19BCP138_Food pasta = new Vedant_19BCP138_Pasta(); 
		String pastaItems = ingredients.getPastaItems();
		pasta.prepareFood(pastaItems);
		System.out.println(pasta.deliverFood());
		
		Vedant_19BCP138_Food pizza = new Vedant_19BCP138_Pizza();
		String pizzaItems = ingredients.getPizzaItems();
		pizza.prepareFood(pizzaItems);
		System.out.println(pizza.deliverFood());
		
		//With Facade Design Pattern
		System.out.println("\n\nWITH FACADE DESIGN PATTERN");
		System.out.println(Vedant_19BCP138_Waiter.deliverFood("Pasta"));
		System.out.println(Vedant_19BCP138_Waiter.deliverFood("Pizza"));
		}

}
