#include "percussion.h"
using namespace std;

Percussion::Percussion(){
    type = "drum";
    sound = "Ba Dum Tss";
}

Percussion::~Percussion(){

}

void Percussion::setType(string type){
    for(int i = 0; i<types.size();i++){
        if(type == types[i]){
            this->type = type;
            sound = sounds[i];
        }
    }
}

string Percussion::getType(){
    return type;
}