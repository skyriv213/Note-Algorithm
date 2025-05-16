import java.util.*;
/***
그리디 알고리즘
건전지 최소화 -> 순간이동을 최대한 많이 실행.
n%2 == 0이라면 순간이동이 가능
아니라면 n--를 진행 후 ans++을 통해 정답 카운트 증가
*/
public class Solution {
    public int solution(int n) {
        int ans = 0;
        ans ++;
        while(n>1){
            if(n%2==0){
                n=n/2;
            }else{
                n--;
                ans++;
            }
        }

        return ans;
    }
}