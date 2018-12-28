#include "../include/square.h"


// Constructor and destructor
Square::Square(double samplerate, double frequency) :
  Oscillator(samplerate, frequency)
{
  // TODO - use setFrequency and phase instead, to prevent outrange values
  std::cout << "\nInside Square::oscillator (double frequency, double phase)"
    << "\nfrequency: " << frequency
    << "\nphase: " << phase;
}

Square::~Square()
{
  std::cout << "\nInside Square::~Square";
}


void Square::calculate()
{
  // calculate sample
  // NOTE: sin() method is not the most efficient way to calculate the Square value
  if(phase > 0.5){
      sample=1;
  } else if(phase <0.5){
      sample=-1;
  }
}
