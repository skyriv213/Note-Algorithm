import java.util.*;
import java.util.stream.*;
class Solution {
    boolean solution(String s) {
        boolean answer = true;

        long cp = s.chars().filter(a -> a=='p'||a=='P').count();
        long cy = s.chars().filter(a-> a=='y'||a=='Y').count();
        
        
        return cp==cy;
    }
}