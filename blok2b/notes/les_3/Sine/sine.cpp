#include "sine.h"

Sine::Sine(double samplerate,double frequency) :
    frequency(frequency),phase(0),sample(0),samplerate(samplerate);
{

}

Sine::~Sine(){

}

double Sine::getSample() {
    return sample;
}

void Sine::tick(){

    phase+=frequency*1/samplerate;
    if(phase >=1)phase=phase-1;
    sample=sin(phase*PI_2);
}

void Sine::setFrequency(double frequency){
    if(frequency>0&&frequency<0.5*samplerate)
    this->frequency=frequency;
}

double Sine::getFrequency(){
    
}