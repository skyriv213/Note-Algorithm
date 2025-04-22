class Solution {
    public int solution(String[][] board, int h, int w) {
        int answer = 0;
        int [] dh ={0,0,-1,1};
        int [] dw ={1,-1,0,0};
        int nw,nh;
        for(int i = 0; i<4; i++){
            nw = w+ dw[i];
            nh = h + dh[i];
            if (0<=nw && nw <board.length && 0<=nh && nh<board[0].length){
                if(board[nh][nw].equals(board[h][w])){
                    answer++;
                }
            }
        }
        return answer;
    }
}