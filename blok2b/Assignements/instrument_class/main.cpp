#include <iostream>
#include "instrument.h"
#include <string>
using namespace std;

int main(){
    cout<<"Give the instrumentsound you would like to hear:"<<endl;
    string sound = "";
    cin>>sound;
    Instrument instrument1(sound);
    instrument1.makeSound();
    return 0;
}