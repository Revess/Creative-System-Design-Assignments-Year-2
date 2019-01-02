#include <iostream>
#include <time.h>
#include <string>
#include <fstream>
#include <conio.h>
#include "melody.h"
using namespace std;

int main(){
    ifstream inFile;
    inFile.open()

    int notes[4][3]={{3},{5,4,3},{3,5,4},{4,5,3}};
    Melody melody(notes);

    cout<<melody.getNote(notes)<<endl;
    
    return 0;
}