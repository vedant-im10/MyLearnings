package vedant_19bcp138_school;

import vedant_19bcp138.PilotPen;

public class PenAdapter implements Pen {
	
	PilotPen vv = new PilotPen();
		
	public void write(String str) {
		vv.mark(str);
	}
		
}