
import java.io.*;
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String s = br.readLine();

        System.out.println(Integer.parseInt(s.split(" ")[1]) ^ Integer.parseInt(s.split(" ")[0]));
    }
}