#include <iostream>
#include <string>
#include <array>

#include "percussion.h"

using namespace std;

int main(){
    array<string, 5> instruments;
    cout<<"Which of the following instruments would you like to hear: "<<endl;
    cout<<"-bongo -conga -drums -marimba -timbale"<<endl;
    cin>>instruments[0];
    Percussion drums;
    drums.setType(instruments[0]);
    drums.play();
    return 0;
}