#include<iostream>
using namespace std;
int main()
{
    double mc,tp,ta;
    cin>>mc;
    cin>>tp;
    cin>>ta;
    double t,n,sum;
    t=((tp/100)*mc);
    n=((ta/100)*mc);
    sum=mc+t+n;
    sum=sum+0.5;
    cout<<(int)sum<<endl;
    
    return 0;
}
