import java.util.*;

class Solution {
    public int solution(int[][] board, int[] moves) {
        int answer = 0;
        
        Stack<Integer> st = new Stack<>();

        
        for(int m : moves){
            for(int i = 0; i < board.length;i++){
                if(board[i][m-1]!=0){
                    st.add(board[i][m-1]);
                    board[i][m-1] =0;
                    break;
                }
            }
            while((st.size()>2 || st.size()==2) && st.elementAt(st.size()-2)==st.peek()){
                st.pop();
                st.pop();
                answer+=2;
            }
        }
        return answer;
    }
}