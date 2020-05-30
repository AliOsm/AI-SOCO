#include <bits/stdc++.h>
using namespace std;
int sumOfDigits(int a)
{
    int sum = 1;
    while (a)
    {
        sum *= a % 10;
        a /= 10;
    }
    return sum;
}
int findMax(int x)
{
    int b = 1, ans = x;
    while (x)
    {
        int cur = (x - 1) * b + (b - 1);
        if (sumOfDigits(cur) > sumOfDigits(ans) ||(sumOfDigits(cur) == sumOfDigits(ans) &&cur > ans))
            ans = cur;
        x /= 10;
        b *= 10;
    }

    return ans;
}

// driver program
int main()
{
    int n;
    cin >> n;
    int tt = findMax(n);
    cout << sumOfDigits(tt)<<endl;
    return 0;
}
