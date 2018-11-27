#include <iostream>
#include "instrument.h"
using namespace std;

Instrument::Instrument(string newSound){
    sound = newSound;
}

Instrument::~Instrument(){
    
}

void Instrument::makeSound(){
    cout<<sound<<endl;
}