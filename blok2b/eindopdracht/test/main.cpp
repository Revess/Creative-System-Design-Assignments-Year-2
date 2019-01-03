#include <iostream>
#include <string>
#include <conio.h>
#include <windows.h>
#include <vector>
#include <fstream>
#include "melody.h"
using namespace std;

int main(){
    //Variables
    int test = 0;

    ifstream inFile;
    vector<vector<string> > notes;
    vector<string> temporary;
    string note;

    //Reading out the file
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

    //Initiate the melody calculator
    Melody melody(notes);

    //Start of notes loop
    while(true){
        cout<<melody.getNote(notes)<<endl;
        test++;
        Sleep(500);
        if(test >= 5){
            break;
        }
    }
    return 0;
}