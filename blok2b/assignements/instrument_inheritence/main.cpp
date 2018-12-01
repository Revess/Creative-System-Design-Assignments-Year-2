#include <iostream>
#include <string>
#include <array>

#include "percussion.h"
#include "strings.h"
#include "brass.h"
#include "woodwinds.h"

using namespace std;

int main(){
    string instrumentInput;
    cout<<"Which of the following instruments would you like to hear: "<<endl;
    cout<<"-bongo -conga -drums -marimba -timbale"<<endl;
    cin >> instrumentInput;
    Percussion percussion; 
    percussion.setType(instrumentInput);
    cout<<"Which of the following instruments would you like to hear: "<<endl;
    cout<<"-violin -viola -cello -contrabass"<<endl;
    cin >> instrumentInput;
    Strings strings;
    strings.setType(instrumentInput);
    cout<<"Which of the following instruments would you like to hear: "<<endl;
    cout<<"-trumpet -french horn -trombone -tuba"<<endl;
    cin >> instrumentInput;
    Brass brass; 
    brass.setType(instrumentInput);
    cout<<"Which of the following instruments would you like to hear: "<<endl;
    cout<<"-clarinet -saxophone -piccolo -flute -fagot"<<endl;
    cin >> instrumentInput;
    Woodwinds woodwinds;
    woodwinds.setType(instrumentInput);

    percussion.play();
    strings.play();
    brass.play();
    woodwinds.play();
    return 0;
}