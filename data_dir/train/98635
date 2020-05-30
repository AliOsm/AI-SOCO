#include <bits/stdc++.h>

using namespace std;

const int N = 4e5 + 5;

char buf[N];
int cnt[256];

int main() {
  int n;
  scanf("%d %s", &n, buf);
  for (int i = 0; i < n; i++) cnt[buf[i]]++;
  int ada = 0;
  for (char c = 'a'; c <= 'z'; c++) ada += cnt[c] / 2;
  for (char c = 'A'; c <= 'Z'; c++) ada += cnt[c] / 2;
  for (char c = '0'; c <= '9'; c++) ada += cnt[c] / 2;
  
  for (int len = n; len >= 1; len--) {
    if (n % len) continue;
    int ans_words = n / len;
    int need = len / 2 * ans_words;
    if (need <= ada) {
      vector<string> s(ans_words);
      for (auto& it : s) {
        for (int i = 0; i < len; i++) it.push_back('*');
      }
      if (need > 0) {
        // pointer kata, character
        int p = 0, q = 0;
        for (char c = 'a'; c <= 'z'; c++) {
          while (cnt[c] >= 2 && p < ans_words) {
            s[p][q] = s[p][len - 1 - q] = c;
            q++;
            if (q == len / 2) {
              p++;
              q = 0;
            }
            cnt[c] -= 2;
          }
        }
        for (char c = 'A'; c <= 'Z'; c++) {
          while (cnt[c] >= 2 && p < ans_words) {
            s[p][q] = s[p][len - 1 - q] = c;
            q++;
            if (q == len / 2) {
              p++;
              q = 0;
            }
            cnt[c] -= 2;
          }
        }
        for (char c = '0'; c <= '9'; c++) {
          while (cnt[c] >= 2 && p < ans_words) {
            s[p][q] = s[p][len - 1 - q] = c;
            q++;
            if (q == len / 2) {
              p++;
              q = 0;
            }
            cnt[c] -= 2;
          }
        }
      }
      if (len % 2 == 1) {
        //printf("ans words %d\n", ans_words);
        for (int i = 0; i < ans_words; i++) {
          if (s[i][len / 2] == '*') {
            bool ok = 0;
            for (int c = 'a'; c <= 'z' && !ok; c++) if (cnt[c]) {
              ok = 1;
              cnt[c]--;
              s[i][len / 2] = c;
            }
            for (int c = 'A'; c <= 'Z' && !ok; c++) if (cnt[c]) {
              ok = 1;
              cnt[c]--;
              s[i][len / 2] = c;
            }
            for (int c = '0'; c <= '9' && !ok; c++) if (cnt[c]) {
              ok = 1;
              cnt[c]--;
              s[i][len / 2] = c;
            }
            assert(ok);
          }
        }
      }
      printf("%d\n", ans_words);
      for (auto it : s) printf("%s ", it.c_str());
      return 0;
    }
  }
  assert(0);
  return 0;
}