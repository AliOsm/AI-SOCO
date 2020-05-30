/*

Our shadows stretch out on the pavement
As I walk in the twilight with you
If we could be together like this forever
Holding hands
It's almost enough to make me cry

The wind grows colder
I can smell winter
Soon the season will come to this town
When I can get close to you

This moment
When the two of us cuddle up
To gaze at the first snow flower of the year
Is overflowing with happiness

It's not dependence or weakness
I just love you
I thought so with all my heart

I feel like when I'm with you
I can overcome anything
I pray that these days
Will continue forever

The wind rattled the window
The night shakes you awake
I will change any sorrow
Into a smile

The snow flowers fell
Outside the window
Unceasing
And colored our town
I realized that love means
Wanting to do something
For someone else

If I should lose you
I'll become a star and shine on you
I'll be with you even on nights
When your smile is wet with tears

This moment
When the two of us cuddle up
To gaze at the first snow flower of the year
Is overflowing with happiness

It's not dependence or weakness
I just want to be like this
With you forever
I can honestly think that now

The pure white snow flowers
Bury this town
Softly drawing memories in our hearts
Together forever with you...

*/

#include <bits/stdc++.h>

using namespace std;

const int N = 2e5 + 5;
const int inf = 1e9;

int a[N];

int main() {
  int n;
  scanf("%d", &n);
  set<int> s;
  for (int i = 0; i < n; i++) {
    scanf("%d", a + i);
    if (i) {
      if (a[i] == a[i-1]) {
        puts("NO");
        return 0;
      }
      int d = abs(a[i] - a[i - 1]);
      if (d > 1) {
        s.insert(d);
      }
    }
  }
  bool can = (s.size() <= 1);
  for (int i = 0; i < n; i++) a[i]--;
  int d = (s.size()? *(s.begin()) : 1);
  for (int i = 1; i < n; i++) {
    int l = min(a[i-1], a[i]);
    int r = max(a[i-1], a[i]);
    if (d > 1 && abs(l - r) == 1 && l / d != r / d) {
      can = 0;
    }
  }
  if (!can) {
    puts("NO");
  } else {
    puts("YES");
    printf("%d %d\n", inf, d);
  }

  return 0;
}
