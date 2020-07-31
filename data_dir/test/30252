#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <functional>
#include <utility>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstdio>
#include <stack>

using namespace std;

#define REP(i,n) for((i)=0;(i)<(int)(n);(i)++)
#define foreach(c,itr) for(__typeof((c).begin()) itr=(c).begin();itr!=(c).end();itr++)

char buf[100010];
string s,t;
int dp[100010],pre[100010],rad[100010];
pair <int, int> premax[100010]; // id, len

void failure(void){
    int N=t.length(),i,j;
    dp[0] = -1;
    for(i=1;i<=N;i++){
        for(j=dp[i-1];j>=0;j=dp[j]) if(t[j] == t[i-1]) break;
        dp[i] = j + 1;
    }
}

void kmp(void){
    int N=s.length(),i,j=0;
    REP(i,N){
        while(j == t.length() || (j >= 0 && s[i] != t[j])) j = dp[j];
        j++;
        pre[i+1] = j;
    }
}

void manacher(void){
    int N=s.length(),L=-1,R=-1,i;
    REP(i,N){
        int tmp = 0;
        if(i <= R) tmp = min(R-i,rad[L+R-i]);
        while(i-tmp-1 >= 0 && i+tmp+1 < N && s[i-tmp-1] == s[i+tmp+1]) tmp++;
        rad[i] = tmp;
        if(i+tmp > R) {R = i+tmp; L = i-tmp;}
    }
}

int main(void){
    int i;
    
    scanf("%s",buf);
    s = t = buf;
    int N = s.length();
    reverse(t.begin(),t.end());
    
    failure(); kmp(); manacher();
    
    premax[0] = make_pair(0,0);
    for(i=1;i<=N;i++){
        premax[i] = premax[i-1];
        if(pre[i] > premax[i].second) premax[i] = make_pair(i,pre[i]);
    }
    
    int ans = 0;
    vector <pair <int, int> > ansv;
    
    REP(i,N){
        int L = i-rad[i], R = i+1+rad[i];
        int len = min(premax[L].second,N-R);
        int tmp = R-L + 2*len;
        if(tmp > ans){
            ans = tmp;
            ansv.clear();
            ansv.push_back(make_pair(premax[L].first-premax[L].second,len));
            ansv.push_back(make_pair(L,R-L));
            ansv.push_back(make_pair(N-len,len));
        }
    }
    
    cout << ((ansv[0].second == 0) ? 1 : 3) << endl;
    REP(i,3) if(ansv[i].second > 0) cout << ansv[i].first + 1 << ' ' << ansv[i].second << endl;
    
    return 0;
}
