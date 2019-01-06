#include "../include/triangle.h"
using namespace std;

// Constructor and destructor
Triangle::Triangle(double samplerate, double frequency) : Oscillator(samplerate, frequency){
    cout<<"Created a triangle"<<endl;
}

Triangle::~Triangle(){
    cout<<"Destructed a sine"<<endl;
}


void Triangle::calculate(){
  // calculate sample
  // NOTE: sin() method is not the most efficient way to calculate the Square value
  double tempPhase = (phase*4)-1;
  if(tempPhase > 1){
      sample=2-tempPhase;
  } else {
      sample=tempPhase;
  }
}
