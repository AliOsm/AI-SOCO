#include <bits/stdc++.h>
using namespace std;
#define INF 1<<30
#define MAX 10005
#define FASTIO ios_base::sync_with_stdio(false), cin.tie(0), cout.tie(0);
typedef long long ll;
typedef pair<ll, ll> pi;
int main()
{
    FASTIO
    ///*
    //double start_time = clock();
#ifndef ONLINE_JUDGE
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    freopen("error.txt", "w", stderr);
#endif
    //*/
    ll n,m;
    cin >> n >> m;
    ll dish[n+2], cost[n+2];
    for(int i = 1; i <= n; i++)cin >> dish[i];
    for(int i = 1; i <= n; i++)cin >> cost[i];
        priority_queue<pi, vector<pi>, greater<pi> > PQ; 
        for(int i = 1; i <= n; i++){
            PQ.push({cost[i], i});
        }
        //sort(v.begin(), v.end());
        /*for(int i = 0; i < n; i++){
            pair<int, int> top = PQ.top();
            cerr << top.first << " "<<top.second<<endl;
            PQ.pop();
        }*/
        int cnt = 0;
        while(m--){
            cnt++;
            ll item, item_num;
            ll ans = 0;
            cin >> item >> item_num;
            if(dish[item] >= item_num){
                cout << cost[item]*item_num<<endl;
                dish[item] -= item_num;
               // index[item] = -item_num;
            }
            else{
                //cerr << "value of Index: "<<cnt<<endl;
               // cerr << item << " "<<item_num<<endl;
                ans  += dish[item]*cost[item];
                item_num -= dish[item];
               // cerr << item_num <<"------"<<endl;
                dish[item] = 0;
                bool flag = true;
                while(!PQ.empty()){
                    int idx = PQ.top().second;
                   // cerr << idx<<endl;
                    if(dish[idx] >= item_num){
                        cout << ans + cost[idx]*item_num<<endl;
                        dish[idx] -= item_num;
                        flag = false;
                        break;
                    }
                    else if(dish[idx] > 0){
                        ans += dish[idx]*cost[idx];
                        item_num -= dish[idx];
                       // cerr << item_num<<endl;
                        dish[idx] = 0;
                    }
                    else{
                       // cerr << PQ.top().second<<endl;
                     PQ.pop();
                     }
                 }
                 //if(flag)cout << 0 << endl;

                 if(flag){
                    cout << 0<<endl;
                    for(int k = 1; k <= m; k++)
                        cout << 0 << endl;
                    return 0;
                 }

                }
            }
    //double end_time = clock();
    //printf( "Time = %lf ms\n", ( (end_time - start_time) / CLOCKS_PER_SEC)*1000);

    return 0;
} 