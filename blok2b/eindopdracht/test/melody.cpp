#include <iostream>
#include <time.h>
#include "melody.h"
using namespace std;

Melody::Melody(int (&notes)[4][3]){
    //Upon starting there will be items added to the array
    srand (time(NULL));
    int randomChoise = (rand() % notes[0][0])+1;
    newNote = notes[randomChoise][(rand()%2)+1];
    prevNote = newNote;
}

Melody::~Melody(){
}

int Melody::getNote(int (&notes)[4][3]){
    //Gets a random note from the list based on the previous one, uses a random number to pick one or the other.
    for(int i = 0; i < notes[0][0]; i++){
        if(notes[i+1][0] == prevNote){
            newNote = notes[i+1][(rand()%2)+1];
            prevNote = newNote;
            return newNote;
        }
    }
    return 2;
}