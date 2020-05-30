    #include <bits/stdc++.h>
    #include <bitset>
    
    #define REP(i,n) for(int i=0;i<(int)n;i++)
    #define REP1(i,j,n) for(int i=j;i<(int)n;i++)
    #define pb(x) push_back(x)
    #define fi first
    #define se second
    #define all(x) x.begin(),x.end()
    #define double long double
    #define mp(x,y) make_pair(x,y)
    
    typedef long long ll;
    
    using namespace std;
    
    
    const int N=1e6;
    bool rem[N];
    queue<int>pos[26];
    int n,k;
    
    int main(){
        ios_base::sync_with_stdio(0);
        cin.tie(0);
    
    
        cin>>n>>k;
        string s;
        cin>>s;
        REP(i,s.length())pos[s[i]-'a'].push(i);
        int c=0;
        REP(i,k){
            while(!pos[c].size())c++;
            rem[pos[c].front()]=1;
            pos[c].pop();
        }
        REP(i,s.size())if(!rem[i])cout<<s[i];
        cout<<"\n";
    
    }