
/**************************************************************
**               BISMILLAH HIR RAHMAN NIR RAHIM              **
**             https://github.com/Md-Merazul-Islam           **
**************************************************************/
#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
using namespace __gnu_pbds;
using namespace std;
#define PI 3.14159265359
#define dmin 1e-9
#define dd double
#define ll long long
#define yes cout << "YES\n"
#define no cout << "NO\n"
#define pb push_back
#define vi vector<ll>
#define vpi vector<pair<ll, ll>>
#define pii pair<ll, ll>
#define srt(a) sort(a.begin(), a.end())
#define all(a) a.begin(), a.end()
#define rsrt(a) sort(a.rbegin(), a.rend())
#define line "\n"
#define nl cout << "\n"
#define fast ios_base::sync_with_stdio(false), cin.tie(NULL);
#define loop(i, a, b) for (int i = (a); i < (b); ++i)
#define rloop(i, a, b) for (int i = (a); i <= (b); ++i)
#define scan(a) loop(i, 0, a.size()) cin >> a[i]
void print(vector<ll> &a) { loop(i, 0, a.size()) cout << a[i] << ' '; }
template <typename T>
using my_ordered_set = tree<T, null_type, less<T>, rb_tree_tag, tree_order_statistics_node_update>;
const int N = 2e5 + 5;
void hello_world_solve_here()
{

    ll n, b, x;
    cin >> n >> b >> x;
    vector<ll> v(n);
    ll ans = 0;
    for (ll i = 0; i < n; i++)
        cin >> v[i];
    map<ll, ll> m;
    for (auto xx : v)
        m[xx]++;
    ll limit = *max_element(v.begin(), v.end());
    for (ll k = 1; k <= limit; k++)
    {
        ll sum = 0;
        for (auto [xx, y] : m)
        {
            ll al = xx / k + 1;
            ll be = xx / k;
            ll p = xx % k;
            ll t = al * p + (k - p) * be;
            ll c = t * t - be * al * p * (k - p) - al * al * (p * (p + 1)) / 2 - be * be * ((k - p) * (k - p + 1) / 2);
            sum += c * b * y;
        }
        ans = max(ans, sum - (k - 1) * x);
    }
    cout << ans << endl;
}

signed main()
{
    fast;
    int t = 1;
    cin >> t;
    while (t--)
        hello_world_solve_here();
    return 0;
}