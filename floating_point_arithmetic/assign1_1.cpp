#include<iostream>
using namespace std;

float eps_simple()
{   float eps = 1.0;
    int count = 0;
    while(eps + 1.0 > 1.0)
{       count++;
        eps = 0.5*eps;
}    
    //cout<<count<<endl;
    return eps;
}

double eps_with_double()
{   double eps = 1.0;
    double exact = 1.0;
    double multiplier = 0.5;
    int count = 0;
    while(eps + exact > exact)
{       count++;
        eps = multiplier*eps;
}    
    //cout<<count<<endl;
    return eps;
}

float eps_with_float()
{   float eps = 1.0;
    float exact = 1.0;
    float multiplier = 0.5;
    int count = 0;
    while(eps + exact > exact)
{       count++;
        eps = multiplier*eps;
}    
    //cout<<count<<endl;
    return eps;
}

long double eps_with_long_double()
{   long double eps = 1.0;
    long double exact = 1.0;
    long double multiplier = 0.5;
    int count = 0;
    while(eps + exact > exact)
{       count++;
        eps = multiplier*eps;
}    
    //cout<<count<<endl;
    return eps;
}

int main(){
    cout<<"Epsilon with double : ";
    cout<<eps_with_double()<<endl;
    cout<<"Epsilon with float : ";
    cout<<eps_with_float()<<endl;
    cout<<"Epsilon with long double : ";
    cout<<eps_with_long_double()<<endl;
    cout<<"Epsilon to find data type of temporaries: ";
    cout<<eps_simple()<<endl;
    return 0;
}


//find the data type of the temporaries.
