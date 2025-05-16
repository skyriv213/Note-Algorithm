class Solution {
    public String solution(String s) {
    
        StringBuilder sb = new StringBuilder();
        boolean start = true;
        for(char c : s.toCharArray()){
            if(start && Character.isLetter(c)){
                sb.append(Character.toUpperCase(c));
                start = false;
            }else{
                sb.append(Character.toLowerCase(c));
                if(c == ' ') start = true;
                else start = false;
            }
            if (c==' ') start = true;
        }
        return sb.toString();
    }
}