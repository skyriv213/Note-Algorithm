import java.util.*;

class Solution {
    public long solution(int n, int[] times) {
        
        long start, end,time, total;
        Arrays.sort(times);
        
        start = (long)times[0];
        end = (long)times[times.length-1]*n;
        
        long answer = (long)end;
        while(start<=end){
            time = (start + end)/2;
            total = 0;
            for(int t : times){
                total += (long)time/t;
            }
            
            if(total<n){
                start = time+1;
            }else{
                end = time-1;
                answer = (long)time;
            }
        }
        
        return answer;
    }
}