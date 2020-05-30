#include <bits/stdc++.h>
using namespace std;
#define popCnt(x) (__builtin_popcountll(x))
typedef long long Long;
typedef unsigned long long ULong;

const int N = 3e5 + 5;

string all = "ACGT";

vector<array<string, 2>> combs;

void buildCombs() {
  for (int mask = 0; mask < (1 << all.size()); ++mask) {
    string a, b;
    for (int j = 0; j < all.size(); ++j) {
      if ((mask >> j) & 1) {
        a += all[j];
      } else {
        b += all[j];
      }
    }
    if (a.size() != 2) continue;
    combs.push_back( { a, b });
    combs.push_back( { b, a });
  }
}

int n, m;
string grid[N];
string rotated[N];

string build(const string& p, bool b) {
  string res;
  for (int i = 0; i < m; ++i) {
    res += p[(i & 1) ^ b];
  }
  return res;
}

int getDiff(const string& s1, const string& s2) {
  int res = 0;
  for (int i = 0; i < s1.size(); ++i) {
    res += (s1[i] != s2[i]);
  }
  return res;
}

bool rot;
int res = INT_MAX;
array<string,2> best_comb;
bool best_rot;

void solve() {
  for (auto& comb : combs) {
    int tmp = 0;
    for (int i = 0; i < n; ++i) {
      string s1 = build(comb[i & 1], true);
      string s2 = build(comb[i & 1], false);
      tmp += min(getDiff(s1, grid[i]), getDiff(s2, grid[i]));
    }
    if (tmp < res) {
      res = tmp;
      best_comb = comb;
      best_rot = rot;
    }
  }
}

void rotate() {
  rot = true;
  for (int i = 0; i < m; ++i) {
    rotated[i].clear();
    rotated[i].resize(n);
    for (int j = 0; j < n; ++j) {
      rotated[i][j] = grid[j][i];
    }
  }
  swap(n, m);
  for (int i = 0; i < n; ++i) {
    grid[i] = rotated[i];
  }
}

int main() {
  ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0);
#ifdef Local
  freopen("test.in", "r", stdin);
#else
#define endl '\n'
#endif

  buildCombs();

  cin >> n >> m;

  for (int i = 0; i < n; ++i) {
    cin >> grid[i];
  }
  solve();
  rotate();
  solve();

  vector<string> v;

  if (!best_rot) {
    rotate();
  }

  for (int i = 0; i < n; ++i) {
    string s1 = build(best_comb[i & 1], true);
    string s2 = build(best_comb[i & 1], false);
    int t1 = getDiff(s1, grid[i]);
    int t2 = getDiff(s2, grid[i]);

    if (t1 < t2) {
      v.push_back(s1);
    } else {
      v.push_back(s2);
    }
  }

  if (!best_rot) {
    for (auto& s : v) {
      cout << s << endl;
    }
    return 0;
  }
  for (int i = 0; i < m; ++i) {
    for (int j = 0; j < n; ++j) {
      cout << v[j][i];
    }
    cout << endl;
  }

}
