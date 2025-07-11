import java.io.*;
import java.util.HashSet;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        HashSet<String> users = new HashSet<>();
        String[] s = br.readLine().split(" ");
        Integer num = Integer.parseInt(s[0]);

        for (int i = 0; i < num; i++) {
            String people = br.readLine();
            users.add(people);
        }
        if (s[1].equals("Y")) {
            System.out.println(users.size());
        } else if (s[1].equals("F")) { //3명, 
            System.out.println(users.size()/2);
        }else{
            System.out.println(users.size()/3);
        }

    }
}