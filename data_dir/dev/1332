#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define clr(a,b) memset(a,b,sizeof(a))
#define all(v) ((v).begin()),((v).end())
#define fastIO ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr), cout << fixed << setprecision(0)
double const EPS = 1e-8, PI = acos(-1);
const int N = 2e6 + 9, OO = 1e9, v = 1e6;

bool primes[1001];
vector<int> prime;

void sieve() {
  int mxx = 1001;
  primes[0] = primes[1] = 1;
  for (int i = 2; i*i <= mxx; ++i) {
    for (int j = i * i; j <= mxx; j += i)
      primes[j] = 1;
  }
  for (int i = 0; i < mxx; ++i) {
    if(!primes[i])
      prime.push_back(i);
  }
}

set<int> st[1001];
int ff[1001], arr[26];

int main() {
  fastIO;
//  freopen("input.in", "rt", stdin); // freopen("output.in", "wt", stdout);
  sieve();
  string str;
  cin >> str;
  int n = str.size();
  for (int i = 0; i < n; ++i)
    ++arr[str[i] - 'a'];
  priority_queue<pair<int, char>> q;
  for (int i = 0; i < 26; ++i)
    if(arr[i])
      q.push({arr[i], i + 'a'});

  iota(ff, ff+1001, 0);
  for(int pr: prime) {
    if(pr > n)
      break;
    int lps = n / pr;
    for (int i = 1; i <= lps; ++i) {
      st[ff[pr]].insert(i * pr);
      if(!primes[i])
        ff[i] = ff[pr];
    }
  }
  vector<pair<int, int>> vec;
  st[1].insert(1);
  vec.push_back({1, 1});

  for(int pr: prime) {
    if(pr > n)
      break;
    if(st[pr].size() == 0)
      continue;
    vec.push_back({st[pr].size(), pr});
  }
  sort(vec.rbegin(), vec.rend());
  string ans(n, 'a');
  for(auto it: vec) {
    if(q.empty()) {
      cout << "NO\n";
      return 0;
    }
    auto tp = q.top();
    q.pop();
    if(tp.first < it.first) {
      cout << "NO\n";
      return 0;
    }
    tp.first -= it.first;
    if(tp.first)
      q.push(tp);
    for(int el: st[it.second])
      ans[el-1] = tp.second;
  }
  cout << "YES\n";
  cout << ans;
  return 0;
}
