import java.util.*;
import java.util.stream.*;    // java.util.stream의 모든 클래스/인터페이스


class Solution {
    public List<Integer> solution(int[] num_list) {
        List<Integer> ans = Arrays.stream(num_list)
                            .boxed()
                            .collect(Collectors.toList());
        Collections.reverse(ans);
        
        return ans;
    }
}