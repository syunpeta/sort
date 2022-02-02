#include <bits/stdc++.h>
using namespace std;

void insertion_sort(vector<int> &a,int N){

    for(int i=1;i<N;i++){
        int v = a[i];
        int j=i-1;

        while(j>=0 && a[j] >v){
            a[j+1] =a[j];
            j-=1;
        }
        a[j+1] =v;

    }
}

int main(){
    int N;
    cout << "input size of vector" << endl;
    cin >> N;
    vector<int> a(N);
    for(int i=0;i<N;i++){
        cin >> a[i];
    }

    insertion_sort(a,N);
    
    for(int j=0;j<N;j++){
        cout <<a[j] << ", ";
    }

    return 0;

}