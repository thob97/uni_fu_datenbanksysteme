import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.Statement;
import java.sql.ResultSet;
public class main {
   public static void main(String[] args) {
      String JdbcURL = "jdbc:postgresql://localhost/dbs";
      String Username = "postgres";
      String password = "postgres";
      Connection con = null;
      Statement stmt = null;
      try {
         con = DriverManager.getConnection(JdbcURL, Username, password);
         stmt = con.createStatement();
         ResultSet rs = stmt.executeQuery("select * from passagier");
         while (rs.next()) {
              String name = rs.getString("vorname");
              System.out.println(name);
          }
      } catch (Exception exec) {
         exec.printStackTrace();
      }
   }
}
