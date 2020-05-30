#include<bits/stdc++.h>
using namespace std;
int a[12345];
queue<char>q;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL),cout.tie(NULL);
    string s;
    cin >> s;
    int zero = 0, one = 0, two=0,z=0,cnt=0;
    for(int i = s.length()-1; i >= 0; i--)
    {
        if(s[i] == '2')break;
        else if(s[i] == '0')cnt++;
    }
    for(int i = 0; i < s.length(); i++)
    {
        if(s[i] == '0' && two == 0)zero++;
        if(s[i] == '0' && two > 0)z++;
        if(s[i] == '1')one++;
        if(s[i] == '2')
        {
            two++;
            while(z)
            {
                if(z == 0)break;
                q.push('0');
                z--;
            }
            z = 0;
            q.push('2');
        }
    }
    for(int i = 0; i < zero; i++)
    {
      //  cout<<"ZERO"<<endl;
        cout<<"0";
    }
    for(int i =0; i < one; i++)
    {
        //cout<<"ONE"<<endl;
        cout<<"1";
    }
    while(!q.empty())
    {
        //  cout<<"ck"<<endl;
        cout<<q.front();
        q.pop();
    }
    if( two > 0){
    for(int i = 0; i < cnt; i++)
    {
        cout<<"0";
    }
    }
    return 0;
}
