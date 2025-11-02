
import java.io.*;
import java.util.Arrays;

public class Main {
    public static int[] nsr;
    public static boolean[] participation;

    public static boolean[] extra;
    public static boolean check(int idx) {
        // 1. 왼쪽 이웃 (idx - 1) 확인 (idx > 0)
        if (idx > 0 && extra[idx - 1]) {
            extra[idx - 1] = false;
            return true;
        }

        // 2. 오른쪽 이웃 (idx + 1) 확인 (idx < N-1)
        if (idx < participation.length - 1 && extra[idx + 1]) {
            extra[idx + 1] = false;
            return true;
        }

        // 3. 빌릴 수 없으면
        return false;
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        nsr = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        participation = new boolean[nsr[0]];
        Arrays.fill(participation, true);

        int[] arr = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        // 참여불가 참가자 세팅
        for (int i : arr) {
            participation[i-1] = false;
        }
        // 여분 카약 세팅, 그리고 파손 카약 확인
        extra = new boolean[nsr[0]];
        Arrays.fill(extra, false);
        arr = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();

        for (int i : arr) {
            if (!participation[i-1]) {
                participation[i-1] = true;
            } else {
                extra[i-1] = true;
            }
        }
        int cnt = 0;
        for (int i = 1; i <= nsr[0]; i++) {
            if (!participation[i-1]) { // 참가자의 카약이 파손된 상태라 참가 불가능하다면?
                if (!check(i-1)) { // 옆에 참가자가 카약이 있는지 판단
                    cnt++;
                }
            }

        }
        System.out.println(cnt);

    }
}

