#include <bits/stdc++.h>
using namespace std;

#define ll long long

int main() {
    ll t;
    cin >> t;

    vector<ll> out;

    while (t--) {
        ll x, y;
        cin >> x >> y;

        ll ans;
        ll m = max(x, y);
        ll sq = m * m;

        if (m % 2 == 0) {
            if (x == m)
                ans = sq - y + 1;
            else
                ans = (m - 1) * (m - 1) + x;
        } else {
            if (y == m)
                ans = sq - x + 1;
            else
                ans = (m - 1) * (m - 1) + y;
        }

        out.push_back(ans);
    }

    for (ll v : out)
        cout << v << "\n";
}