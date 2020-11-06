#include<iostream>
#include<array>
#include<iterator>
using namespace std;

int main(){
  float nums = 3;
  float *i = &nums;

  cout << **&i << " " << &nums <<endl;

}
