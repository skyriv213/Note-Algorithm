
import java.io.*;
import java.util.*;

import static java.util.Arrays.stream;


// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] line = br.readLine().split(" ");
        int n = Integer.parseInt(line[0]), m = Integer.parseInt(line[1]);

        HashMap<String, String> map = new HashMap<>();

        for(int i = 0; i < n; i++){
            line = br.readLine().split(" ");
            map.put(line[0], line[1]);
        }
        for (int i = 0; i < m; i++){
            System.out.println(map.get(br.readLine()));

        }
    }
}
