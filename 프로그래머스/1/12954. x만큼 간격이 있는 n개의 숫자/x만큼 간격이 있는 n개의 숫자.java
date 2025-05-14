import java.util.*;
class Solution {
    public ArrayList<Long> solution(int x, int n) {
        ArrayList<Long> answer = new ArrayList<>();
        for(int i = 1; i<= n;i++){
            answer.add((long)x*i);
        }
        return answer;
    }
}