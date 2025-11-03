import java.io.*;
import java.util.Arrays;
import java.util.*;

/**
 * n개의 교실과 n/2개의 반이 있음
 * 각 반을 홀수 번호인 학생들과 짝수 번호인 학생들로 나눠 사용할 예정
 * 반 배정을 고려하지 않은 채, 교실을 두 개씩 짝지어 전달
 * 교실 짝짓는 방법 하나당 초코파이 1개, 총 몇개 가능? -> 반을 정하는 경우의 수를 구하라
 *
 */


public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.valueOf(br.readLine());
        int k = Integer.valueOf(br.readLine());

        if(k>=n){
            System.out.print(0);
            return;
        }
        int[] sensor = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::valueOf).toArray();
        Arrays.sort(sensor);
        Integer[] distance = new Integer[n - 1];
        for (int i = 0; i < n - 1; i++) {
            distance[i] = sensor[i + 1] - sensor[i];
        }
        Arrays.sort(distance, Collections.reverseOrder());
        long total = 0;
        for(int i = k-1 ; i < n-1; i++){
            total += distance[i];
        }
        System.out.println(total);
        br.close();

    }
}