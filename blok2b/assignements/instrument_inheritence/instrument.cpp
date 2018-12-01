#include <iostream>
#include "instrument.h"
using namespace std;

Instrument::Instrument(string instrument,string sound,string type){
    this->instrument = instrument;
    this->sound = sound;
    this->type = type;
}

Instrument::~Instrument(){
}

void Instrument::setInstrument(string instrument,string sound){
    this->instrument = instrument;
    this->sound = sound;
}

string Instrument::getInstrument(){
    return instrument;
}

void Instrument::setPitchRange(int pitchMin, int pitchMax){
    pitchRange[0] = pitchMin;
    pitchRange[1] = pitchMax;
}

string Instrument::getPitchRange(){
    return instrument;
}

void Instrument::play(){
    cout<<"Type of instrument: "<<type<<endl<<"Name: "<<instrument<<endl<<"Pitchrange: "<<pitchRange[0]<<"-"<<pitchRange[1]<<endl<<"Sound: "<<sound<<endl<<endl;
}