#include<bits/stdc++.h>
using namespace std;

int res[101];

struct ank
{
    int ques, exam, prep, ID;
    ank(int ques, int exam, int prep,int ID)
        : ques(ques), exam(exam), prep(prep), ID(ID)
    {
    }
};

struct cmp
{
    bool operator()(ank const& a, ank const& b)
    {
        if(a.ques == b.ques) return a.exam > b.exam;
        return a.ques > b.ques;
    }
};
struct cmp2
{
    bool operator()(ank const& a, ank const& b)
    {
        return a.exam > b.exam;
    }
};

priority_queue<ank, vector<ank>, cmp>PQ;
priority_queue<ank, vector<ank>, cmp2>ans;

int main()
{
   // freopen("in.txt", "r", stdin);
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    int n, m;
    cin >> n >> m;
    int mx = 0;
    int dif = n - m;
    int day = 1;
    vector<int>Exam;
    map<int,bool> mp, ck;
    for(int i = 1; i <= m; i++)
    {
        int s,d,c;
        cin >> s >> d >> c;
        mx += c;
        Exam.push_back(d);
        mp[d] = true;
        PQ.push(ank(s,d,c,i));
    }
    int time = 0;
    int cnt = 0;
    while(!PQ.empty())
    {
        auto x = PQ.top();
        int s = x.ques;
        int d = x.exam;
        int c = x.prep;
        int yd = x.ID;
        //cout << x.ques << " "<<x.exam << " "<<x.prep << " "<<x.ID<<endl;
        PQ.pop();
        while(!ans.empty())
        {
            int flag = 0;
            auto y = ans.top();
            int p = y.ques;
            int q = y.exam;
            int r = y.prep;
            int id = y.ID;
            ans.pop();
            day = min(day, p);
            //cout << y.ques << " **  "<<y.exam << " **  "<<y.prep << " ** "<<y.ID<<endl;
           // cout << day << "~~~~~~~~~~~~~"<<s<<endl;
            while( day < s && r > 0)
            {
                if(day >= q)
                {
                   // cout << "here--------------------------------------------\n";
                    flag = 1;
                    break;
                }
                if(p > day || mp[day] == true || res[day] > 0)
                {
                    day++;
                    continue;
                }
                res[day]  = id;
               // cout << res[day] << "------"<<day << " ----- "<<r <<  endl;
                r--;
                day++;
                flag = 1;
            }
            if(r > 0) ans.push(ank(p,q,r,id));
            if(flag) break;
            if(day >= s || r <= 0) break;
        }
        ans.push(ank(s,d,c,yd));
    }

    while(!ans.empty())
    {
        int flag = 0;
        auto y = ans.top();
        int p = y.ques;
        int q = y.exam;
        int r = y.prep;
        int id = y.ID;
        ans.pop();
        day = min(day, p);
        while( day < q && r > 0)
        {
            if(day >= q) break;
            if(p > day || mp[day] == true || res[day] > 0)
            {
                day++;
                continue;
            }
            res[day]  = id;
            r--;
            // cout << res[day] << "---&&&---"<<day << endl;
            day++;
        }
        // cout << y.ques << " &&  "<<y.exam << " &&  "<<r << " && "<<y.ID<<endl;
        if(r > 0)
        {
           // cout << day << " % ";
            //cout << y.ques << " %  "<<y.exam << " %  "<<r << " % "<<y.ID<<endl;
            cout << "-1\n";
            return 0;
        }
    }
    for(auto x: Exam)
    {
        res[x] = m+1;
    }
//    int nt = 0;
//    for(int i = 1; i <= n; i++)
//    {
//       if(res[i] == 0 || res[i] == m+1) continue;
//        if(ck[res[i]] == false)
//        {
//            nt++;
//            ck[res[i]] = true;
//            cout << res[i] << " ";
//        }
//    }
//    cout << nt << endl;
//    if(nt < m)
//   {
//        //cout << "-1\n";
//        return 0;
//    }
    for(int i = 1; i <= n; i++)
    {
        cout << res[i] << " ";
    }
    return 0;
}

