#include "../include/triangle.h"


// Constructor and destructor
Triangle::Triangle(double samplerate, double frequency) :
  Oscillator(samplerate, frequency)
{
  // TODO - use setFrequency and phase instead, to prevent outrange values
  std::cout << "\nInside Square::oscillator (double frequency, double phase)"
    << "\nfrequency: " << frequency
    << "\nphase: " << phase;
}

Triangle::~Triangle()
{
  std::cout << "\nInside Square::~Square";
}


void Triangle::calculate()
{
  // calculate sample
  // NOTE: sin() method is not the most efficient way to calculate the Square value
  double tempPhase = (phase*4)-1;
  if(tempPhase > 1){
      sample=2-tempPhase;
  } else {
      sample=tempPhase;
  }
}
