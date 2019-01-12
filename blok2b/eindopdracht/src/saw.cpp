#include "../include/saw.h"
using namespace std;

//~~CC~~ but altered the use of it slightly

// Constructor and destructor
Saw::Saw(double samplerate, double frequency) : Oscillator(samplerate, frequency){
    cout<<"Created a saw"<<endl;

}

Saw::~Saw(){
    cout<<"Destructed a saw"<<endl;
}


void Saw::calculate(){
  // calculate sample
  sample = (phase*2)-1;
}

//||CC||