#include "strings.h"
#include <iostream>
using namespace std;

Strings::Strings() : Instrument("violin", "Hnggg","String"){
    setPitchRange(24,84);
}

Strings::~Strings(){
}

void Strings::setType(string type){
    cout << type << endl;
    for(int i = 0; i<=types.size();i++){
        if(type == types[i]){
            this->instrument = type;
            sound = sounds[i];
            setInstrument(type,sound);
        }
    }
}

string Strings::getType(){
    return instrument;
}