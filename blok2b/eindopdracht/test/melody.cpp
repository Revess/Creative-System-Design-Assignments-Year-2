#include <iostream>
#include <time.h>
#include <vector>
#include <string>
#include <math.h>
#include "melody.h"
using namespace std;

Melody::Melody(vector<vector<string> > &notes){
    //Upon starting there will be items added to the array
    srand (time(NULL));
    int randomChoise = (rand() % notes.size());
    newNote = notes[randomChoise][(rand()%2)+1];
    prevNote = newNote;
}

Melody::~Melody(){
}

double Melody::getNote(vector<vector<string> > &notes){
    //Gets a random note from the list based on the previous one, uses a random number to pick one or the other.
    for(int i = 0; i < notes.size(); i++){
        if(notes[i][0] == prevNote){
            newNote = notes[i][(rand()%2)+1];
            prevNote = newNote;

            //convert the note to a frequency, based on midi notes;
            for(int i = 0; i<sizeof(midiNotes)/sizeof(midiNotes[0]); i++){
                if((int)newNote[0] == midiNotes[i][0]){
                    double midiNote = midiNotes[i][1]+((newNote[1]-48)*12);
                    frequency = 440.0*pow(2.0,(midiNote-69)/12);
                    return frequency;
                }
            }
        }
    }
    return 2;
}