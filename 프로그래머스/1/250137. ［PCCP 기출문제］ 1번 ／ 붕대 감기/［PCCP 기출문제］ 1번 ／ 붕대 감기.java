// '''
// t초동안 동작 반복, 1초 동안 x의 체력 회복,'연속'으로 동작 성공시 체력은 t*x+y
// 최대 체력 < 회복체력은 불가능
// 몬스터에게 공격을 당하면 동작 취소 및 피해량만큼 체력 감소

// bondage = 시전시간, 초당 회복력, 추가 회복량 (t,x,y) t초 동안 붕대를 감으면서 1초마다 x만큼의 체력을 회복, t초동안 감는 것에 성공 시 y만큼 체력 회복,  -> 최대 체력이 존재해서 해당 체력보다 커지는 것은 불가능.
// health = 최대 체력
// attack = 공격시간, 피해량

// 추가 변수
// 연속 성공 시간

// 결과
// 모든 공격이 끝난 뒤에 남은 체력 반환

// '''

class Solution {
    public int solution(int[] bandage, int health, int[][] attacks) {
        int max_health = health;
        int time = 0;
        boolean check = true;
        int cnt = 0; // t랑 비교를 위한 변수
        
        for(int i = 0 ; i < attacks.length;i++){
            if(time< attacks[i][0]){
                time = attacks[i][0];
            }
        }

        for(int i = 1; i <=time;i++){
            for(int j = 0;j<attacks.length;j++){
                if (i < attacks[j][0]){
                    break;
                }
                if (i == attacks[j][0]){
                    health-=attacks[j][1];
                    check = false;
                }
            }
            if(health <=0){
                return -1; // 사망
            }else{
                // 체력 회복
                if(check){
                    cnt++;
                    if(cnt == bandage[0]){
                        health += bandage[1]+bandage[2];
                        cnt =0;
                    }else{
                        health += bandage[1];
                    }
                    if(max_health < health){
                        health = max_health;
                    }
                }else{
                    check = true;
                    cnt = 0;
                }
                
            }
            
        }
        return health;
    }
}