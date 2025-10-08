import java.util.*;

class Solution {
    public int solution(int n, int k) {
        int answer = 0;
        
        String [] sarr = Integer.toString(n, k).split("0");
        for(String s: sarr){
            if(s.isEmpty()){                
                continue;
            }
            long l = Long.valueOf(s);
            if(isPrime(l)){
                answer++;
            }
        }
    
        return answer;
    }
    
    private boolean isPrime(long num) {
        if (num <= 1) {
            return false;
        }
        if (num == 2) {
            return true;
        }
        if (num % 2 == 0) {
            return false;
        }
        for (long i = 3; i * i <= num; i += 2) {
            if (num % i == 0) {
                return false;
            }
        }
        return true;
    }
}