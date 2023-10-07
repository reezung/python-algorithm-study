#include<iostream>
#include<queue>
#define MAX 50
using namespace std;

void bfs(int r, int c, int n, int m, int graph[][MAX])
{
    queue<pair<int,int>> q;
    q.push({r, c});
    graph[r][c] = 0;

    int dr[4] = {-1, 1, 0, 0};
    int dc[4] = {0, 0, -1, 1};

    while(!q.empty())
    {
        int r = q.front().first;
        int c = q.front().second;
        q.pop();

        for(int i=0; i<4; i++)
        {
            int nr = r+dr[i];
            int nc = c+dc[i];

            if(nr>=0&&nr<n&&nc>=0&&nc<m)
            {
                if(graph[nr][nc]==1)
                {
                    q.push({nr,nc});
                    graph[nr][nc]=0;
                }
            }
        }
    }
}
int main()
{
    int t;
    cin >> t;
    for(int i=0; i<t; i++)
    {
        int m, n, k;
        int graph[MAX][MAX] = {0, };
        cin >> m >> n >> k;
        for(int j=0; j<k; j++)
        {
            int x, y;
            cin >> x >> y;
            graph[y][x] = 1;
        }

        int ans=0;
        for(int r=0; r<n; r++)
        {
            for(int c=0; c<m; c++)
            {
                if(graph[r][c]==1)
                {
                    ans++;
                    bfs(r, c, n, m, graph);
                }
            }
        }
        cout << ans << endl;
    }

}