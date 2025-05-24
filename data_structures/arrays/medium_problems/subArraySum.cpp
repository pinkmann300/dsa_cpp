#include <iostream> 
#include <cmath> 

using namespace std;


int arrayCount(vector<int> &data1, int targetSum);

int main()
{
    return -1; 
}

int arrayCount(vector<int> &data1, int targetSum){
    vector<vector<int>> sumArrs;
    int length = data1.size();
    int sum = 0;  
    for (int i = 0; i < length; i++){
        sum += data1[i]; 
        if (sum == targetSum){
            
        }
        

    }
}