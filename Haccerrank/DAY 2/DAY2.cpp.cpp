#include <iostream>
#include<iomanip>
using namespace std;

int main() 
{    int a;
     long long int b;
     char c;
     float d;
     double e;
     cin>>a>>b>>c>>d>>e;
     cout<<a<<endl;
     cout<<b<<endl;
     cout<<c<<endl;
     cout<<std::fixed<<std::setprecision(3)<<d<<endl;
     cout<<std::fixed<<std::setprecision(9)<<e<<endl;
    
    return 0;
}
