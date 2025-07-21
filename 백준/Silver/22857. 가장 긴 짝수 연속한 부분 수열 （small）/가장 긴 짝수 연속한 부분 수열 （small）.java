//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or

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
        int k = input[1], max = 0;
        int[][] dp = new int[arr.length + 1][k + 1];

        for (int i = 1; i <= arr.length; i++) {
            for (int j = 0; j <= k; j++) {
                if (arr[i - 1] % 2 == 1) {
                    if (j > 0) {
                        dp[i][j] = dp[i - 1][j - 1];
                    }
                } else {
                    dp[i][j] = dp[i - 1][j] + 1;
                }
            }
        }

        for (int i = 0; i < dp.length; i++) {
            for (int j = 0; j < dp[i].length; j++) {
                max = Math.max(max, dp[i][j]);
            }
        }

        System.out.println(max);

    }
}