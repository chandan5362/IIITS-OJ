#include <bits/stdc++.h>
using namespace std;
int main() {
   int t;
   cin>>t;
   while(t--){
      int a,b;
      cin>>a>>b;
      int diff = a>b?a-b:b-a;
      cout<<diff<<endl;
   }
   return 0;
}
