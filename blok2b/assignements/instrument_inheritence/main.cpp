#include <iostream>
#include <string>
#include <array>

#include "percussion.h"

using namespace std;

int main(){
    string instrument;
    cout<<"Which of the following instruments would you like to hear: "<<endl;
    cout<<"-bongo -conga -drums -marimba -timbale"<<endl;
    cin >> instrument;
    Percussion percussion; 
    percussion.setInstrument(instrument);
    percussion.play();
    return 0;
}