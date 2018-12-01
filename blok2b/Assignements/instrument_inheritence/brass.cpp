#include "brass.h"
#include <iostream>
using namespace std;

Brass::Brass() : Instrument("trumpet", "Bwaap","Brass"){
    setPitchRange(36,60);
}

Brass::~Brass(){
}

void Brass::setType(string type){
    cout << type << endl;
    for(int i = 0; i<=types.size();i++){
        if(type == types[i]){
            this->instrument = type;
            sound = sounds[i];
            setInstrument(type,sound);
        }
    }
}

string Brass::getType(){
    return instrument;
}