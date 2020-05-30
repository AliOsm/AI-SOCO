#include<bits/stdc++.h>
using namespace std;
#define MAX 100009
#define INF 200000000000000
typedef long long ll;
ll n, m, x, y, z, ans;

typedef struct _node{
    ll max_pref;
    ll max_suff;
    ll sum;

    ll ans;

}Node;

Node tree[4 * MAX + 100];

ll ara[300000];

void init(ll node, ll beg, ll end)
{
    if(beg > end) return;

    if(beg == end){

        tree[node].sum = ara[beg];
        tree[node].max_pref = ara[beg];
        tree[node].max_suff = ara[beg];

        tree[node].ans = ara[beg];
        return;
    }

    ll mid = (beg + end) / 2;
    ll lft = 2 * node;
    ll rght = 2 * node + 1;

    init(lft, beg, mid);
    init(rght, mid + 1, end);

    tree[node].sum = tree[lft].sum + tree[rght].sum;
    tree[node].max_pref = max(tree[lft].max_pref, tree[lft].sum + tree[rght].max_pref);
    tree[node].max_suff = max(tree[rght].max_suff, tree[rght].sum + tree[lft].max_suff);

    tree[node].ans = max(tree[lft].ans, tree[rght].ans);
    tree[node].ans = max(tree[node].ans, tree[lft].max_suff + tree[rght].max_pref);


}

Node query(ll node, ll beg, ll end, ll i, ll j)
{
    if(beg >= i && end <= j){
        return tree[node];
    }

    ll mid = (beg + end) / 2;
    ll lft = 2 * node;
    ll rght = 2 * node + 1;

    Node p, q;

    p.sum = p.ans = p.max_pref = p.max_suff = -INF;
    q.sum = q.ans = q.max_pref = q.max_suff = -INF;

    Node result_node;

    if (mid >= i) p = query(lft, beg, mid, i, j);
    if (mid < j) q = query(rght, mid + 1, end, i, j);

    result_node.sum = p.sum  + q.sum;
    result_node.max_pref = max(p.max_pref, p.sum + q.max_pref);
    result_node.max_suff = max(q.max_suff, q.sum + p.max_suff);

    result_node.ans = max(p.ans, max(q.ans, p.max_suff + q.max_pref));

    return result_node;

}

void update(ll node, ll beg, ll end, ll i, ll val)
{
    if(beg > i || end < i || beg > end) return;

    if(beg == end){
        tree[node].sum = val;
        tree[node].max_pref = val;
        tree[node].max_suff = val;

        tree[node].ans = val;
        return;
    }

    ll mid = (beg + end) / 2;
    ll lft = 2 * node;
    ll rght = 2 * node + 1;

    update(lft, beg, mid, i, val);
    update(rght, mid + 1, end, i, val);

    tree[node].sum = tree[lft].sum + tree[rght].sum;
    tree[node].max_pref = max(tree[lft].max_pref, tree[lft].sum + tree[rght].max_pref);
    tree[node].max_suff = max(tree[rght].max_suff, tree[rght].sum + tree[lft].max_suff);

    tree[node].ans = max(tree[lft].ans, tree[rght].ans);
    tree[node].ans = max(tree[node].ans, tree[lft].max_suff + tree[rght].max_pref);

}

int main()
{
    scanf("%I64d", &n);
    for(int i = 1; i <= n; i++) scanf("%I64d", &ara[i]);

    init(1, 1, n);

    for(int i = 0; i < n; i++){

        scanf("%I64d", &x);
        if(i == n - 1){
            printf("0\n");
            return 0;
        }

        update(1, 1, n, x, -INF);
        ll ans = tree[1].ans;
        printf("%I64d\n", ans);
    }


    return 0;
}
