import java.util.*;
import java.io.*;

class Solution {
    
    static boolean[][] check;
    static ArrayList<ArrayList<String>> list;
    
    static int[] dx = {1,-1,0,0};
    static int[] dy = {0,0,-1,1};
    
    static class Point{
        int x, y;
        public Point(int x, int y){
            this.x = x;
            this.y = y;
        }
        
    }
    public int bfs(int a, int b){
        int cnt = Integer.parseInt(list.get(a).get(b));
        check[a][b] = true;

        Queue<Point> q = new LinkedList<>();
        q.add(new Point(a,b));

        
        while (!q.isEmpty()){
            Point p = q.poll();
            int x = p.x;
            int y = p.y;
            for(int i =0; i<4;i++){
                int nx = x+dx[i];
                int ny = y+dy[i];
                if (0 <= nx && nx < list.size() && 0 <= ny && ny < list.get(0).size()) {

                    if (!"X".equals(list.get(nx).get(ny)) && !check[nx][ny]) {
                        cnt+=Integer.parseInt(list.get(nx).get(ny));
                        check[nx][ny]=true;
                        q.add(new Point(nx,ny));
                    }
                }
            }
        }
        
        return cnt;
    }
    
    
    public int[] solution(String[] maps) {
        List<Integer> answer = new ArrayList<>();
        
        
        
        list = new ArrayList<>();
        for(String s : maps){
            ArrayList<String> row = new ArrayList<>(Arrays.asList(s.split("")));
            list.add(row);
        }
        
        check = new boolean[maps.length][maps[0].length()];
        
        
        
        for(int x = 0 ; x< maps.length;x++){
            for(int y = 0;y<maps[0].length();y++){
                if (!check[x][y] && !"X".equals(list.get(x).get(y))) {
                    answer.add(bfs(x,y));
                }
            }
        }

        
        if(answer.isEmpty()){
            return new int[]{-1};
        }
        return answer.stream().sorted().mapToInt(i -> i).toArray();
    }
}