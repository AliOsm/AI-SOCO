#include <bits/stdc++.h>
#define REP(i,n) for(int i=0;i<(int)n;i++)
#define REP1(i,j,n) for(int i=j;i<(int)n;i++)
#define all(x) x.begin(),x.end()
#define BUG cerr<<"BUG\n";

typedef long long ll;

using namespace std;


int main() {
//    ios_base::sync_with_stdio(0); cin.tie(0);

    int students,bugs,s;
    scanf("%d%d%d",&students,&bugs,&s);
    vector<pair<int,int> >a(bugs);
    vector<pair<int,pair<int,int> > >stds(students);
    REP(i,bugs)scanf("%d",&a[i].first),a[i].second=i;
    REP(i,students)scanf("%d",&stds[i].first);
    REP(i,students)scanf("%d",&stds[i].second.first),stds[i].second.second=i;
    sort(all(stds));
    sort(all(a));
    bool can=0;
//    BUG

    for(int i=students-1;i>=0;i--)
        if(stds[i].first>=a[bugs-1].first&&stds[i].second.first<=s){
            can=1;
        }
    if(!can){
        printf("NO\n");
        return 0;
    }


    int lo=1,hi=bugs,bst=bugs;
    while(lo<=hi){
        int days=lo+hi>>1;
        set<pair<int,int> >active;
        int std_idx=students-1;
        ll sum=0;
        for(int i=bugs-1;i>=0;i-=days){
            while(std_idx>=0&&stds[std_idx].first>=a[i].first){
                active.insert(stds[std_idx].second);
                std_idx--;
            }
            if(!active.empty()){
                auto it=active.begin();
                sum+=(*it).first;
//                cerr<<it->second<<"\n";
                active.erase(it);
            }else {
                sum=s+1;
            }
        }
//        cerr<<days<<" "<<sum<<"\n";
        if(sum<=s){
            bst=days;
            hi=days-1;
        }else lo=days+1;
    }
    int std_idx=students-1;
    set<pair<int,int> >active;
    vector<int>res(bugs);
    for(int i=bugs-1;i>=0;i-=bst){
        while(std_idx>=0&&stds[std_idx].first>=a[i].first){
            active.insert(stds[std_idx].second);
            std_idx--;
        }
        auto it=active.begin();
        for(int j=i;j>=max(0,i-bst+1);j--) {
            res[a[j].second] = it->second;
        }
        active.erase(it);
    }
    printf("YES\n");
    REP(i,bugs){
        if(i)printf(" ");
        printf("%d",res[i]+1);
    }
    printf("\n");
}