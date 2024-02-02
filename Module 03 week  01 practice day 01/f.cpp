

#include <bits/stdc++.h>
using namespace std;
#define ll long long

int main()
{
    int x, y;
    cin >> x >> y;
    ll ans = 02;
    for (int i = 2; i < y; i+=2)
    {
        // if (i % 2 == 0)
            ans += (pow(x, i));
    }
    cout << ans << endl;

    return 0;
}