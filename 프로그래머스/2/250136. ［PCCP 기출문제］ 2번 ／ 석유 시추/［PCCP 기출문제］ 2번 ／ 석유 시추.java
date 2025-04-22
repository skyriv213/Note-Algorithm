import java.util.*;

class Solution {
    // 좌표를 입력받을 Point 객체 생성
    static class Point{
        int x;
        int y;
        
        public Point(int x, int y){
            this.x= x;
            this.y =y;
        }
    }
    public int solution(int[][] land) {
        int answer = 0;
        // land의 행,열 크기 파악
        int row = land.length;
        int col = land[0].length;
        
        // 이동을 위한 이동계 선언
        int [] dx = {0,0,1,-1};
        int [] dy = {1,-1,0,0};
        
        // 해당 지역을 돌았는지 체크하기 위한 배열, 각 열당 가능한 총량 체크의 Map 선언
        boolean [][] check= new boolean [row][col];
        Map<Integer, Integer> oil = new HashMap<Integer, Integer>(); // put, getOrDefualt()사용
        
        
        // 기본적으로 모든 값은 false로 값을 가지게 됨
//         for(int i = 0; i< row; i++){
//             for(int j = 0 ; j< col ; j++){
//                 check[i][j] =false;
//             }
//         }
        
        // land 순회
        for(int i = 0 ; i< row; i++){
            for(int j = 0 ;j<col;j++){
                // 석유가 있고(1), 방문기록이 없으면 !false
                if(land[i][j]== 1 && !check[i][j]){
                    Queue<Point> q = new LinkedList<>(); // add, poll 사용
                    Set<Integer> set = new HashSet<>(); // add 사용
                    int oilS = 0; // 파악가능 한 석유 총량 bfs
                    q.add(new Point(i,j));
                    check[i][j] = true;
                    // bfs 진행
                    while(!q.isEmpty()){
                        Point p = q.poll();
                        int x = p.x;
                        int y = p.y;
                        oilS++;
                        check[i][j]= true;
                        set.add(y);
                        for(int k = 0; k< 4; k++){
                            int nx = x+ dx[k];
                            int ny = y+ dy[k];
                            if(0<=nx && nx< row && 0<=ny && ny<col){
                                if(land[nx][ny]== 1 && !check[nx][ny]){
                                    check[nx][ny]=true;
                                    q.add(new Point(nx, ny));
                                }
                            }
                        }
                    }
                    for (int c : set){
                        oil.put(c, oil.getOrDefault(c,0) + oilS);
                    }
                }
            }
        }
        
        
        
        return oil.values().stream().max(Integer::compare).orElse(0);
    }
}
