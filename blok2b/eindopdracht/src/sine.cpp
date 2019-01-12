#include "../include/sine.h"
using namespace std;

//~~CC~~ but altered the use of it slightly

// Constructor and destructor
Sine::Sine(double samplerate, double frequency) : Oscillator(samplerate, frequency){
    cout<<"Created a sine"<<endl;
}

Sine::~Sine(){
    cout<<"Destructed a sine"<<endl;
}

void Sine::calculate(){
    // calculate sample
    sample = sin(phase * PI_2);
}

//||CC||