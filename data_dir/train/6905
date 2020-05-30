#include<bits/stdc++.h>

using namespace std;

typedef long long LL;
typedef unsigned long long uLL;
typedef long double ldb;
typedef pair<int,int> pii;
typedef pair<LL,LL> pll;

#define root(x) ((x.second-x.first)/2LL+x.first)

int main()
{
    ios_base::sync_with_stdio(0);cin.tie(0);
    LL n, q;
    cin>>n>>q;
    LL u;
    string s;
    while(q--)
    {
        cin>>u>>s;
        stack<pll> st;
        st.emplace(1, n);
        while(root(st.top()) != u)
        {
            if(u<root(st.top()))
                st.emplace(st.top().first, root(st.top())-1LL);
            else
                st.emplace(root(st.top())+1LL, st.top().second);
        }
        for(char c:s)
        {
            if(c == 'U')
            {
                if(st.size()>1)
                    st.pop();
            }
            else if(c == 'L')
            {
                if(st.top().first != st.top().second)
                    st.emplace(st.top().first, root(st.top())-1LL);
            }
            else if(st.top().first != st.top().second)
                st.emplace(root(st.top())+1LL, st.top().second);
        }
        cout<<root(st.top())<<'\n';
    }
    return 0;
}
