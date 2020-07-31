#include<bits/stdc++.h>
using namespace std;
int main()
{
    long long n;
    cin >> n;
    vector<pair<long long,long long> >v;
    for(long long i = 1; i <= 2*n; i++){
        long long x;
        cin >> x;
        v.push_back({x, i});
    }
    long long shasha  = 1, dima = 1;
    sort(v.begin(), v.end());
   // for(long long i = 0; i < 2*n; i++){
       // cout << v[i].first << " "<<v[i].second<<endl;
    //}
    long long ans = 0;
    long long i = 0;
       while(i < 2*n){
            long long first = v[i].second;
            long long sec = v[i+1].second;
            i += 2;
           // cout << first << " "<<sec<<endl;
            long long s1 = abs(first - shasha);
            long long d1 = abs(first - dima);
            long long s2 = abs(sec - shasha);
            long long d2 = abs(sec - dima);
            if((s1+d2) < (s2+d1)){
                ans += (s1 + d2);
                shasha = first;
                dima = sec;
//                if(shasha < first)shasha += s1;
//                else if(shasha > first) shasha -= s1;
//                if(dima < sec)shasha += d2;
//                else if(dima > sec) dima -= d2;
            }
            else{
                ans += (s2 + d1);
                shasha = sec;
                dima = first;
//                 if(shasha < sec)shasha += s2;
//                else if(shasha > sec) shasha -= s2;
//                if(dima < first)shasha += d1;
//                else if(dima > first) dima -= d1;
            }
           // cout << shasha << " "<< dima<<endl;
           //cout << ans << endl;
    }
    cout << ans << endl;
    return 0;
}
