#include <iostream>
#include <time.h>
#include <string>
#include <vector>
#include <fstream>
#include <conio.h>
#include "melody.h"
using namespace std;

int main(){
    ifstream inFile;
    vector<vector<string> > notes;
    vector<string> temporary;
    string note;


    inFile.open("doc/possibilities.txt");
    if(!inFile){
        cout<<"Unable to open file"<<endl;
        exit(1);
    }
    //Fill a vector with the input of the user, the vector is a 2d vector with the markovchain rules
    while(inFile >> note){
        if(note == "//"){
            notes.push_back(temporary);
            temporary.clear();
        }else {
            temporary.push_back(note);
        }
    }
    inFile.close();

    Melody melody(notes);

    cout<<melody.getNote(notes)<<endl;
    
    return 0;
}