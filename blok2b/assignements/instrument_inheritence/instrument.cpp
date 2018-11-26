#include <iostream>
#include "instrument.h"
using namespace std;

Instrument::Instrument(string instrument,string sound){
    this->instrument = instrument;
    this->sound = sound;
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

void Instrument::play(){
    cout<<sound<<endl;
}