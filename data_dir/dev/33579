#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define ull unsigned long long
#define clr(a,b) memset(a,b,sizeof(a))
#define all(v) ((v).begin()),((v).end())
void debug() {
#ifndef ONLINE_JUDGE
  freopen("input.in", "rt", stdin);
//  freopen("output.txt", "wt", stdout);
#endif
  cout << fixed << setprecision(0);
  ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
}
double const EPS = 1e-8, PI = acos(-1);
const int N = 5e5 + 9, OO = 1e9;

vector<int> diff = { 4, 8, 15, 16, 23, 42 };
vector<int> vec;
int main() {
  debug();
  int total;
  string str = "";
  for (int i = 2; i < 6; ++i) {
    str = "? " + to_string(1) + " " + to_string(i);
    cout << str << endl;
    getline(cin, str);
    total = stoi(str);
    vec.push_back(total);
  }
  for (int j = 0; j < 6; ++j) {
    vector<int> vv;
    for (int i = 0; i < 4; ++i) {
      if(vec[i] % diff[j] == 0 && find(all(diff), vec[i] / diff[j]) != diff.end()) {
        vv.push_back(vec[i] / diff[j]);
      }
    }
    if(vv.size() != 4)
      continue;
    cout << "! " << diff[j];
    for(int it: vv)
      cout << " " << it;
    vv.push_back(diff[j]);
    for (int j = 0; j < 6; ++j) {
      if(find(all(vv), diff[j]) == vv.end()) {
        cout << " " << diff[j];
        break;
      }
    }
    break;
  }
  return 0;
}
