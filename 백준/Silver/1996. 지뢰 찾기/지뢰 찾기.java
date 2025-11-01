
import java.io.*;

public class Main {

    public static int n;
    public static String [][] s;
    public static int [][] arr;

    public static void check(int bomb, int x, int y){
        int[] dx = {1, 0, -1, 0, 1, 1, -1, -1};
        int[] dy = {0, 1, 0, -1, 1, -1, -1, 1};
        int nx, ny;
        for (int i = 0; i < 8; i++) {
            nx = x + dx[i];
            ny = y + dy[i];
            if(0<=nx && nx<n && 0<=ny && ny<n&& arr[nx][ny]!=-1) {
                arr[nx][ny] += bomb;
            }
        }
        arr[x][y] = -1;
    }


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        n = Integer.parseInt(br.readLine());
        s = new String[n][];
        for(int i = 0; i < n; i++){
            s[i] = br.readLine().split("");
        }

        arr = new int[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if(!s[i][j].equals(".")){
                    check(Integer.parseInt(s[i][j]), i, j);
                }
            }
        }

        StringBuilder sb = new StringBuilder();
        for(int [] arr2 : arr){
            for(int i: arr2){
                if(i==-1){
                    sb.append("*");
                }else if(10<=i){
                    sb.append("M");
                }else{
                    sb.append(String.valueOf(i));
                }
            }
            sb.append("\n");
        }
        System.out.println(sb.toString());

    }

}
