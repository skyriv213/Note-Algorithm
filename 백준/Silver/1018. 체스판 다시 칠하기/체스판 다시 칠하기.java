import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] s = br.readLine().split(" ");
        int n = Integer.parseInt(s[0]);
        int m = Integer.parseInt(s[1]);

        String[][] chess = new String[n][m];
        for (int i = 0; i < n; i++) {
            String line = br.readLine();
            for (int j = 0; j < m; j++) {
                chess[i][j] = String.valueOf(line.charAt(j));
            }
        }
        int minChanges = Integer.MAX_VALUE;

        for (int i = 0; i <= n - 8; i++) {
            for (int j = 0; j <= m - 8; j++) {
                int whiteStartChanges = 0;
                for (int a = i; a < i + 8; a++) {
                    for (int b = j; b < j + 8; b++) {
                        // (a + b) % 2 == 0 이면 시작 색과 같아야 함
                        if ((a + b) % 2 == 0) {
                            if (!chess[a][b].equals("W")) {
                                whiteStartChanges++;
                            }
                        } else {
                            if (!chess[a][b].equals("B")) {
                                whiteStartChanges++;
                            }
                        }
                    }
                }
                minChanges = Math.min(minChanges, Math.min(whiteStartChanges, 64 - whiteStartChanges));
            }
        }

        System.out.println(minChanges);
        br.close();
    }
}
