import java.sql.*;
public class movie_db {
	public static void main(String args[]) {
		try {
			// passing driver-class name
			Class.forName("org.sqlite.JDBC");
			// Creating a connection
			Connection con= DriverManager.getConnection("jdbc:sqlite:movies_list.db");
			if(con!=null)
			{
				//System.out.println("Connection Established");
				// All the sql queries can be written using statement object
				Statement st= con.createStatement();
				String sql ="CREATE TABLE movies_list"+
						"(movie_name text,"+
						"lead_actor text," + 
						"actress text,"+ 
						"release_date text,"+ 
						"director_name text)";
				// executeUpdate returns a integer value 0 if created 
				int n=st.executeUpdate(sql);
				// Inserting data into Table
				String insert= "INSERT INTO movies_list values"
						+ "('Maharshi','Mahesh Babu', 'Pooja Hegde', '9-May-2019','Vamshi Paidapally'),"
						+ "('Pushpa', 'Allu Arjun','Rashmika Mandanna','25-December-2021', 'Sukumar'),"
						+ "('Rangasthalam', 'Ram Charan','Samantha', '30-March-2018', 'Sukumar'),"
						+ "('Geetha Govindam', 'Vijay Deverakonda','Rashmika Mandanna', '15-August-2018', 'Parasuram'),"
						+ "('Rebel', 'Prabhas', 'Tamanna','28-Sepetember-2012', 'Raghava Lawrence'),";
				// now we need to use executeUpdate(for non select queries)
				int rec=st.executeUpdate(insert);
				// rec has the number of values
				System.out.println("Number of recrds:- "+rec);

				ResultSet rs= st.executeQuery("select * from movies");
				int i=0;
				while(rs.next()) {
					System.out.println("MOVIE - "+i+" Details");
					System.out.println("Movie Name:- "+rs.getString(1));
					System.out.println("Hero Name:- "+rs.getString(2));
					System.out.println("Actress Name:- "+rs.getString(3));
					System.out.println("Release Date:- "+rs.getString(4));
				}
			}
		}
		catch(Exception e)
		{
			System.out.println(e);
		}

	}

}
