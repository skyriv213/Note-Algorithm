import java.util.*;

class Solution {
    public int solution(String[][] clothes) {
        int answer = 1;
        
        HashMap<String, Integer> c = new HashMap<>();
        
        for(String[] s: clothes){
            c.merge(s[1], 1, Integer::sum);
        }
        for(int n : c.values()){
            answer*=n+1;
        }
        return answer-1;
    }
}