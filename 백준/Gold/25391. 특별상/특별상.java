
import java.io.*;
import java.util.Arrays;
import java.util.*;


/***
 * 학생수 n, 특별상 m, 본상 k
 * 주최자 점수 , 심판 점수
 * 주최자의 점수가 최대
 * 그렇다면 총 m+k명을 골라야함
 * 이때 주최자의 점수가 가장 큰 학생들로 m+k명 골라야함
 * 이때 심판의 점수가 k 명
 * 그럼 정렬을 점수가 가장 큰 m
 * 정렬점수를 먼저 심판을 기준으로 정렬
 * 해당 인원들은 무조건 상이므로 해당 인원 이후 인원 k 명 선발
 */

public class Main {

    //
//    public static void main(String[] args) throws IOException {
//        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//        int[] arr = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray(); // n,m,k
//        int n = arr[0];
//        int m = arr[1];
//        int k = arr[2];
//        point[] points = new point[n];
//        StringTokenizer st ;
//
//        for (int i = 0; i < n; i++) {
//            st = new StringTokenizer(br.readLine());
//            points[i] = new point(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()));
//        }
//        Arrays.sort(points, new Comparator<point>() {
//            @Override
//            public int compare(point o1, point o2) {
//                return o2.s1 - o1.s1;
//            }
//        });
//        int res = 0;
//        for (int i = 0; i < m; i++) {
//            res += points[i].s1;
//        }
//
//        Arrays.sort(points, m, n, new Comparator<point>() {
//            @Override
//            public int compare(point o1, point o2) {
//                return o2.s2 - o1.s2;
//            }
//        });
//        for(int i = m; i< m+k; i++){
//            if(i< n){
//                res += points[i].s1;
//            }
//        }
//        System.out.println(res);
//
//    }
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());
        int[][] arr = new int[n][2];

        for(int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            arr[i][0] = Integer.parseInt(st.nextToken());
            arr[i][1] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(arr, (e1, e2) -> {
            return e2[1] - e1[1];
        });
        long res = 0;
        for(int i = 0; i < k; i++) {
            res += arr[i][0];
        }

        int[][] arr2 = new int[n - k][2];
        for (int i = 0; i < n - k; i++) {
            arr2[i][0] = arr[i+k][0];
            arr2[i][1] = arr[i+k][1];
        }
        Arrays.sort(arr2, (e1, e2) -> {
            return e2[0] - e1[0];
        });

        for(int i = 0; i < m; i++) {
            res += arr2[i][0];
        }
        System.out.println(res);

    }
}