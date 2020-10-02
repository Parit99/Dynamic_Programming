#include<bits/stdc++.h>
using namespace std;
int main()
{
    cout << "Enter the number of items :" << endl;
    int n;
    cin >> n;
    vector<int> weight(n),price(n);
    for(int i=0;i<n;++i)
    {
        cout << "Enter weight of item-" << i+1 << " : " << endl;
        cin >> weight[i];
        cout << "Enter cost of item-" << i+1 << " : " << endl;
        cin >> price[i];
    }
    
    cout << "Enter the weight of your bagpack : " << endl;
    int W;
    cin >> W;
    vector<int> dp(W+1);
    for(int i=0;i<n;++i)
    {
        for(int j=W-weight[i];j>=0;--j)
        {
            dp[j+weight[i]]=max(dp[j+weight[i]],dp[j]+price[i]);
        }
    }
    cout << "Maximun value you can get is " << dp[W] << endl; 
}
