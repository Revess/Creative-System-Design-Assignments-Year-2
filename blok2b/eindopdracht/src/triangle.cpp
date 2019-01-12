#include "../include/triangle.h"
using namespace std;

//~~CC~~ but altered the use of it slightly

// Constructor and destructor
Triangle::Triangle(double samplerate, double frequency) : Oscillator(samplerate, frequency){
    cout<<"Created a triangle"<<endl;
}

Triangle::~Triangle(){
    cout<<"Destructed a sine"<<endl;
}


void Triangle::calculate(){
  // calculate sample
  double tempPhase = (phase*4)-1;
  if(tempPhase > 1){
      sample=2-tempPhase;
  } else {
      sample=tempPhase;
  }
}

//||CC||