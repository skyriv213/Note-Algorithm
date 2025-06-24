class UnionFind{
    
    private static int [] parent;
    private static int [] size;
    
    public UnionFind(int s){
        this.parent = new int[s+1];
        this.size = new int[s+1];
        
        for(int i =1 ; i< s+1;i++){
            parent[i]=i;
            size[i]=1;
        }
        
    }
    
    public static int find(int x){
        if(parent[x]!=x){
            parent[x] = find(parent[x]);
        }
        return parent[x];
    }
    
    public static void union(int a, int b){
        a = find(a);
        b = find(b);
        if(a==b) return;
        if(a<b){
            parent[b] = a;
            size[a]+= size[b];
        }else{
            parent[a] =b;
            size[b] += size[a];
        }
        
    }
    
    public static int getComponentSize(int x){
        return size[find(x)];
    }
    
}


class Solution {
    public int solution(int n, int[][] wires) {
        int answer = n;
        
        for(int i = 0; i<wires.length; i++){
            UnionFind u = new UnionFind(n);
            for(int j = 0; j< wires.length;j++){
                if(i==j) continue;
                u.union(wires[j][0],wires[j][1]);
            }
            int compSize = u.getComponentSize(1);
            int diff = Math.abs(2*compSize -n);
            if(diff<answer){
                answer = diff;
            }
        }
        return answer;
    }
}