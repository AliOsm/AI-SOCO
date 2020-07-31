#include<bits/stdc++.h>
#define f(i, j, k) for(int i = j; i < k; i++)
#define all(x) x.begin(), x.end()
#define ll long long
using namespace std;

pair<int,pair<int,int> > parent[500][5001];
int main() {

   ios_base::sync_with_stdio(0); cin.tie(0);
   int d, s; cin >> d >> s;
   int INF = 1e9;
    vector<vector<int> > dist(500, vector<int>(5001, INF));
    f(i, 0, 500)f(j, 0, 5001)parent[i][j] = {INF, {INF, INF}};
   queue<int> q;
   q.push(0); q.push(0);
   dist[0][0] = 0;
   while(!q.empty()){
       int mod = q.front(); q.pop();
       int sum = q.front(); q.pop();
       f(put, 0, 10){
           int nxt_mod = (mod * 10 + put) % d;
           int nxt_sum = sum + put;
           if(nxt_sum > s)continue;
           if(dist[nxt_mod][nxt_sum] == INF){
               dist[nxt_mod][nxt_sum] = dist[mod][sum] + 1;
               q.push(nxt_mod);
               q.push(nxt_sum);
               parent[nxt_mod][nxt_sum] = {put, {mod, sum}};
           }
       }
   }

   if(dist[0][s] == INF){
       cout << -1 << "\n";
   }else {
       int mod = 0, sum = s;
       vector<int> digits;
       while(mod != 0 || sum != 0){
           digits.push_back(parent[mod][sum].first);
           int nxt_mod = parent[mod][sum].second.first;
           int nxt_sum = parent[mod][sum].second.second;
           mod = nxt_mod;
           sum = nxt_sum;
       }
       reverse(all(digits));
       f(i, 0, (int)digits.size())cout << digits[i];
       cout << "\n";
   }
}