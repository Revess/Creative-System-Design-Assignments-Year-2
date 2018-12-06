#include <iostream>
using namespace std;

int main(){
    float samples[100];
    float *samplePointer = samples;

    for(int s=0; s<100; s++){
        *samplePointer = s;
        samplePointer++;        
    }

    for(int s=0; s<100; s++){
        cout<<samples[s]<<endl;
    }
}