
import java.io.*;


import static java.util.Arrays.stream;

// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {


    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[] input = stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt).toArray();
        int[] arr = stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt).toArray();

        int n = input[0], k = input[1];

        int start = 0, cnt = 0, max = 0;
        
        for (int end = 0; end < n; end++) {
            if (arr[end] % 2 != 0) {
                cnt++;
            }
            while (cnt > k) {
                if (arr[start] % 2 != 0) {
                    cnt--;
                }
                start++;
            }
            max = Math.max(max, end - start + 1 - cnt);

        }
        System.out.println(max);
    }
}