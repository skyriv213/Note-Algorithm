# [Silver II] 자원 캐기 - 14430 

[문제 링크](https://www.acmicpc.net/problem/14430) 

### 성능 요약

메모리: 34852 KB, 시간: 116 ms

### 분류

다이나믹 프로그래밍

### 제출 일자

2025년 6월 9일 22:08:25

### 문제 설명

<p>인류의 차세대 인공지능 자원 캐기 로봇인 WOOK은 인간 대신 자원을 캐는 로봇이다. WOOK은 언제나 제한된 범위 내에서 자원을 탐색하며, 왼쪽 위 (1, 1)부터 오른쪽 아래 (N, M)까지 자원을 탐색한다. WOOK은 한 번에 오른쪽 또는 아래쪽으로 한 칸 이동할 수 있으며, 그 외의 방향으로 움직이는 것은 불가능하다. WOOK은 자신이 위치한 (x, y)에 자원이 있는 경우에만 해당 자원을 채취할 수 있다. WOOK이 탐사할 영역에 대한 정보가 주어질 때, WOOK이 탐색할 수 있는 자원의 최대 숫자를 구해라!</p>

### 입력 

 <p>첫째 줄에 WOOK이 탐사할 영역의 세로길이 N(1≤N≤300)과 가로길이 M(1≤M≤300)이 주어진다. 그 다음 N행 M열에 걸쳐 탐사영역에 대한 정보가 주어진다. 숫자는 공백으로 구분된다. (자원은 1, 빈 땅은 0으로 표시된다)</p>

### 출력 

 <p>WOOK이 수집할 수 있는 최대 광석의 개수를 출력하라.</p>

