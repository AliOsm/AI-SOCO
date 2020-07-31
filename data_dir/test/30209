#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define clr(a,b) memset(a,b,sizeof(a))
#define all(v) ((v).begin()),((v).end())
#define read freopen("input.in", "rt", stdin);
#define write freopen("output.in", "wt", stdout);
#define fastIO cout << fixed << setprecision(12), ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
double const EPS = 1e-8, PI = acos(-1);
const int N = 1e6 + 9, OO = 1e9;

int freq[N];
bool arr[N];
stack<int> st;
bool valid(char c, char cc) {
  return (c == ')' && cc == '(') || (c == ']' && cc == '[');
}

int main() {
  fastIO;
  string str;
  cin >> str;
  int n = str.size();
  for (int i = 0; i < n; ++i) {
    freq[i] += (str[i] == '[');
    if(i)
    freq[i] += freq[i-1];
    if(str[i] == '(' || str[i] == '[')
    st.push(i);
    else if(!st.empty() && valid(str[i], str[st.top()])) {
      arr[i] = arr[st.top()] = 1;
      st.pop();
    } else {
      while(!st.empty())
      st.pop();
    }
  }
  int start = 0,
  end = 0, len;
  int mx = 0, finalStart, finalEnd;
  bool en = 0;
  for (int i = 0; i < n; ++i) {
    if (arr[i]) {
      end = i;
      if (!en)
        start = i;
      en = 1;
    } else {
      if (!en)
        continue;
      len = freq[end];
      if (start)
        len -= freq[start - 1];
      if (len > mx)
        mx = len, finalEnd = end, finalStart = start;
      en = 0;
    }
  }
  if (start != -1) {
    if (en) {
      len = freq[end];
      if (start)
        len -= freq[start - 1];
      if (len > mx)
        mx = len, finalEnd = end, finalStart = start;
    }
  }
//  if(finalEnd == finalStart)
  cout << mx << '\n';
  if (!mx)
    finalEnd = -2;
  for (; finalStart <= finalEnd; finalStart++)
    cout << str[finalStart];
  return 0;
}
