package vedant_19bcp138_school;

public class AssignmentWork {
	
	private Pen v;
		
	public Pen getP() {
		return v;
	}

	public void setP(Pen v) {
		this.v = v;
	}

	public void writeAssignment(String str) {
		v.write(str);
	}

}