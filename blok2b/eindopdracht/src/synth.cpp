#include "../include/synth.h"
#include "sine.h"
#include "saw.h"
#include "square.h"
#include "triangle.h"

#include <iostream>
#include <string>

using namespace std;

//Create an instance of a synthesizer with just one oscillator and whatever waveform the user wants and the program allows
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
    for(int i = 0; i < oscillatorVector.size(); i++){       //Also delete each oscillator
        delete oscillatorVector[i];
    }
}

//Change the frequency of every oscillator
void Synth::setFrequency(double frequency){
    this->frequency = frequency;
    for(int i = 0; i < oscillatorVector.size(); i++){
        oscillatorVector[i]->setFrequency(frequency);
    }
}

//Add an oscillator with a custom waveform
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

//Get the sample from every oscillator
//TODO: Make sure it returns every oscillator, it only returns the last one right now.
double Synth::getSample(){
    double sample;
    for(int i = 0; i < oscillatorVector.size(); i++){
        sample = oscillatorVector[i]->getSample();
    }
    return sample;
}

//Set the tick from every oscillator.
void Synth::tick(){
    for(int i = 0; i < oscillatorVector.size(); i++){
        oscillatorVector[i]->tick();
    }
}
