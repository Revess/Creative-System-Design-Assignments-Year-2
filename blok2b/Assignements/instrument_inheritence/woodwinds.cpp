#include "woodwinds.h"
#include <iostream>
using namespace std;

Woodwinds::Woodwinds() : Instrument("clarinet", "SquareSound","Woodwind"){
    setPitchRange(48,84);
}

Woodwinds::~Woodwinds(){
}

void Woodwinds::setType(string type){
    cout << type << endl;
    for(int i = 0; i<=types.size();i++){
        if(type == types[i]){
            this->instrument = type;
            sound = sounds[i];
            setInstrument(type,sound);
        }
    }
}

string Woodwinds::getType(){
    return instrument;
}