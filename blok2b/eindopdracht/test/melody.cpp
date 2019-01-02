#include <iostream>
#include <time.h>
#include <vector>
#include <string>
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

string Melody::getNote(vector<vector<string> > &notes){
    //Gets a random note from the list based on the previous one, uses a random number to pick one or the other.
    for(int i = 0; i < notes.size(); i++){
        if(notes[i][0] == prevNote){
            newNote = notes[i][(rand()%2)+1];
            prevNote = newNote;
            return newNote;
        }
    }
    return "ERROR";
}