import java.util.*;

class Solution {
    public ArrayList<Integer> solution(int[] num_list) {
        ArrayList<Integer> answer = new ArrayList<>();
        for (int num : num_list) {
            answer.add(num);
        }
        
        if (answer.get(answer.size() - 1) > answer.get(answer.size() - 2)) {
            answer.add(answer.get(answer.size() - 1) - answer.get(answer.size() - 2));
        } else {
            answer.add(answer.get(answer.size() - 1) * 2);
        }
        
        return answer;
    }
}