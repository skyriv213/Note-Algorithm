
import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String [] s = br.readLine().split(" ");
        int n = Integer.parseInt(s[0]);
        int k = Integer.parseInt(s[1]);
        String[] s1 = br.readLine().split(" ");
        ArrayList<Integer> arr = new ArrayList<>();
        for (int i = 0; i < s1.length; i++) {
            arr.add(Integer.parseInt(s1[i]));
        }
        int left = 0;
        int right = k;
        int temp = new ArrayList<>(arr.subList(left, right)).stream().mapToInt(Integer::intValue).sum();
        int max = temp;
        while (right < n) {
            temp = temp - arr.get(left) + arr.get(right);
            right++;
            left++;
            if (temp > max) {
                max = temp;
            }
        }
        System.out.println(max);
        br.close();
    }
}