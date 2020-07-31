#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>
#include <unordered_map>
#include <cmath>
#define N 1000002
using namespace std;
typedef long long ll;
const ll mod = 1000000007LL;
ll n;
ll f1, f2, f3;
ll c;
ll getpw(ll a, ll b) {
  ll res=1LL;
  while(b) {
    if (b&1) res=res*a%mod;
    a=a*a%mod;
    b/=2;
  }
  return res;
}
ll getpc() {
  if (n<=3) return 0;
  if (n==4) return 2;
  if (n==5) return 6;
   ll a1[5] = {6,2,0,0,0};
   ll b1[5][5] = {{3+mod-1,-2+mod-1,mod-1,-1+mod-1,1+mod-1}, {1+mod-1,mod-1,mod-1,mod-1,mod-1}, {mod-1,1+mod-1,mod-1,mod-1,mod-1}, {mod-1,mod-1,1+mod-1,mod-1,mod-1}, {mod-1,mod-1,mod-1,1+mod-1,mod-1}};
  // ll a1[5] = {0,0,0,1,1};
  // ll b1[5][5] = {{1,1,1,2,0},{1,0,0,0,0},{0,1,0,0,0},{0,0,0,1,1},{0,0,0,0,1}};
  ll b = n-5;
  while(b) {
    if (b&1) {
      ll res[5]={0,0,0,0,0};
      for (int i = 0; i < 5; ++i) {
        for (int j = 0; j < 5; ++j) {
          res[i] = (res[i]+b1[i][j]*a1[j]%(mod-1LL))%(mod-1LL);
        }
      }
      for (int i = 0; i < 5; ++i) {
        a1[i] = res[i];
      }
    }
    ll c[5][5]={{0,0,0,0,0},{0,0,0,0,0},{0,0,0,0,0},{0,0,0,0,0},{0,0,0,0,0}};
    for (int i = 0; i < 5; ++i) {
      for (int j = 0; j < 5; ++j) {
        for (int k = 0; k < 5; ++k) {
          c[i][j] = (c[i][j]+b1[i][k]*b1[k][j]%(mod-1LL)) % (mod-1LL);
        }
      }
    }
    for (int i = 0; i < 5; ++i) {
      for (int j = 0; j < 5; ++j) {
        b1[i][j] = c[i][j];
      }
    }
    b /= 2;
  }
  return a1[0];
}
ll getpf(int x) {
  if (x==1) {
    if (n==1) return 1;
    if (n==2) return 0;
    if (n==3) return 0;
  } else if (x==2) {
    if (n==1) return 0;
    if (n==2) return 1;
    if (n==3) return 0;
  } else {
    if (n==1) return 0;
    if (n==2) return 0;
    if (n==3)return 1;
  }
  ll a1[3] = {0,0,0};
  if (x==1) a1[2] = 1;
  if (x==2) a1[1] = 1;
  if (x==3) a1[0] = 1;
  ll b1[3][3] = {{1,1,1},{1,0,0},{0,1,0}};
  ll b = n-3;
  while(b) {
    if (b&1) {
      ll res[3]={0,0,0};
      for (int i = 0; i < 3; ++i) {
        for (int j = 0; j < 3; ++j) {
          res[i] = (res[i]+b1[i][j]*a1[j]%(mod-1LL))%(mod-1LL);
        }
      }
      for (int i = 0; i < 3; ++i) {
        a1[i] = res[i];
      }
    }
    ll c[3][3]={{0,0,0},{0,0,0},{0,0,0}};
    for (int i = 0; i < 3; ++i) {
      for (int j = 0; j < 3; ++j) {
        for (int k = 0; k < 3; ++k) {
          c[i][j] = (c[i][j]+b1[i][k]*b1[k][j]%(mod-1LL)) % (mod-1LL);
        }
      }
    }
    for (int i = 0; i < 3; ++i) {
      for (int j = 0; j < 3; ++j) {
        b1[i][j] = c[i][j];
      }
    }
    b /= 2;
  }
  return a1[0];
}
int main() {
  cin>>n>>f1>>f2>>f3>>c;
  ll pc = getpc();
  ll p1 = getpf(1);
  ll p2 = getpf(2);
  ll p3 = getpf(3);
  ll ans = getpw(c, pc);
  ans = ans*getpw(f1, p1)%mod;
  ans = ans*getpw(f2, p2)%mod;
  ans = ans*getpw(f3, p3)%mod;
  cout<<ans<<endl;
  return 0;
}
