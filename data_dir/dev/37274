#include <bits/stdc++.h>
using namespace std;
#define popCnt(x) (__builtin_popcountll(x))
typedef long long Long;
typedef long double Double;

const int N = 70000 + 5;

enum TestType {
  REGULAR = 0, EXAMPLE = 1, EMPTY = 2,
};

int r;
struct Hasher {
  int operator()(const string& s) const {
    hash<string> h;
    return h(s) ^ r;
  }
};

struct File {
  string name = "";
  TestType type = EMPTY;
};

File& getFile(const string& name) {
  static unordered_map<string, File, Hasher> file;
  File& res = file[name];
  if (res.name.empty()) res.name = name;
  return res;
}

string tmp;

vector<pair<string, string>> moves;
vector<pair<string, int>> v;
int n, e = 0;

vector<string> opp[2];

unordered_set<string, Hasher> non_opp[2];

vector<string> empty[2];

void build() {
  for (int type = 0; type < 2; ++type) {
    int start, end;
    if (type == REGULAR) {
      start = e + 1, end = n;
    } else {
      start = 1, end = e;
    }

    for (int i = start; i <= end; ++i) {
      string s = to_string(i);

      non_opp[REGULAR].erase(s);
      non_opp[EXAMPLE].erase(s);

      if (getFile(s).type == EMPTY) {
        empty[type].push_back(s);
      }
      if (getFile(s).type == (type ^ 1)) {
        opp[type ^ 1].push_back(s);
      }
    }
  }
}

void move_files(File& file1, File& file2) {
  file2.type = file1.type;
  file1.type = EMPTY;
  moves.emplace_back(file1.name, file2.name);
}

void move_files(const string& file1, const string& file2) {
  move_files(getFile(file1), getFile(file2));
}

int main() {
  ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0);
#ifdef Local
  freopen("test.in", "r", stdin);
#else
#define endl '\n'
#endif

  srand(time(0));
  r = rand();

  cin >> n;

  v.resize(n);

  for (auto& p : v) {
    cin >> p.first >> p.second;
    e += (p.second == EXAMPLE);

    non_opp[p.second].insert(p.first);

    getFile(p.first).type = (TestType) p.second;
  }

  build();
  tmp = to_string(n + 1);

  while (true) {
    bool changed = false;
    for (int type = 0; type < 2; ++type) {
      if (empty[type].empty()) continue;
      changed = true;

      string new_name = empty[type].back(), old_name;
      empty[type].pop_back();

      if (opp[type].empty()) {
        assert(!non_opp[type].empty());
        old_name = *non_opp[type].begin();
        non_opp[type].erase(non_opp[type].begin());
      } else {
        old_name = opp[type].back();
        opp[type].pop_back();
        empty[type ^ 1].push_back(old_name);
      }

      move_files(old_name, new_name);
    }

    if (!changed) {
      if (opp[EXAMPLE].empty()) break;
      move_files(opp[EXAMPLE].back(), tmp);
      empty[REGULAR].push_back(opp[EXAMPLE].back());
      opp[EXAMPLE].pop_back();
      non_opp[EXAMPLE].insert(tmp);
    }
  }

  cout << moves.size() << endl;

  for (auto& p : moves) {
    cout << "move " << p.first << ' ' << p.second << endl;
  }

}

