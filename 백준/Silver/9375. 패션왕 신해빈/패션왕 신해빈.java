//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or

import java.io.*;
import java.util.*;


// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        for (int i = 0; i < n; i++) {
            int m = Integer.parseInt(br.readLine());
            HashMap<String, Integer> map = new HashMap<>();
            for (int j = 0; j < m; j++) {
                String[] line = br.readLine().split(" ");
                map.putIfAbsent(line[1], 0);
                map.put(line[1], map.getOrDefault(line[1], 0) + 1);
            }
            int ans = 1;
            for(int cnt : map.values()){
                ans *= (cnt + 1);
            }
            System.out.println(ans-1);
        }
    }
}
