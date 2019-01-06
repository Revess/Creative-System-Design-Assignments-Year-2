#include "../include/sine.h"
using namespace std;

// Constructor and destructor
Sine::Sine(double samplerate, double frequency) : Oscillator(samplerate, frequency){
    cout<<"Created a sine"<<endl;
}

Sine::~Sine(){
    cout<<"Destructed a sine"<<endl;
}

void Sine::calculate(){
    // calculate sample
    // NOTE: sin() method is not the most efficient way to calculate the sine value
    sample = sin(phase * PI_2);
}
