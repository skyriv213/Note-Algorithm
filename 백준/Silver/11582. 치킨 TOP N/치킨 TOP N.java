import java.io.*;
import java.util.*;
import java.util.stream.IntStream;

public class Main {

    static int n, k;
    static int[] arr;

    private static void makeSort(int start, int end) {

        if (end-start == n / k) {
            Arrays.sort(arr, start, end);
            return;
        }
        int half = (start+end) / 2;
        makeSort(start, half);
        makeSort(half, end);
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        arr = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        k = Integer.parseInt(br.readLine());

        makeSort(0, n);
        StringBuilder sb = new StringBuilder();
        for (int i : arr) {
            sb.append(i +" ");
        }
        System.out.println(sb);
    }
}
