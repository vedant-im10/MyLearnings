package vedant_19bcp138_school;

import vedant_19bcp138.PilotPen;

public class School {

	public static void main(String[] s) {
		Pen v = new PenAdapter();
		AssignmentWork vedant = new AssignmentWork();
		vedant.setP(v);
		vedant.writeAssignment("I have started writing Assignment and if will be completed in short period of time.");
	}
		
}