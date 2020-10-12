#include<bits/stdc++.h>
using namespace std;

struct item
{
    int p;
    int w;
    float ratio;
};
bool cmp(struct item x,struct item y)
{
    return x.ratio>y.ratio;
}

int main()
{
    int n,i,j;
    cout << "Enter the number of iteams" << endl;
    cin>>n;
    
    item arr[n+1]={0};
    for(int i=1;i<=n;i++)
    {
        cout << "Enter the profit and weight of the " << i << "th iteam." << endl;
        cin>> arr[i].p >> arr[i].w;
        arr[i].ratio=arr[i].p/arr[i].w;
    }
    cout << "enter the total weight" << endl;
    int W;cin>>W;
    //cout << "TEST" << endl;
    sort(arr,arr+n,cmp);
    float a[n+1][W+1];
    //cout << "TEST" << endl;
    for(i=0;i<=n;i++)
    {
        for(j=0;j<=W;j++)
        {
            if(i==0 || j==0)
            {
                a[i][j]=0;
            }
            else if(arr[i].w>j)
            {
                a[i][j]=a[i-1][j];
            }
            else
            {
                //cout << arr[i].w << "EXP";
                a[i][j]=max(a[i-1][j],a[i-1][j-arr[i].w]+arr[i].p);
            }
            //cout << a[i][j] << " ";
            
        }
        cout << endl;
        cout << "Total Profit: ";
        cout << a[n][W] << endl;
    }
    i=n;
    j=W;
    while(i>0 && j>=0)
    {
        //cout << "YES" << endl;
        if(a[i][j]==a[i-1][j])
        {
            cout << i << " = 0" << endl;
        }
        else
        {
            cout << i << " = 1" << endl;
            j=j-arr[i].w;
        }
        i--;
    }
}