#include "../include/square.h"
using namespace std;

// Constructor and destructor
Square::Square(double samplerate, double frequency) : Oscillator(samplerate, frequency) {
    cout<<"Created a square"<<endl;
}

Square::~Square(){
    cout<<"Destructed a square"<<endl;
}


void Square::calculate(){
  // calculate sample
  // NOTE: sin() method is not the most efficient way to calculate the Square value
  if(phase > 0.5){
      sample=1;
  } else if(phase <0.5){
      sample=-1;
  }
}
