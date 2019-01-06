#include "../include/simpleSynth.h"
#include <iostream>
#include <string>
using namespace std;

SimpleSynth::SimpleSynth(double samplerate, double frequency, string waveform) : Synth(samplerate, frequency, waveform, 1){
    cout<<"Created a Simple synthesizer"<<endl;
}

SimpleSynth::~SimpleSynth(){
    cout<<"Destructed a Simple synthesizer"<<endl;
}