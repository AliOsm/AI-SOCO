#include<bits/stdc++.h>

using namespace std;

#define F first
#define S second
#define FOR(i,j,k) for(int i=j;i<=k;i++)
#define REV(i,j,k) for(int i=j;i>=k;i--)
#define MAX 200010
#define ba 31
#define LL unsigned long long
typedef pair<LL,LL> PR;

string str, pre;
LL n, bits[MAX], m;
LL has[2][MAX], mul[2][MAX], bag[2][MAX];
LL M[] = {1000000007, 141650939};
LL bm(LL n, LL p, LL m)
{
    if(p == 0) return 1;
    if(p == 1 || n == 1) return n % m;

    LL ret = bm(n, p/2, m);
    ret = (ret * ret) % m;
    if(p % 2) ret = (ret * n) % m;
    return ret%m;
}

LL modinv( LL n, LL p )
{
    return bm( n, p-2, p );
}

void dude(int ck)
{
    mul[ck][0] = 1;
    bag[ck][0] = modinv(mul[ck][0], M[ck]);
    FOR(i,1,n-1)
    {
        mul[ck][i] = mul[ck][i - 1] * ba;
        mul[ck][i] %= M[ck];
        if(i == 1) bag[ck][i] = modinv(mul[ck][i], M[ck]);
        else  bag[ck][i] = (bag[ck][i-1] * bag[ck][1]) % M[ck];
    }
}

void info()
{
    FOR(ck,0,1)
    {
        dude(ck);
        LL c = 0;
        FOR(j,0,n-1)
        {
            c += (LL)bits[j] * mul[ck][j];
            c %= M[ck];
            has[ck][j] = c;
        }
    }
}

PR ran(LL l,LL r)
{
    LL ret = has[0][r] + M[0];
    if(l) ret -= has[0][l - 1]; ret %= M[0];
    ret *= bag[0][l]; ret %= M[0];

    LL po = has[1][r] + M[1];
    if(l) po -= has[1][l - 1]; po %= M[1];
    po *= bag[1][l]; po %= M[1];

    return make_pair(ret, po);
}

PR hashVal(string str)
{
    PR ret;
    int n = str.size();

    FOR(ck,0,1)
    {
        LL c = 0;
        FOR(j,0,n-1)
        {
            LL v = str[j] - 'a'; v++;
            c += (LL)v * mul[ck][j]; ///age info call naah hole mul[][] always 0 thakbe
            c %= M[ck];
        }
        if(!ck) ret.F = c;
        else ret.S = c;
    }
    return ret;
}


PR reverseRan(int l,int r)
{
    return ran(n - r - 1, n - l - 1);
}

int isPalin(int l,int r)
{
    if(ran(l, r) == reverseRan(l, r)) return 1;
    return 0;
}

int centerPoint(int p1,int p2)
{
    int st = 0, en = min(p1, (int)m - (p2 + 1)), mid;

    while(st <= en)
    {
        mid = (st + en)>>1;
        if(isPalin(p1 - mid, p2 + mid)) st = mid + 1;
        else en = mid - 1;
    }

    if(p1 == p2) return 2*st - 1;
    else return 2*st;
}

int cnt[MAX], fc[MAX], val[MAX];
string text;
int lps[MAX];

void make_lps(string pattern)
{
    int n = pattern.size();

    lps[0] = lps[1] = 0;
    FOR(i,2,n)
    {
        int p = lps[i-1];

        while(true)
        {
            if(pattern[i - 1] == pattern[p])
            {
                lps[i] = p + 1;
                break;
            }

            if(p == 0) break;
            else p = lps[p];
        }
    }

}

int main()
{
    ios::sync_with_stdio(false);
    ///freopen("in.txt", "r", stdin);
    int l, r, x;

   /// cin >> n;
    cin >> str;
    text = str;
    pre = str; reverse(pre.begin(), pre.end());
    str += pre;

    n = str.size(); m = n / 2;
    ///cout << str << endl;
    FOR(i,0,n-1)
    {
        LL x = str[i] - 'a'; x++;
        bits[i] = x;
    }
    info();

    int prin = 0, pos;
    FOR(i,0,m-1)
    {
        x = centerPoint(i, i);
        int st = (i - x/2);
        cnt[st] = max(cnt[st], x);
    }

    int v = 0;
    FOR(i,0,m-1)
    {
        v = max(v, cnt[i]);
        cnt[i] = v;
        v -= 2;
    }

    string pat = string(text.rbegin(), text.rend()) + "#" + text;
    ///cout << pat << endl;
    make_lps( pat );

    memset(fc, -1, sizeof(fc));
    int sz = text.size();

    FOR(i,0,text.size()-1)
    {
        int p = sz + i + 1;

        if(lps[p + 1])
            if(fc[ lps[p + 1] ] == -1) fc[ lps[p + 1] ] = i;
    }

    FOR(i,1,text.size()-1)
        if(fc[i] != -1) val[ fc[i] ] = i;

    prin = 0;
    int c = 0, k = 0;
    l = 0; m = 0;

    FOR(i,0,text.size()-1)
    {
        ///cout << i << ' ' << cnt[i] << ' ' << c << endl;
        int x = cnt[i], y = i + x;
        if(x)
        {
            int v = x + min(sz - y, c)*2;
            if(prin < v)
            {
                l = min(sz - y, c);
                prin = v;
                m = i + 1;
            }
        }

        c = max(c, val[i]);
    }
    if(l == 0)cout << 1 << endl << m << ' ' << prin << endl;
    else cout << 3 << endl
        << fc[l] - l + 2 << ' ' << l << endl
        << m << ' ' << prin - l*2  << endl
        << sz - l + 1 << ' ' << l << endl;

    return 0;
}

