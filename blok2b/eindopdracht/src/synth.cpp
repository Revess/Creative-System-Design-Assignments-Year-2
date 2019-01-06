#include "../include/synth.h"
#include "sine.h"
#include "saw.h"
#include "square.h"
#include "triangle.h"

#include <iostream>
#include <string>

using namespace std;

Synth::Synth(double samplerate, double frequency, string waveform, int amount){
    this->samplerate = samplerate;
    this->frequency = frequency;
    this->waveform = waveform;
    cout<<"made synth with waveform: "<<waveform<<endl;
    if(waveform == "sine"){
        for(int i = 0; i < amount; i++){
            oscillator = new Sine(samplerate,frequency);
            oscillatorVector.push_back(oscillator);
        }
    }else if(waveform == "saw"){
        for(int i = 0; i < amount; i++){
            oscillator = new Saw(samplerate,frequency);
            oscillatorVector.push_back(oscillator);
        }
    }else if(waveform == "square"){
        for(int i = 0; i < amount; i++){
            oscillator = new Square(samplerate,frequency);
            oscillatorVector.push_back(oscillator);
        }
    }else {
        for(int i = 0; i < amount; i++){
            oscillator = new Triangle(samplerate,frequency);
            oscillatorVector.push_back(oscillator);
        }
    }
}

Synth::~Synth(){
    for(int i = 0; i < oscillatorVector.size(); i++){
        delete oscillatorVector[i];
    }
}

void Synth::setFrequency(double frequency){
    this->frequency = frequency;
    for(int i = 0; i < oscillatorVector.size(); i++){
        oscillatorVector[i]->setFrequency(frequency);
    }
}

void Synth::addOscillator(string waveform, int amount, double frequency){
    if(waveform == "sine"){
        for(int i = 0; i < amount; i++){
            oscillator = new Sine(samplerate,frequency);
            oscillatorVector.push_back(oscillator);
        }
    }else if(waveform == "saw"){
        for(int i = 0; i < amount; i++){
            oscillator = new Saw(samplerate,frequency);
            oscillatorVector.push_back(oscillator);
        }
    }else if(waveform == "square"){
        for(int i = 0; i < amount; i++){
            oscillator = new Square(samplerate,frequency);
            oscillatorVector.push_back(oscillator);
        }
    }else {
        for(int i = 0; i < amount; i++){
            oscillator = new Triangle(samplerate,frequency);
            oscillatorVector.push_back(oscillator);
        }
    }
}

double Synth::getSample(){
    double sample;
    for(int i = 0; i < oscillatorVector.size(); i++){
        sample = oscillatorVector[i]->getSample();
    }
    return sample;
}

void Synth::tick(){
    for(int i = 0; i < oscillatorVector.size(); i++){
        oscillatorVector[i]->tick();
    }
}