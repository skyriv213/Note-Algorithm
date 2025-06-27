import java.util.*;


class Solution {
    public int solution(int[] mats, String[][] park) {
        int ms = 1;
        int n =park.length;
        int m = park[0].length;
        int [][] board = new int[n][m];
        int [][] dp = new int[n][m];
        for(int i = 0; i < n; i++){
            for(int j = 0; j<m;j++){
                if(park[i][j].equals("-1")){
                    board[i][j] = 1;
                }
            }
        }
        
        for(int i = 0; i< n;i++){
            for(int j = 0; j< m;j++){
                if(board[i][j] == 1){
                    if(i==0||j==0){
                        dp[i][j]= 1;
                    }else{
                        dp[i][j] = Math.min(dp[i-1][j-1], Math.min(dp[i-1][j],dp[i][j-1]))+1;
                    }
                    ms = Math.max(dp[i][j],ms);
                }
            }
        }
        int bestSize = -1;
        for (int size : mats) {
            if (size <= ms && size > bestSize) {
                bestSize = size;
            }
        }
        return bestSize;
    }
}