#include<bits/stdc++.h>

using namespace std;

struct frac
{
    float v;
    float w;
    float ww;
    float pp;
};

bool cmp(struct frac x,struct frac y)
{
    float i = x.v/x.w;
    float j = y.v/y.w;
    return i>j;
}

int main()
{
    float tp=0;
    int n,i,W;
    cin >> n;
    frac array[n];
    for(i=0;i<n;i++)
    {
        cin >> array[i].v >> array[i].w;
        array[i].ww=0;
        array[i].pp=0;
    }
    sort(array,array+n,cmp);
    cout << "Enter a total Weight Do you Want" << endl;
    cin >> W;    
    int cw=0;               
    float p=0;                     // cw= current Weight
    i=0;
    while (cw < W && i<n)
    {
        if(array[i].w <= W-cw)
        {
            cw += array[i].w;
            array[i].ww=array[i].w;
            array[i].pp=array[i].v;
            p += array[i].v;
        }
        else
        {
            array[i].ww=W-cw;
            array[i].pp=(W-cw)*(array[i].v/array[i].w);
            p += array[i].pp;
            cw = W;
        }
        i++;
    }
    cout << p << endl;
    cout << "Value " << " " << "Weight " << " " << "Weight Taken" << " " << "Profit Gain" << endl;
    for(int i=0;i<n;i++)
    {
        cout << array[i].v << "\t" << array[i].w << "\t" << array[i].ww << "\t \t" << array[i].pp << endl;
        tp += array[i].pp;
    }
    cout << "Total Profit Gain" << endl;
    cout << tp << endl;
}