#include "../include/fmSynth.h"
#include <iostream>
#include <string>
using namespace std;

//Create a new synth with one oscillator
FmSynth::FmSynth(double samplerate, double frequency, string waveform1,string waveform2, double modamount, double ratio) : Synth(samplerate, frequency, waveform1, 1){
    double tempFreq = frequency * ratio;
    cout<<"Created a FM synthesizer"<<endl;
    this->modamount=modamount;
    this->ratio = ratio;
    Synth::addOscillator(waveform2,1,tempFreq);     //Add one oscillator with that will be the modulator
    
}

FmSynth::~FmSynth(){
    cout<<"Destructed a FM synthesizer"<<endl;
}

void FmSynth::setFrequency(double frequency){
    this->frequency=frequency;
    oscillatorVector[1]->setFrequency(frequency*ratio);     //Set the frequency of the modulator
    oscillatorVector[0]->setFrequency(frequency);           //Set the frequency of the base
}

double FmSynth::getSample(){
    return oscillatorVector[0]->getSample();                //Return the sample of only the base oscillator. Since it is fm we don't need to hear the modulator
}

//Calculate the fm
void FmSynth::tick(){
    double sample;
    sample = oscillatorVector[1]->getSample()*modamount;    //Get the amp value of the modulator
    
    this->frequency+=sample;                                //Set the base frequency with the modulator amplitude added

    oscillatorVector[0]->setFrequency(this->frequency);     //Set the new frequencyt of the base oscillator

    for(int i = 0; i < oscillatorVector.size(); i++){
        oscillatorVector[i]->tick();                        //Ask fir the next sample of each oscillator.
    }
}

int FmSynth::say_Hello(){
    return this->hello;
}