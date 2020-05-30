#include<bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
using namespace std;

template<typename T>
using ordered_set = __gnu_pbds::tree<T, __gnu_pbds::null_type, less<T>, __gnu_pbds::rb_tree_tag, __gnu_pbds::tree_order_statistics_node_update>;
using ll = long long int;
using i64 = long long int;
#define all(vec) (vec).begin(),(vec).end()
template <typename T> inline void ckmax(T &x, T y) {if (y > x) x = y; }
template <typename T> inline void ckmin(T &x, T y) {if (y < x) x = y; }
#define error(args...) { string _s = #args; replace(_s.begin(), _s.end(), ',', ' '); stringstream _ss(_s); istream_iterator<string> _it(_ss); err(_it, args); }
void err(istream_iterator<string> it) {}
template<typename T, typename... Args>
void err(istream_iterator<string> it, T a, Args... args) {
	cerr << *it << " =: " << a << endl;
	err(++it, args...);
}
template <typename T1, typename T2>
inline std::ostream& operator << (std::ostream& os, const std::pair<T1, T2>& buf) {
    return os << "(" << buf.first << ": " << buf.second << ")";
}
template<typename T>
inline std::ostream &operator << (std::ostream & os,const std::vector<T>& v) {
    bool first = true;
    os << "[";
    for(unsigned int i = 0; i < v.size(); i++) {
        if(!first) os << ", ";
        os << v[i];
        first = false;
    }
    return os << "]";
}
template<typename T>
inline std::ostream &operator << (std::ostream & os,const std::set<T>& v) {
    bool first = true;
    os << "{";
    for (typename std::set<T>::const_iterator ii = v.begin(); ii != v.end(); ++ii) {
        if(!first) os << ", ";
        os << *ii;
        first = false;
    }
    return os << "}";
}
template<typename T1, typename T2>
inline std::ostream &operator << (std::ostream & os,const std::map<T1, T2>& v) {
    bool first = true;
    os << "{";
    for (typename std::map<T1, T2>::const_iterator ii = v.begin(); ii != v.end(); ++ii) {
        if(!first) os << ", ";
        os << *ii ;
        first = false;
    }
    return os << "}";
}
template<typename T>
inline std::ostream &operator << (std::ostream & os,const std::unordered_set<T>& v) {
    return os << std::set<T>(v.begin(), v.end());
}
template<typename T>
inline std::ostream &operator << (std::ostream & os,const std::multiset<T,greater<T>>& v) {
    return os << std::vector<T>(v.begin(), v.end());
}
template<typename T>
inline std::ostream &operator << (std::ostream & os,const ordered_set<T>& v) {
    return os << std::set<T>(v.begin(), v.end());
}
template<typename T1, typename T2>
inline std::ostream &operator << (std::ostream & os,const std::unordered_map<T1, T2>& v) {
    return os << std::map<T1, T2>(v.begin(), v.end());
}

const int MOD = 1e9 + 7;
const long long INF = 1e18;
const double EPS = 1e-6;
/***********************************************************************/
bool isprime(int n) {
    if (n < 2) return false;
    if (n == 2 || n == 3) return true;
    for (int i = 2; i * i <= n; ++i)
        if (n % i == 0) return false;
    return true;
}
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    cin >> n;
    vector<int> masks(60, 0);
    int p = 0;
    for (int i = 2; i < 60; ++i) {
        if (isprime(i)) {
            masks[i] = 1 << p;
            for (int j = i + i; j < 60; j += i)
                masks[j] |= masks[i];
            ++p;
        }
    }
    vector<int> a(n), ans(n, -1);
    for (int &i : a) cin >> i;
    vector<vector<int>> dp(n + 1, vector<int>(1 << p, MOD));
    vector<vector<int>> val(n + 1, vector<int>(1 << p, -1));
    vector<vector<int>> link(n + 1, vector<int>(1 << p, -1));
    dp[0][0] = 0;
    for (int i = 1; i <= n; ++i) {
        for (int k = 1; k < 60; ++k) {
            for (int mask = 0; mask < (1 << p); ++mask) {
                if (masks[k] & mask) continue;
                if (dp[i - 1][mask] + abs(a[i - 1] - k) < dp[i][masks[k] | mask]) {
                    dp[i][masks[k] | mask] = dp[i - 1][mask] + abs(a[i - 1] - k);
                    val[i][masks[k] | mask] = k;
                    link[i][masks[k] | mask] = mask;
                }
            }
        }
    }
    int mn = MOD;
    for (int mask = 0; mask < (1 << p); ++mask) {
        ckmin(mn, dp[n][mask]);
    }
    for (int mask = 0; mask < (1 << p); ++mask) {
        if (mn == dp[n][mask]) {
            int i = n;
            for (; i > 0; --i) {
                ans[i - 1] = val[i][mask];
                mask = link[i][mask];
            }
            break;
        }
    }
    for (int x: ans) cout << x << ' ';
    cout << '\n';

    return 0;
}
