#include "percussion.h"
#include <iostream>
using namespace std;

Percussion::Percussion() : Instrument("drum", "Ba Dum Tss"){
}

Percussion::~Percussion(){
}

void Percussion::setType(string type){
    cout << type << endl;
    for(int i = 0; i<=types.size();i++){
        if(type == types[i]){
            this->instrument = type;
            sound = sounds[i];
            setInstrument(type,sound);
        }
    }
}

string Percussion::getType(){
    return instrument;
}