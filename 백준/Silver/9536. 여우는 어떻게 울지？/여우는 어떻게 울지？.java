import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.Arrays;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int t = Integer.parseInt(br.readLine());
        String s;
        for (int i = 0; i < t; i++) {
            ArrayList<String> calling = new ArrayList<>(Arrays.asList(br.readLine().split(" ")));
            while(true){
                s = br.readLine();
                if(s.equals("what does the fox say?")){
                    break;
                }
                String [] animal = s.split(" ");
                calling.removeIf(a -> a.equals(animal[2]));
            }
            String[] arr = calling.toArray(new String[0]);
            System.out.println(String.join(" ", arr));

        }
    }
}
