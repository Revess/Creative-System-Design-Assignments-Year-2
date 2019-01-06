#include "../include/fmSynth.h"
#include <iostream>
#include <string>
using namespace std;

FmSynth::FmSynth(double samplerate, double frequency, string waveform1,string waveform2, double modamount, double ratio) : Synth(samplerate, frequency, waveform1, 1){
    double tempFreq = frequency * ratio;
    cout<<"Created a FM synthesizer"<<endl;
    this->modamount=modamount;
    this->ratio = ratio;
    Synth::addOscillator(waveform2,1,tempFreq);
    
}

FmSynth::~FmSynth(){
    cout<<"Destructed a FM synthesizer"<<endl;
}

void FmSynth::setFrequency(double frequency){
    this->frequency=frequency;
    oscillatorVector[1]->setFrequency(frequency*ratio);
    oscillatorVector[0]->setFrequency(frequency);
}

double FmSynth::getSample(){
    return oscillatorVector[0]->getSample();
}

void FmSynth::tick(){
    double sample;
    sample = oscillatorVector[1]->getSample()*modamount;
    this->frequency+=sample;

    oscillatorVector[0]->setFrequency(this->frequency);

    for(int i = 0; i < oscillatorVector.size(); i++){
        oscillatorVector[i]->tick();
    }
}

int FmSynth::say_Hello(){
    return this->hello;
}