#include <bits/stdc++.h>

using namespace std;
typedef long long ll;
typedef pair<int, int> pi;

void dfs(vector<vector<int> > & g, vector<bool> & vst, int r) {
  vst[r] = true;
  for (int x: g[r]) {
    if (!vst[x]) dfs(g, vst, x);
  }
}
int main() {
  ios_base::sync_with_stdio(false); cin.tie(NULL); cout.precision(20);
  int t; 
  cin >> t;
  while (t--) {
    int n, m; 
    cin >> n >> m;
    vector<vector<int> > g1(n), g2(n);
    for (int i = 0; i < m; i++) {
      int x, y;
      cin >> x >> y;
      x--; y--;
      g1[y].push_back(x);
      g2[x].push_back(y);
    }
    vector<bool> vst1(n,false), vst2(n, false);
    vector<int> jury,cats;
    dfs(g1, vst1, 0);
    for (int i = 0; i <n; i++) {
      if (vst1[i]) cats.push_back(i);
      else jury.push_back(i);
    }
    if (jury.size() > 0 and cats.size() > 0) {
      cout << "Yes\n";
      cout << jury.size() << " " << cats.size() << "\n";
      for (int x: jury)
        cout << x+1 << " ";
      cout << "\n";
      for (int x: cats)
        cout << x+1 << " ";
      cout << "\n";
      continue;
    }
    
    cats.clear();
    jury.clear();
    dfs(g2, vst2, 0);
    for (int i = 0; i <n; i++) {
      if (vst2[i]) jury.push_back(i);
      else cats.push_back(i);
    }
    if (jury.size() > 0 and cats.size() > 0) {
      cout << "Yes\n";
      cout << jury.size() << " " << cats.size() << "\n";
      for (int x: jury)
        cout << x+1 << " ";
      cout << "\n";
      for (int x: cats)
        cout << x+1 << " ";
      cout << "\n";
    }
    else cout << "No\n";
    
  }
}

