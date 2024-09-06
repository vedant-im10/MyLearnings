public class Students {
	   //attributes 
       String studentname;
       String studentid;
       String degreetype;
       String degreename;
       
       int semester,year;
       float cgpa;
       
       //constructor
       public Students(String string, String string2, String string3,
			String string4) {
		      studentname = string;
		      studentid = string2;
		      degreetype = string3;
		      degreename = string4;
        }
	
       //methods
       public void getName()
       {      System.out.println("Name of the student is :" + studentname );
              }
	   
       public void getid()
       {      System.out.println("Id of the student is :" + studentid );
              }
       
       public void getdetails()
       {      System.out.println("\n"+studentname + "\n"+studentid + "\n"+degreetype + "\n"+degreename);  
	       }
       
       /*public void setName(String studentname)
       {      studentname =  studentname;   }  */  
       
       /*public void setName(String studentname)
       {      this.studentname =  studentname;   } */
       
       public void setName(String name)
       {      studentname =  name;   }   

	public static void main(String[] args) {
		// TODO Auto-generated method stub
           Students stu = new Students("rahul","101","4 years degree","CSE or ICT");
           //stu.studentname = "Rohan";
           //stu.studentid = "19bcp007";
           stu.getName();
           stu.getid();
           stu.setName("Rohit");
           stu.getName();
           stu.getdetails();
           System.out.println(stu.studentname);
	}
}
