#include <bits/stdc++.h>

using namespace std;

string to_string(char ch) {
    return "'" + string(1, ch) + "'";
}

string to_string(string s) {
    return '"' + s + '"';
}

string to_string(const char *s) {
    return to_string((string) s);
}

string to_string(bool b) {
    return (b ? "true" : "false");
}

template <typename A, typename B>
string to_string(pair<A, B> p) {
    return "(" + to_string(p.first) + ", " + to_string(p.second) + ")";
}

template <size_t N>
string to_string(bitset<N> v) {
    return v.to_string();
}

template <typename A>
string to_string(A v) {
    string res = "{", sep;
    for (const auto x : v) {
        res += sep + to_string(x);
        sep = ", ";
    }
    res += "}";
    return res;
}

void debug_out() { cerr << endl; }

template <typename Head, typename... Tail>
void debug_out(Head H, Tail... T) {
    cerr << " " << to_string(H);
    debug_out(T...);
}

#ifdef LOCAL
#define debug(...) cerr << "[" << #__VA_ARGS__ << "]:", debug_out(__VA_ARGS__)
#else
#define debug(...) 42
#endif

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    int k;
    cin >> k;
    string s;
    cin.ignore();
    getline(cin, s);
    vector<int> markers;
    for (int i = 0; i < (int) s.size(); ++i) {
        if (s[i] == ' ' || s[i] == '-') {
            markers.emplace_back(i);
        }
    }
    int lo = 1, hi = s.size();
    while (lo < hi) {
        int mid = lo + (hi - lo >> 1);
        int take = 0;
        int st = 0;
        while (st < (int) s.size()) {
            ++take;
            int lst = st + mid - 1;
            if (lst + 1 >= (int) s.size()) {
                break;
            }
            int ind = upper_bound(markers.begin(), markers.end(), lst) - markers.begin();
            if (ind == 0) {
                take = INT_MAX;
            } else {
                --ind;
                if (markers[ind] >= st) {
                    st = markers[ind] + 1;
                } else {
                    take = INT_MAX;
                }
            }
            if (take == INT_MAX) {
                break;
            }
        }
        if (take <= k) {
            hi = mid;
        } else {
            lo = mid + 1;
        }
    }
    cout << lo << "\n";
    return 0;
}

