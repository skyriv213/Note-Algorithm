import java.util.*;

class Solution {
    public long solution(int n, int[] works) {
        long answer = 0;
        PriorityQueue<Integer> queue = new PriorityQueue<>(Collections.reverseOrder());
        for(int i : works){
            queue.add(i);
        }
        for(int i = 0 ; i < n;i++){
            if(!queue.isEmpty()){
                int j = queue.poll();
                if(j-1!=0){
                    queue.add(j-1);     
                }else{
                    continue;
                }
            }else{
                break;
            }
        }
        for(int i : queue){
            answer += i*i;
        }
        return answer;
    }
}