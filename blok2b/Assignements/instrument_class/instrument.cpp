#include <iostream>
#include "instrument.h"
using namespace std;

Instrument::Instrument(string newSound){
    sound = newSound;
}

void Instrument::makeSound(){
    cout<<sound<<endl;
}