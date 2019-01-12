#include "../include/simpleSynth.h"
#include <iostream>
#include <string>
using namespace std;

//Create an instance of the synthesizer with just one oscillator
SimpleSynth::SimpleSynth(double samplerate, double frequency, string waveform) : Synth(samplerate, frequency, waveform, 1){
    cout<<"Created a Simple synthesizer"<<endl;
}

SimpleSynth::~SimpleSynth(){
    cout<<"Destructed a Simple synthesizer"<<endl;
}