#include<iostream>
#include<queue>
#include<algorithm>
#define MAX 1000
using namespace std;

int m, n;

void bfs(queue<pair<int,int>> q, int visited[][MAX])
{
    int dx[4] = {-1, 1, 0, 0};
    int dy[4] = {0, 0, -1, 1};

    while(!q.empty())
    {
        int x = q.front().first;
        int y = q.front().second;
        q.pop();

        for(int i=0; i<4; i++)
        {
            int nx = x + dx[i];
            int ny = y + dy[i];

            if(nx >= 0 && nx < n && ny >= 0 && ny < m)
            {
                if(visited[nx][ny]==0 || visited[nx][ny] > visited[x][y] + 1)
                {
                    q.push({nx, ny});
                    visited[nx][ny] = visited[x][y] + 1;
                }
            }
        }
    }
}
int main()
{
    cin >> m >> n;
    queue<pair<int,int>> q;
    int visited[MAX][MAX];

    int cnt=0;
    for(int i=0; i<n; i++)
    {
        for(int j=0; j<m; j++)
        {
            int x;
            cin >> x;
            if(x == 0)
            {
                visited[i][j] = 0;
                cnt++;
            }
            else
            {
                if(x == 1)
                {
                    q.push({i, j});
                }
                visited[i][j] = 1;

            }
        }
    }

    if(cnt==0)
    {
        cout << 0;
        exit(0);
    }

    bfs(q, visited);
    int ans = 0;
    for(int i=0; i<n; i++)
    {
        for(int j=0; j<m; j++)
        {
            if(visited[i][j]==0)
            {
                cout << -1;
                exit(0);
            }
            else if(ans < visited[i][j])
            {
                ans = visited[i][j];
            }
        }
    }
    cout << ans-1;
}