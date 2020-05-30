#include <cstdio>
using namespace std;
const int maxq = 1e5 + 2010;
struct node
{
	int v, tag;
	node * lc, * rc;
	node() : v(0), tag(0), lc(NULL), rc(NULL) {}
};
node * ver[maxq];
inline int val(node * t) {return t ? t->v : 0;}
inline void copy(node * & t) {t = t ? new node(*t) : new node();}
inline void pull(node * t) {t->v = val(t->lc) + val(t->rc);}
inline void inv(node * t, int l, int r)
{
		t->tag ^= 1;
		t->v = r - l - t->v;
}
inline void push(node * t, int l, int r)
{
	if (t->tag) {
		int m = (l + r) / 2;
		copy(t->lc);
		copy(t->rc);
		inv(t->lc, l, m);
		inv(t->rc, m, r);
		t->tag = 0;
	}
}
node * set(node * t, int l, int r, int i, int v) // [l, r)
{
	copy(t);
	push(t, l, r);
	if (r - l == 1) {
		t->v = v;
	} else {
		int m = (l + r) / 2;
		if (i < m)
			t->lc = set(t->lc, l, m, i, v);
		else
			t->rc = set(t->rc, m, r, i, v);
		pull(t);
	}
	return t;
}
node * inv(node * t, int l, int r, int i, int j) // [l, r), [i, j)
{
	if (r <= i || l >= j)
		return t;
	copy(t);
	if (i <= l && r <= j) {
		inv(t, l, r);
	} else {
		push(t, l, r);
		int m = (l + r) / 2;
		t->lc = inv(t->lc, l, m, i, j);
		t->rc = inv(t->rc, m, r, i, j);
		pull(t);
	}
	return t;
}
int main()
{
	int n, m, q;
	scanf("%d%d%d", &n, &m, &q);
	for (int i = 1; i <= q; ++i) {
		int c, a, b;
		scanf("%d%d", &c, &a);
		switch (c) {
			case 1:
			case 2:
				scanf("%d", &b);
				--a, --b;
				ver[i] = set(ver[i-1], 0, n * m, a * m + b, 2 - c);
				break;
			case 3:
				--a;
				ver[i] = inv(ver[i-1], 0, n * m, a * m, (a + 1) * m);
				break;
			case 4:
				ver[i] = ver[a];
				break;
		}
		printf("%d\n", val(ver[i]));
	}
}
