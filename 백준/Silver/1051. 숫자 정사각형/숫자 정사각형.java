import java.io.*;
import java.util.*;

import static java.lang.Math.min;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] temp = br.readLine().split(" ");
        int n = Integer.parseInt(temp[0]);
        int m = Integer.parseInt(temp[1]);
        int [][] arr = new int[n][m];
        for (int i = 0; i < n; i++) {
            temp = br.readLine().split("");
            for (int j = 0; j < m; j++) {
                arr[i][j] = Integer.parseInt(temp[j]);
            }
        }

        int res = 1;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                int maxLength = Math.min(n - i, m - j);
                for (int k = 1; k < maxLength; k++) {
                    if (arr[i][j] == arr[i + k][j] &&
                            arr[i][j] == arr[i][j + k] &&
                            arr[i][j] == arr[i + k][j + k]) {
                        res = Math.max(res, k + 1);
                    }
                }
            }
        }
        System.out.println(res * res);
        br.close();
    }
}