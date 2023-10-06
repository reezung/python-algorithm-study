/*
    vector의 최댓값, 최솟값:
    #include<algorithm>
    *max_element(v.begin(), v.end())
    *max_element(v.begin(), v.end())
*/
#include<iostream>
#include<queue>
#include<vector>
#include<algorithm>
#define MAX 500
using namespace std;

int n, m;

int bfs(int x, int y, int cnt, int graph[MAX][MAX])
{
    queue<pair<int,int>> q;
    q.push({x, y});
    graph[x][y] = 0;
    cnt++;

    int dx[4] = {-1, 1, 0, 0};
    int dy[4] = {0, 0, -1, 1};

    while(!q.empty())
    {
        pair<int,int> loc = q.front();
        q.pop();

        for(int i=0; i<4; i++)
        {
            int nx = loc.first + dx[i];
            int ny = loc.second + dy[i];

            if(nx >= 0 && nx < n && ny >= 0 && ny < m)
            {
                if(graph[nx][ny]==1)
                {
                    q.push({nx, ny});
                    graph[nx][ny] = 0;
                    cnt++;
                }
            }
        }
    }

    return cnt;
}

int main()
{
    int graph[MAX][MAX];
    vector<int> ans;
    cin >> n >> m;
    for(int i=0; i<n; i++)
    {
        for(int j=0; j<m; j++)
        {
            cin >> graph[i][j];
        }
    }

    for(int i=0; i<n; i++)
    {
        for(int j=0; j<m; j++)
        {
            if(graph[i][j] == 1)
            {
                ans.push_back(bfs(i,j,0,graph));
            }
        }
    }
    cout << ans.size() << endl;
    if(ans.empty())
    {
        cout << 0 << endl;
    }
    else
    {
        cout << *max_element(ans.begin(), ans.end()) << endl;
    }
}