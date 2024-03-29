/*

[c++ 문법 정리]

1.  #include<iostream>
    using namespace std;
2.  #include<algorithm> : sort 함수
3.  #include<vector>, #include<queue>
4.  정렬
    (1) vector: sort(arr.begin(), arr.end());
    (2) 배열: sort(arr, arr+MAX);
5.  vector: push_back(), pop_back()
6.  queue: push(), pop(), push()
7.  pair<int, int> a = {x, y};
       -> a.first, a.second
8.  string: 내부 값 변경 가능
9.  cin >> value;
    cout << value << endl;

*/
#include<iostream>
#include<vector>
#include<queue>
#include<algorithm>

#define MAX 26
using namespace std;

int cnt;

void bfs(int x, int y, int n, string graph[])
{
    queue<pair<int, int>> q;
    q.push({x, y});
    graph[x][y] = '0';
    cnt++;

    int dx[4] = {-1, 1, 0, 0};
    int dy[4] = {0, 0, -1, 1};
    
    while(!q.empty())
    {
        pair<int, int> loc = q.front();
        q.pop();

        for(int i=0; i<4; i++)
        {
            int nx = loc.first + dx[i];
            int ny = loc.second + dy[i];

            if(nx >= 0 && nx < n && ny >= 0 && ny < n && graph[nx][ny] == '1')
            {
                q.push({nx, ny});
                graph[nx][ny] = '0';
                cnt++;
            }
        } 
    }
}

int main()
{
    string graph[MAX];
    vector<int> result;
    
    int n;
    cin >> n;
    
    for(int i=0; i<n; i++)
    {
        cin >> graph[i];
    }
    for (int i=0; i<n; i++)
    {
        for(int j=0; j<n; j++)
        {
            if(graph[i][j]=='1')
            {
                cnt = 0;
                bfs(i, j, n, graph);
                result.push_back(cnt);
            }
        }
    }
    sort(result.begin(), result.end());
    cout << result.size() << endl;
    for(int i=0; i<result.size(); i++)
    {
        cout << result[i] << endl;
    }

}