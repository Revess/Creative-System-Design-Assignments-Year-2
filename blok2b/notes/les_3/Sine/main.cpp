#include <iostream>
#include "sine.h"
#include "WriteToFile.h"

int main(){
    int samplerate = 44100;

    Sine sine(samplerate, 220);

    for(int i=0; i<samplerate; i++){
        double sample=sine.getSample();
        std::cout<<"\n"<<sample<<endl;
    }
}