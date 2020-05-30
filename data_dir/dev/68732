#include<bits/stdc++.h>
#define ll          long long
#define pii         pair<int,int>
#define sf(a)       scanf("%d",&a)
#define pf(a)       printf("%d\n",a)
#define mem(a,b)    memset(a,b,sizeof(a))
#define all(x)      x.begin(),x.end()
#define rall(x)     x.rbegin(),x.rend()
#define pb          push_back
#define F           first
#define S           second
#define Check       cout<< "Done in " << clock() / CLOCKS_PER_SEC <<" sec"<< endl;
#define FastRead    ios_base::sync_with_stdio(false);cin.tie(NULL);
using namespace std;
string s[15],s1[15],t[15],t1[15];
int n;
bool check()
{
    for(int i=0; i<n; i++)
        if(s1[i] != t1[i])
            return false;
    return true;
}
int c;
void ninetyDegree()
{
    for(int i=0;i<n;i++)
        t[i] = t1[i];

    /// 90 Degree Rotation
    //cout << "-------------------" << endl;
    for(int i=0; i<n; i++)
    {
        for(int j=0;j<n;j++)
            t1[i][j] = t[n-j-1][i];
        //cout << t1[i] << endl;
    }
}
bool grandCheck()
{
    ninetyDegree();
    if(check())
        return true;

    ninetyDegree();
    if(check())
        return true;
    ninetyDegree();
    if(check())
        return true;

    return false;
}
bool flip1()
{
    //cerr << "---------------------------" << endl;


    for(int i=0; i<n; i++)
        t[i] = s[i];
    for(int i=0; i<n/2; i++)
        swap(t[i],t[n-i-1]);
    for(int i=0; i<n; i++)
        t1[i] = t[i];
    if(check())
        return true;
    if(grandCheck())
        return true;
    return false;
}
bool flip2()
{
    //cout << "-----------------------\n";
    c = 1;
    for(int i=0; i<n; i++)
    {
        t[i] = s[i] ;
        reverse(all(t[i]));
        //cout << t[i] << endl;
    }
    for(int i=0; i<n; i++)
        t1[i] = t[i];
    if(check())
        return true;
    if(grandCheck())
        return true;
    return false;

}
int main()
{
    cin >> n;
    for(int i=0; i<n; i++)
        cin >> s[i];
    for(int i=0; i<n; i++)
        cin >> s1[i];
    for(int i=0;i<n;i++)
        t1[i] = s[i];
    if(check() || grandCheck() || flip1() || flip2())
        cout << "Yes\n";
    else
        cout << "No\n";
}
