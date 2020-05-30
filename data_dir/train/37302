#include <bits/stdc++.h>
using namespace std;

struct Node {
    pair<int, int> p;

    Node* children[26];
    Node() {
        memset(children, 0, sizeof children);
    }
    ~Node() {
        for (auto &x : children)
            delete x;
    }
};
Node *root = new Node();
int main() {
    ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0);
#ifndef ONLINE_JUDGE
//  freopen("test.in", "rt", stdin);
#endif
    string s, t;
    cin >> s >> t;

    for (char &x : s)
        x -= 'a';
    for (char &x : t)
        x -= 'a';

    for (int i = 0; i < s.size(); ++i) {
        Node* curr = root;
        for (int j = i; j < s.size(); ++j)
            if (curr->children[s[j]])
                curr = curr->children[s[j]];
            else {
                curr = curr->children[s[j]] = new Node();
                curr->p = {i,j};
            }
        }
    for (int i = s.size() - 1; i >= 0; --i) {
        Node* curr = root;
        for (int j = i; j >= 0; --j) {
            if (curr->children[s[j]])
                curr = curr->children[s[j]];
            else {
                curr = curr->children[s[j]] = new Node();
                curr->p = {i,j};
            }
        }
    }

    vector<pair<int, int> > vec;
    int h = 0, prv = 0;
    for (int i = 0; i < t.size(); ++i) {
        Node *curr = root;
        if (!curr->children[t[i]]) {
            cout << -1;
            return 0;
        }
        --i;
        while (i + 1 < t.size() && curr->children[t[i + 1]])
            ++i, curr = curr->children[t[i]];

        vec.push_back(curr->p);
    }
    cout << vec.size() << endl;
    for (auto &x : vec)
        cout << x.first + 1 << ' ' << x.second + 1 << '\n';

    return 0;

}
