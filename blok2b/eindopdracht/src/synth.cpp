#include "../include/synth.h"
#include <string>
using namespace std;

Synth::Synth(string type, double frequency, string waveform, float amplitude, double samplerate){
    cout<<"Synth: "<<type<<" created"<<endl;
    this->frequency=frequency;
    this->type=type;
    this->waveform=waveform;
    this->amplitude=amplitude;
    Sine sine(samplerate,frequency);
    Saw saw(samplerate,frequency);
    Square square(samplerate,frequency);
    Triangle triangle(samplerate,frequency);

    if(waveform == "sine"){
        oscillator = &sine;
    } else if(waveform == "saw"){
        oscillator = &saw;
    } else if(waveform == "square"){
        oscillator = &square;
    } else if(waveform == "traingle"){
        oscillator = &triangle;
    }
}

Synth::~Synth(){
    cout<<"Synth: "<<type<<"destructed"<<endl;
}

void Synth::setEnvelope(float attack, float decay, float sustain, float release){

}

//int getEnvelope(int *array);

void Synth::setType(string type){
    this->type = type;
}

string Synth::getType(){
    return type;
}

void Synth::setFrequency(double frequency){
    this->frequency = frequency;
    oscillator->setFrequency(frequency);
}

double Synth::getFrequency(){
    return oscillator->getFrequency();
}

void Synth::setAmplitude(double amplitude){
    std::cout << ".";
}

double Synth::getAmplitude(){
    return 1; 
}

void Synth::setWaveform(string waveform){
    this->waveform = waveform;

    // if(waveform == "sine"){
    //     oscillator = &sine;
    // } else if(waveform == "saw"){
    //     oscillator = &saw;
    // } else if(waveform == "square"){
    //     oscillator = &square;
    // } else if(waveform == "traingle"){
    //     oscillator = &triangle;
    // }
}

string Synth::getWaveform(){
    return waveform;
}

double Synth::getSample(){
    return oscillator->getSample();
}

void Synth::tick(){
    oscillator->tick();
}

void Synth::calculate(){
    std::cout << ".";
}