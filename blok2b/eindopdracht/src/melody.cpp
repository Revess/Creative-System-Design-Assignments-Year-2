#include <iostream>
#include <time.h>
#include <vector>
#include <string>
#include <math.h>
#include "melody.h"
using namespace std;

Melody::Melody(vector<vector<string> > &notes, vector<double> &rhythm, int bpm){
    //Upon starting there will be items added to the array
    srand (time(NULL));
    int randomChoise = (rand() % notes.size());
    newNote = notes[randomChoise][(rand()%(notes[0].size()-1))+1];
    prevNote = newNote;
    position = randomChoise;

    this->bpm = bpm;

    newRhythm = rhythm[randomChoise];
    prevRhythm = newRhythm;
}

Melody::~Melody(){
}

double Melody::getNote(vector<vector<string> > &notes){
    //Gets a random note from the list based on the previous one, uses a random number to pick one or the other.
    for(int i = 0; i < notes.size(); i++){
        if(notes[i][0] == prevNote){
            position = i;
            newNote = notes[i][(rand()%(notes[0].size()-1))+1];
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

double Melody::getRhythm(vector<double> &rhythm){
    //Give back the next rhythm value of the chain
    newRhythm = rhythm[position];
    prevRhythm = newRhythm;
    return newRhythm * (60000/bpm);
}