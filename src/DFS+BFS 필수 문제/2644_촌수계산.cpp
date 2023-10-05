/*

bfs를 이용한 cnt:

visited 배열에 cnt를 저장

*/
#include<iostream>
#include<vector>
#include<queue>
#define MAX 101
using namespace std;


int bfs(int s, int d, vector<int> graph[], int visited[])
{   
    queue<int> q;
    q.push(s);

    while(!q.empty())
    {
        int x = q.front();
        q.pop();

        for(int i=0; i<graph[x].size(); i++)
        {
            int nx = graph[x][i];
            if(!visited[nx])
            {
                q.push(nx);
                visited[nx] = visited[x]+1;
            }
            if(nx == d)
            {
                cout << visited[nx] << endl;
                exit(0);
            }
        }
    }

    return -1;
}
int main()
{
    int n, p1, p2, m;
    cin >> n >> p1 >> p2 >> m;

    int visited[MAX] = {0, };
    vector<int> graph[MAX];
    for(int i=0; i<m; i++)
    {
        int u,v;
        cin >> u >> v;
        graph[u].push_back(v);
        graph[v].push_back(u);
    }

    bfs(p1, p2,graph, visited);
    cout << -1 << endl;


}